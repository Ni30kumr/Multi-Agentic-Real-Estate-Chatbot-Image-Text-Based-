# Multi-Agentic Real Estate Chatbot (Image + Text Based)

This project implements a multi-agent real estate assistant chatbot developed as a solution for the **PROPERTYLOOP ASSESSMENT** task. It addresses real estate-related queries by specializing in two areas: detecting property issues from images and answering tenancy law questions.

---

## Objective

Create a multi-agent system capable of solving real estate issues through two specialized virtual agents:
- **Issue Detection & Troubleshooting Agent (Image + Text)**
- **Tenancy FAQ Agent (Text-based)**

---

## Approach

- Uses **LangGraph** to orchestrate agents.
- An **Agent Router** automatically decides the best agent based on:
  - Presence of an uploaded image.
  - Text classification of the user's query.
- If the intent is unclear, the bot will ask clarifying questions.

---

## Agents

### 🛠️ Issue Detection & Troubleshooting Agent
- Accepts user-uploaded property images and optional text.
- Detects visible issues (e.g., mold, water damage, broken fixtures).
- Provides troubleshooting advice and repair suggestions.
- May ask clarifying follow-up questions.

**Example:**
> **User:** "What's wrong with this wall?" (uploads image)  
> **Agent:** "It appears there is mold near the ceiling. Check for leaks and use a dehumidifier."

---

### 📜 Tenancy FAQ Agent
- Handles FAQs about tenancy laws, agreements, rental procedures.
- Can provide location-specific advice if the city/country is provided.

**Example:**
> **User:** "Can my landlord evict me without notice?"  
> **Agent:** "In most cases, written notice is required unless in emergencies. Please share your location for specific advice."

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Ni30kumr/Multi-Agentic-Real-Estate-Chatbot-Image-Text-Based-.git
cd Multi-Agentic-Real-Estate-Chatbot-Image-Text-Based-
```

---

### 2. Create a Virtual Environment

**For Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

**For macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup Environment Variables

Create a `.env` file in the root directory with the following content:

```plaintext
GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
TAVILY_API_KEY="YOUR_TAVILY_API_KEY"
```

Get your API keys from:
- **Google Cloud (Gemini)**
- **Tavily Search**

---

### 5. Running the Application

Activate your virtual environment, then run:

```bash
streamlit run app.py
```

This will start the Streamlit server and open the application in your web browser automatically.

---

## Usage

- Enter your tenancy law question in the text field.
- Optionally upload a property image if your query relates to analyzing property issues.
- Click "Submit Query" to receive a response from the appropriate agent.

---

## Tools and Platforms Used

### AI Platforms:
- **LangChain**
- **LangGraph**
- **Google Gemini 1.5 Flash** (for text and image understanding)

### Other Tools:
- **Streamlit** (for frontend UI)
- **python-dotenv** (for environment variable management)
- **Tavily Search** (for web search integration)

---

## Agent Workflows

- **FAQ Agent:** Fetches and summarizes tenancy law-related information.
- **Image Agent:** Analyzes property images and suggests fixes.
- **Clarification Node:** If query is unclear, the system asks clarifying questions.

---

## Example Questions

- "What is the ideal advance rent to pay for a flat in the US?"
- "How much notice do I need to give before vacating in the US?"
- "Can you analyze this property image for any issues?"

---

# 📌 End of Documentation
