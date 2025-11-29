AI Agent Development Challenge – HR Assistant Agent

This project is developed for the **48-Hour AI Agent Development Challenge.  
The goal is to build a fully functional AI agent that solves real-world problems in **HR, Operations, Sales, Marketing, or Support.

1. Overview

The HR Assistant Agent is designed to answer HR-related queries such as:

- Company policies  
- Leave and benefits  
- Payroll & salary questions  
- IT & tool usage  
- FAQs  

This project demonstrates practical AI engineering ability using modern AI models, vector databases, and retrieval techniques.

2. Features

Answer HR policy, leave, and benefits queries  
Retrieve information from a knowledge base  
Provide quick, accurate, and context-aware responses  
 Easy to update knowledge base for new policies  

Limitations:

Only answers questions present in the knowledge base  
Does not handle real-time dynamic HR workflows (future enhancement possible)  

3. Tech Stack

AI Models: OpenAI GPT, sentence-transformers embeddings  
Frameworks: LangChain, FAISS  
UI: Streamlit  
Database/Storage:Local vector store (FAISS)  
Languages:Python  

 4. Knowledge Base

- The knowledge is stored in a single file: "knowledge.txt"
- Example entries:

HR Knowledge Base
Leave Policies
Casual Leave: 12 days/year
Sick Leave: 10 days/year
Maternity Leave: 26 weeks
Work Hours
9:30 AM - 6:30 PM
Remote work: max 2 days/week
Employee Benefits
Health Insurance: up to ₹5,00,000/year
Retirement Fund: 12% monthly

 You can update this file with new policies, payroll info, IT procedures, or FAQs.

 5. Setup & Run Instructions
 1. Clone the Project
git clone <your-repo-url>
cd hr-assistant-agent

2. Create & Activate Virtual Environment
python -m venv .venv
.venv\Scripts\activate    

3. Install Dependencies
pip install -r requirements.txt

4. Run the App
streamlit run app.py