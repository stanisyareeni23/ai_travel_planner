
# ✈️ Autonomous AI Travel Planner

An intelligent AI-powered travel planner that generates personalized travel itineraries using Retrieval-Augmented Generation (RAG), FastAPI, FAISS vector database, and Streamlit.

This system retrieves real travel information from a custom knowledge base and generates realistic travel plans including daily itinerary, budget estimation, hotel suggestions, and travel tips.

---

# 🚀 Features

- 🧠 AI-powered itinerary generation using RAG
- 📅 Day-wise structured travel plan
- 💰 Budget estimation and breakdown
- 🏨 Hotel suggestions (Luxury / Mid / Budget)
- 📍 Uses real travel data from knowledge base
- ⚡ FastAPI backend for scalable API
- 🎨 Streamlit frontend with modern UI
- 🔎 FAISS vector search for semantic retrieval
- 📖 Travel tips and recommendations

---

# 🧠 How It Works (RAG Pipeline)

1. Travel data stored in `tourism_india.txt`
2. Text is split into chunks
3. Chunks converted into embeddings using Sentence Transformers
4. Stored in FAISS vector database
5. User query converted into embedding
6. Relevant chunks retrieved using vector search
7. LLM generates accurate itinerary based on retrieved context
8. Result sent to frontend and displayed

This ensures accurate, real-world travel plans.

---

# 🏗️ Project Architecture


User Input (Streamlit UI)
↓
FastAPI Backend (/query)
↓
RAG Pipeline
↓
FAISS Vector Search
↓
Retrieve travel knowledge
↓
LLM generates itinerary
↓
Response sent to frontend


---

# 🛠️ Tech Stack

## Frontend
- Streamlit
- Python

## Backend
- FastAPI
- Python

## AI / RAG
- Groq LLM
- Sentence Transformers
- FAISS Vector Database

## Database
- SQLite (optional)

---

# 📂 Project Structure

ai_travel_planner/
│
├── backend/
│   │
│   ├── database/
│   │   ├── db.py             → DB / vector connection
│   │   └── dep.py            → Dependency injection
│   │
│   ├── models/
│   │   ├── pydantic.py       → Request/response schemas
│   │   └── table.py          → SQLAlchemy tables (optional)
│   │
│   ├── services/
│   │   └── rag.py            → FAISS + RAG Logic
│   │
│   ├── routes/
│   │   └── routes.py         → API endpoints
│   │
│   └── main.py               → FastAPI app entry
│
├── frontend/
│   └── app.py                → Streamlit UI
│
├── data/
    ├── tourism_india.txt    



---

# ⚙️ Installation

## Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/ai_travel_planner.git
cd ai_travel_planner

Create virtual environment
python -m venv .venv


Activate:

Windows:

.venv\Scripts\activate


Mac/Linux:

source .venv/bin/activate

Install dependencies
pip install -r requirements.txt

▶️ Run Backend
cd backend
uvicorn main:app --reload


Backend runs at:

http://127.0.0.1:8000

▶️ Run Frontend
cd frontend
streamlit run app.py


Frontend runs at:

http://localhost:8501

🔐 Environment Variables

Set your API key securely:

GROQ_API_KEY=your_api_key_here


Do NOT hardcode API keys.

📊 Example Output

The system generates:

Best Time to Visit

Estimated Budget

Day-wise itinerary

Budget breakdown

Travel tips

Hotel suggestions

🌍 Deployment

Backend can be deployed on:

Render

Railway

AWS

Frontend can be deployed on:

Streamlit Cloud

🎯 Use Cases

AI Travel Planner

Tourism recommendation system

GenAI portfolio project

RAG learning project

Intelligent assistant systems

🔮 Future Improvements

User login system

Save trip history

PDF export

Google Maps integration

Flight and hotel booking integration

Multi-country support

👩‍💻 Author

Stanisya Reeni
MCA Student
AI / GenAI Developer