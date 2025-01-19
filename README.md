# VISDAK Chatbot

VISDAK Chatbot is a powerful AI-driven solution that enables businesses to manage their WhatsApp Business and Meta accounts effectively. It integrates AI models to provide automated responses based strictly on business-provided data.

## Features

- **WhatsApp Business Integration:** Seamlessly handle customer queries via WhatsApp.

- **Meta API Integration:** Webhook-based automation for Meta interactions.

- **Hybrid Query Classification:** Combines keyword-based detection with LLM fallback.

- **Structured Data Handling:** PostgreSQL with pgvector for optimized storage and retrieval.

- **AI-Powered Responses:** Utilizes OpenAI models for intelligent query processing.

## Tech Stack

- **Backend:** Flask (Python)

- **Database:** PostgreSQL with pgvector

- **AI Models:** OpenAI API

- **Frontend:** Next.js (for landing page and demo)

- **Deployment:** Linux servers

## Project Structure

```
visdak-chatbot/
├── app.py                   # Main Flask application entry point
├── config.py                # Configuration settings
├── requirements.txt         # Dependencies
├── .env                     # Environment variables
├── routes/
│   ├── chatbot.py            # Handles chatbot queries
│   ├── webhooks.py           # Handles Meta webhooks
│   ├── users.py              # User management
├── models/
│   ├── database.py           # PostgreSQL connection
│   ├── embeddings.py         # pgvector utilities
├── services/
│   ├── structured_queries.py # SQL query handling
│   ├── semantic_search.py    # Semantic search using pgvector
│   ├── classification.py     # Hybrid query classification
├── utils/
│   ├── logger.py             # Logging utility
│   ├── helpers.py            # Helper functions
└── README.md                 # Project documentation
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourrepo/visdak-chatbot.git

   cd visdak-chatbot
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv

   source venv/bin/activate  # On Windows use  `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables in `.env` file:
   ```env
   META_APP_ID=your_meta_app_id
   META_APP_SECRET=your_meta_app_secret
   PG_HOST=your_postgres_host
   PG_PORT=your_postgres_port
   PG_USER=your_postgres_user
   PG_PASSWORD=your_postgres_password
   PG_DATABASE=your_postgres_db
   OPENAI_API_KEY=your_openai_api_key
   FLASK_SECRET_KEY=your_flask_secret_key
   ```

## Running the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```
2. The server will run on `http://localhost:5000`

## API Endpoints

- `POST /chat` - Process user query.
- `POST /webhook` - Handle WhatsApp and Meta webhooks.
- `GET /health` - Check server health status.

## Deployment

1. Set up a Linux server (Ubuntu recommended).
2. Install required dependencies:
   ```bash
   sudo apt update && sudo apt install python3-pip python3-venv
   ```
3. Run the application in production using Gunicorn:
   ```bash
   gunicorn --bind 0.0.0.0:5000 app:app
   ```
