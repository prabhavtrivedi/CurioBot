import React, { useState, useEffect } from "react";
import axios from "axios";
import './App.css';

function App() {
  const [question, setQuestion] = useState(""); // State for user input
  const [answer, setAnswer] = useState(""); // State for AI's response
  const [history, setHistory] = useState([]); // State for question/answer history
  const [loading, setLoading] = useState(false); // State for loading status
  const [error, setError] = useState(""); // State for error messages

  // Fetch question/answer history on component mount
  useEffect(() => {
    async function fetchHistory() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/history/");
        setHistory(response.data);
      } catch (error) {
        console.error("Error fetching history:", error);
        setError("Failed to fetch question history.");
      }
    }
    fetchHistory();
  }, []);

  // Handle question submission
  const handleAsk = async () => {
    setError(""); // Clear previous errors
    setLoading(true);

    // Validate input
    if (!question.trim()) {
      setError("Question cannot be empty!");
      setLoading(false);
      return;
    }
    if (question.length > 300) {
      setError("Question is too long. Please limit it to 300 characters.");
      setLoading(false);
      return;
    }

    try {
      const response = await axios.post("http://127.0.0.1:8000/ask/", { question });
      setAnswer(response.data.answer); // Update state with AI response
      setHistory([...history, { question, answer: response.data.answer }]); // Append to history
    } catch (error) {
      if (error.response && error.response.data.detail) {
        setError(error.response.data.detail); // Backend error
      } else {
        setError("An unexpected error occurred. Please try again."); // General error
      }
    } finally {
      setLoading(false); // Reset loading state
    }
  };

  return (
    <div>
      <h1>CurioBot</h1>

      {/* User input */}
      <textarea
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Type your question here..."
        rows="5"
        cols="50"
      />
      <br />
      {error && <p className="error">{error}</p>} {/* Error messages */}
      <button onClick={handleAsk} disabled={loading}>
        {loading ? "Asking..." : "Ask"}
      </button>

      {/* Display AI response */}
      <h2>Answer:</h2>
      <p>{answer}</p>

      {/* Display question/answer history */}
      <h2>Question History:</h2>
      <ul>
        {history.map((item, index) => (
          <li key={index}>
            <strong>Q:</strong> {item.question} <br />
            <strong>A:</strong> {item.answer}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
