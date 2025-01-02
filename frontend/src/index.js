import React from 'react'; // Core React library for component creation
import ReactDOM from 'react-dom/client'; // ReactDOM for rendering components to the DOM
import './index.css'; // Global CSS styling
import App from './App'; // Main application component
import reportWebVitals from './reportWebVitals'; // Tool for measuring performance

// Create a root DOM node and render the React component tree
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode> {/* Enable additional checks in development mode */}
    <App /> {/* Render the main application component */}
  </React.StrictMode>
);

// Optional: Measure performance of the app
// Log results to console or send to an analytics endpoint
reportWebVitals();
