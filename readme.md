# Multi-Agentic Real Estate Chatbot (Image + Text Based)

This project implements a multi-agent real estate assistant chatbot, developed as a solution for the PROPERTYLOOP ASSESSMENT task. It's designed to address real estate-related queries by specializing in two distinct areas: detecting property issues from images and providing expertise on tenancy laws.

## Objective

The main objective is to create a multi-agent system capable of solving real estate issues with a specialization split into two distinct virtual agents: an Issue Detection & Troubleshooting Agent (Image + Text) and a Tenancy FAQ Agent (Text-based).

## Approach

The system utilizes a multi-agent architecture orchestrated by **LangGraph**. An **Agent Router/Manager** automatically identifies which agent should respond based on the user's input. The routing logic considers:

* Text classification (determining if the query is an FAQ or an issue description).
* The presence of an uploaded image.

As a fallback, if the intent is unclear, the chatbot is designed to ask a clarifying question to route the query to the correct agent.

The project is built with **Streamlit** for the frontend interface, **LangChain** and **LangGraph** for agent orchestration, **Google Gemini 1.5 Flash** for large language and vision model capabilities, and **Tavily Search** for web search.

### Agent 1: Issue Detection & Troubleshooting Agent (Image + Text)

**Responsibilities:**

* Accepts user-uploaded images of properties, along with optional textual context. [cite: 3]
* Detects visible issues in the property (e.g., water damage, mold, cracks, poor lighting, broken fixtures) using the vision capabilities of the integrated language model. [cite: 4]
* Provides troubleshooting suggestions based on the detected issues, such as recommending contacting a plumber [cite: 5] or suggesting specific repair methods like using anti-damp coating. [cite: 5]
* Can ask clarifying follow-up questions to diagnose issues better. [cite: 6]

**Example Interaction:**

* **User:** "What's wrong with this wall?" (User uploads image) [cite: 6]
* **Agent 1:** "It appears there is mould growth near the ceiling. This might be due to high humidity or a leak. I recommend checking for water seepage and using a dehumidifier." [cite: 7]

### Agent 2: Tenancy FAQ Agent (Text-based)

**Responsibilities:**

* Handles frequently asked questions related to tenancy laws, agreements, landlord/tenant responsibilities, and rental processes. [cite: 7]
* Capable of giving location-specific guidance if the user's city or country is provided. [cite: 8]
* Can answer common questions like "How much notice do I need to give before vacating?"[cite: 9], "Can my landlord increase rent midway through the contract?"[cite: 10], or "What to do if the landlord is not returning the deposit?". [cite: 11]

**Example Interaction:**

* **User:** "Can my landlord evict me without notice?" [cite: 11]
* **Agent 2:** "In most jurisdictions, landlords must give written notice before eviction, unless it's an emergency situation like non-payment or illegal activity. Please let me know your city or region for more accurate info." [cite: 12]

## Setup

Follow these steps to set up and run the project locally:

### Prerequisites

* Python 3.8 or higher
* Git

### 1. Clone the Repository

First, clone the project repository to your local machine:

git clone [https://github.com/Ni30kumr/Multi-Agentic-Real-Estate-Chatbot-Image-Text-Based-.git](https://github.com/Ni30kumr/Multi-Agentic-Real-Estate-Chatbot-Image-Text-Based-.git)
cd Multi-Agentic-Real-Estate-Chatbot-Image-Text-Based-
2. Create a Virtual Environment
It's highly recommended to create a virtual environment to manage project dependencies.

Bash

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
3. Install Dependencies
Install the required Python packages using the requirements.txt file:

Bash

pip install -r requirements.txt
4. Create a .env file
You need to create a .env file in the root directory of the project to store your API keys. Get your API keys for:

Google Cloud: Obtain a GOOGLE_API_KEY for accessing the Gemini model.
Tavily Search: Obtain a TAVILY_API_KEY for web search capabilities.
Create a file named .env in the project root and add the following lines, replacing "YOUR_GOOGLE_API_KEY" and "YOUR_TAVILY_API_KEY" with your actual keys:


GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
TAVILY_API_KEY="YOUR_TAVILY_API_KEY"

5. File Structure
The main files and directories in this project are:

├── .gitignore          # Specifies intentionally untracked files that Git should ignore
├── app.py              # The main Streamlit application and LangGraph agent logic
├── main.py             # just python code for testing purpose
├── requirements.txt    # Lists the project's Python dependencies
└── uploaded_image.jpg  # Placeholder or saved uploaded image

Running the Application
To run the Streamlit application, make sure your virtual environment is activated and then run:
streamlit run app.py

This will start the Streamlit development server, and your web browser should open automatically to the application interface.

Usage
Enter your tenancy law question in the text input field.
Optionally, upload a property image if your query relates to analyzing an image for issues.
Click the "Submit Query" button to get a response from the appropriate agent.
Tools and Platforms Used
Based on the code and the allowed tools mentioned in the assessment document, this project utilizes:   

AI Platforms: LangChain, LangGraph, Google Gemini 1.5 Flash.
Image Analysis: Implicitly handled by the vision capabilities of Google Gemini 1.5 Flash.
Other Tools: Streamlit (for UI), python-dotenv (for environment variables), Tavily Search (for web search).
This README serves as documentation for the project, outlining the tools used, the logic behind agent switching, how image-based issue detection works, and covering the use case examples  




