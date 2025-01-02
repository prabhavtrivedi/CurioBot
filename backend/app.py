from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from database import log_to_db, fetch_history

# Initialize the FastAPI app
app = FastAPI()

# Allow CORS for your frontend application
origins = [
    "http://localhost:3000",  # React app running on localhost
    "http://127.0.0.1:3000",  # Alternative localhost URL
]

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Specify the allowed origins
    allow_credentials=True,  # Allow cookies and credentials
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all HTTP headers
)

# Hugging Face API configuration
API_URL = "https://api-inference.huggingface.co/models/google/gemma-2-2b-it"  # AI model endpoint
HEADERS = {
    "Authorization": "Bearer "  # Replace with your Hugging Face API token
}

# Define the schema for the question payload using Pydantic
class Question(BaseModel):
    question: str  # The user's question
    temperature: float = 0.1  # Controls randomness in the output
    max_tokens: int = 100  # Limits the length of the response
    top_p: float = 0.9  # Controls diversity of the output
    frequency_penalty: float = 0.5  # Penalizes repetitive phrases
    presence_penalty: float = 0.5  # Penalizes introducing new topics

# Health check endpoint
@app.get("/health")
def health_check():
    """
    Endpoint to verify if the server is running and responsive.
    """
    return {"status": "healthy"}

# Endpoint to handle question and response
@app.post("/ask/")
def ask_question(q: Question):
    """
    Endpoint to handle user questions and get AI-generated answers.
    Validates the question and forwards it to the Hugging Face API.
    """
    # Validate that the question is not empty
    if not q.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    try:
        # Prepare parameters for the Hugging Face API request
        params = {
            "inputs": q.question,  # The user's question
            "temperature": q.temperature,  # Randomness control
            "max_tokens": q.max_tokens if q.max_tokens else 500,  # Response length
            "top_p": q.top_p,  # Diversity control
            "frequency_penalty": q.frequency_penalty,  # Penalize repetitive responses
            "presence_penalty": q.presence_penalty  # Encourage topic adherence
        }

        # Send a POST request to the Hugging Face API
        response = requests.post(API_URL, headers=HEADERS, json=params)
        response.raise_for_status()  # Raise an error for unsuccessful requests

        # Parse the response from the AI model
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            answer = result[0]["generated_text"].strip()
            log_to_db(q.question, answer)  # Log the question and answer to the database
            return {"answer": answer}  # Return the AI-generated answer

        # Raise an error if the response format is unexpected
        raise HTTPException(status_code=500, detail="Unexpected AI response format.")

    except requests.exceptions.RequestException:
        # Handle network-related errors
        raise HTTPException(status_code=503, detail="Network error. Please try again later.")
    except Exception:
        # Handle other unexpected errors
        raise HTTPException(status_code=500, detail="Something went wrong. Please try again.")

# Endpoint to retrieve question/answer history
@app.get("/history/")
def get_history():
    """
    Endpoint to retrieve the question/answer history from the database.
    """
    try:
        # Fetch history from the database
        history = fetch_history()
        # Return the history in a serialized format
        return [{"question": h.question, "answer": h.answer} for h in history]
    except Exception as e:
        # Handle errors while fetching history
        raise HTTPException(status_code=500, detail=f"Error fetching history: {str(e)}")
