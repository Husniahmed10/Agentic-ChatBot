# 🤖 LangGraph AgenticAI - Streamlit Application

LangGraph AgenticAI is an interactive **Streamlit-based AI framework** designed to integrate **LLM models** (like Groq) with **graph-based agentic reasoning**.  
It allows users to select different **use cases**, configure **LLMs**, and visualize intelligent agent workflows dynamically.

---

## 🚀 Features

- 🧠 **Modular LLM Integration:** Plug-and-play support for multiple LLMs (Groq, etc.)  
- 🕸️ **Graph-Based Architecture:** Dynamically constructs reasoning and tool graphs based on the selected use case  
- 💬 **Interactive Streamlit UI:** Simple, responsive interface for users to select models, use cases, and enter prompts  
- 🔗 **Tool Integration:** Supports external API tools like Tavily for web search and news aggregation  
- 📰 **AI News Fetcher:** Built-in “AI News” use case with selectable time frames (Daily / Weekly / Monthly)  
- ⚙️ **Configurable:** Flexible configuration using centralized `Config` class  

---

## ⚙️ How It Works

### 1️⃣ Load the Streamlit UI
Users select:
- LLM Provider (e.g., Groq)
- Model variant
- Use case (e.g., AI News, Chatbot With Web)
- API keys for required services

### 2️⃣ Configure LLM & Graph
The app uses:
- `GroqLLM` → Initializes and configures the selected model  
- `GraphBuilder` → Constructs the reasoning graph for the chosen use case  

### 3️⃣ Generate & Display Results
Once the user submits input:
- The system processes the query through the LLM
- Builds a use-case-specific reasoning flow
- Displays structured results using `DisplayResultStreamlit`

---

## 🔑 Required API Keys

Depending on your selected use case, you may need:

| API Key | Purpose | Required For |
|----------|----------|--------------|
| `GROQ_API_KEY` | To access Groq LLM API | All Groq LLM use cases |
| `TAVILY_API_KEY` | To fetch live web or AI news data | Chatbot With Web / AI News |

You can obtain them here:
- [Groq API Keys](https://console.groq.com/keys)  
- [Tavily API Keys](https://tavily.com/)

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** (Frontend UI)
- **LangGraph AgenticAI Core**
- **Groq API**
- **Tavily API**

---
