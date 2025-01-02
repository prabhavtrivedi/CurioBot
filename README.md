## CurioBot
CurioBot is a web-based application that enables users to ask questions and receive intelligent answers generated by an AI model. It includes a FastAPI backend and a React frontend, designed with a clean and modular architecture for easy development and deployment.

## Features
AI-powered Q&A: Utilizes Hugging Face's google/gemma-2-2b-it model for intelligent responses.
Question History: Stores user queries and responses in a local SQLite database.
User-Friendly Interface: Simple and interactive UI for seamless user experience.

## Folder Structure
ai-qa-app/
├── backend/             # FastAPI backend
│   ├── app.py           # Main application
│   ├── database.py      # Database operations
│   ├── qa_history.db    # SQLite database
│   └── venv/            # Virtual environment
└── frontend/            # React frontend
    ├── src/             # Source code
    ├── public/          # Public assets
    └── package.json     # Node.js dependencies

## Setup and Installation

# Prerequisites
Python 3.10+
Node.js 16+
npm (comes with Node.js)

# Clone the Repository
git clone https://github.com/your-repo/CurioBot.git
cd CurioBot

# Backend Setup
1.Navigate to the backend directory:
cd backend
2.Create and activate a virtual environment:
On Windows:
python -m venv venv
.\venv\Scripts\activate

On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

3.Install dependencies:
pip install -r requirements.txt

4.Start the FastAPI server:
uvicorn app:app --reload

# Frontend Setup
1.Navigate to the frontend directory:
cd frontend

2.Install Node.js dependencies:
npm install

3.Start the React development server:
npm start


## Running the Application Locally
1.Ensure the backend server is running on http://127.0.0.1:8000.
2.Access the frontend at http://localhost:3000 in your browser.
3.Interact with the application: Ask questions and view responses.

### AI Service

# Chosen Model:google/gemma-2-2b-it

## Reason for Selection:

# Accuracy and Relevance:
The model excels at providing accurate and contextually relevant answers, making it a reliable choice for general-purpose question-answering applications.
# Optimized for Question-Answering:
Specifically fine-tuned for question-answering tasks, ensuring high-quality and meaningful responses.
# Hugging Face Integration:
Easily integrates with Hugging Face's API, simplifying implementation and enhancing scalability for production-level applications.
# Open Source and Free:
Being open source and free to use, it significantly reduces costs compared to proprietary models like OpenAI GPT-4 or Anthropic Claude.
# Cost Efficiency:
No licensing or API fees, making it a budget-friendly solution for small-scale projects or startups.
# Customizability:
Open-source nature allows for fine-tuning and custom modifications to better suit specific project needs.
# Comparative Advantages:
OpenAI GPT Models (e.g., GPT-3.5/4): While highly capable, these models are not open-source and incur significant usage costs, making them less ideal for projects with budget constraints.
Anthropic's Claude: Offers impressive natural language capabilities but lacks open-source accessibility and is expensive.
Cohere: Powerful for NLP tasks but often geared towards enterprise use with associated costs.
Hugging Face Transformers (open-source): While comparable, google/gemma-2-2b-it was chosen for its specific tuning for question-answering tasks.
Local Deployment Models (e.g., Llama 2, GPT-J): Though viable, they demand extensive computational resources and infrastructure for hosting, which might be infeasible for this project.
# Scalability:
The model’s lightweight and efficient architecture ensures it can handle scalable use cases while maintaining low latency, especially when integrated via Hugging Face.
# Ease of Use:
Pre-trained and hosted by Hugging Face, eliminating the need for extensive computational resources or setup for deployment.
# Community Support:
Active support and documentation through Hugging Face and the open-source community, enabling troubleshooting and continuous updates.
This combination of features makes google/gemma-2-2b-it an ideal choice for this project, balancing performance, cost-efficiency, and ease of integration.

## To create access tokens for using Hugging Face models, follow these steps:

# Step 1: 
Create a Hugging Face Account
Go to the Hugging Face website.
Click on the Sign Up button in the top-right corner (or Log In if you already have an account).
Complete the sign-up process by entering your email, username, and password, or use a third-party authentication method (e.g., GitHub, Google).

# Step 2: 
Access Your Hugging Face Account Settings
After logging in, click on your profile icon in the top-right corner of the page.
From the dropdown menu, select Settings.

# Step 3: 
Create an Access Token
In the Settings menu, go to the Access Tokens tab.
Click the New Token button to create a new token.
Provide a name or description for your token (e.g., “My API Token”).
Choose the scope of the token:
Read: Access to models and datasets (most common for API usage).
Write: Allows modifying models or datasets.
Admin: Full access to your Hugging Face account (less common).
Click Generate Token to create your access token

# Step 4: 
Store the Token
Your newly generated token will be displayed on the page. Copy the token immediately because you won't be able to view it again after you navigate away.
Store the token securely (e.g., in an environment variable or a configuration file), as it grants access to Hugging Face models and APIs.

## Code Quality

# Modular Design: 
Separate files and functions for database, routes, and UI components.
# Clean Code: 
Commented and structured for readability.
# Error Handling:
Backend: Handles invalid inputs, API timeouts, and database errors.
Frontend: Displays user-friendly error messages for network or server issues.
