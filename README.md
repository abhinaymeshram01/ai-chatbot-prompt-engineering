# 🤖 AI Persona Assistant

A conversational AI chatbot built with **Python, Google Gemini, and Streamlit** that supports context-aware conversations, multiple AI personas, prompt engineering, conversation memory, streaming responses, and basic API error handling.

The project focuses on understanding the core concepts behind modern LLM applications rather than simply calling an API.

## 🚀 Live Demo

👉 **[Try the AI Persona Assistant](https://ai-chatbot-prompt-engineering.streamlit.app/)**

---

## 📌 Project Overview

The AI Persona Assistant is a conversational AI application powered by the **Google Gemini API**.

Users can choose between three different AI personas:

- 👨‍💻 **Coding Tutor**
- 🤝 **Friendly Assistant**
- 😏 **Sarcastic Buddy**

Each persona uses a different system prompt to control the AI's behavior, communication style, and response approach.

The chatbot also maintains conversation history so the AI can understand previous messages within the current conversation.

---

## ✨ Features

- 🤖 Google Gemini API integration
- 🎭 Three different AI personas
- 🧠 Context-aware conversation memory
- 🔄 Persona switching
- 🧹 Conversation memory reset
- ⚡ Streaming AI responses
- 🛡️ Basic API error handling
- ✍️ Prompt engineering
- 💬 Interactive Streamlit chat interface
- 🔐 Environment-based API key management
- 🧩 Modular project structure

---

## 🎭 Personas

### 👨‍💻 Coding Tutor

An experienced coding tutor that helps users understand programming concepts, debug code, and improve their programming skills.

**Behavior:**

- Explains concepts clearly
- Encourages users to understand solutions
- Provides constructive corrections
- Supports multiple programming languages
- Breaks large implementations into logical sections

---

### 🤝 Friendly Assistant

A helpful and approachable AI assistant designed for general questions, learning, and problem solving.

**Behavior:**

- Friendly communication
- Clear explanations
- Helpful responses
- Patient interaction
- Professional and respectful tone

---

### 😏 Sarcastic Buddy

A helpful conversational assistant with a playful personality and light sarcasm.

**Behavior:**

- Casual communication
- Helpful responses
- Light humor and sarcasm
- Still prioritizes accurate information

---

## 🧠 Prompt Engineering

Each persona is controlled using a dedicated system prompt.

The prompts define:

- Role
- Personality
- Communication style
- Response behavior
- Restrictions
- Instruction-following behavior

The project demonstrates how changing system instructions can influence the behavior and communication style of the same underlying LLM.

Persona prompts are stored separately in:

```text
config/prompts.py
```

This keeps the AI behavior separate from the application logic.

---

## 💬 Conversation Memory

The chatbot maintains conversation history using a custom `ConversationMemory` class.

### Conversation Flow

```text
User Message
     ↓
Conversation Memory
     ↓
Conversation History
     ↓
Gemini API
     ↓
AI Response
     ↓
Conversation Memory
```

The conversation history allows Gemini to use previous messages as context when generating new responses.

When the user switches personas or clears the conversation, the conversation memory is reset.

---

## ⚡ Streaming Responses

The application uses Gemini's streaming generation API to display responses progressively.

Instead of waiting for the complete response, the application receives and displays response chunks as they are generated.

```text
User
 ↓
Gemini
 ↓
Chunk 1
 ↓
Chunk 2
 ↓
Chunk 3
 ↓
...
 ↓
Complete Response
```

Streamlit's `st.write_stream()` is used to display the generated chunks.

---

## 🛡️ Error Handling

The application includes basic error handling for Gemini API failures.

If the API request fails, the application:

1. Captures the exception
2. Logs the actual error for debugging
3. Removes the failed user message from conversation memory
4. Displays a user-friendly error message

Example:

> ⚠️ Sorry, I couldn't generate a response right now. Please check your API connection and try again.

---

## 🏗️ Project Architecture

```text
                    ┌───────────────────┐
                    │     Streamlit     │
                    │        UI         │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Persona Selection │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   Chatbot Logic   │
                    └─────────┬─────────┘
                              │
                ┌─────────────┴─────────────┐
                ▼                           ▼
        ┌───────────────┐           ┌───────────────┐
        │    Memory     │           │ Persona Prompt│
        │   Management  │           │   Selection   │
        └───────┬───────┘           └───────┬───────┘
                │                           │
                └─────────────┬─────────────┘
                              ▼
                    ┌───────────────────┐
                    │   Google Gemini   │
                    │       API         │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Streaming Response│
                    └───────────────────┘
```

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| **Language** | Python |
| **Generative AI** | Google Gemini API, Google GenAI SDK |
| **UI** | Streamlit |
| **Prompting** | System Prompts, Prompt Engineering |
| **Configuration** | python-dotenv |
| **Version Control** | Git, GitHub |

---

## 📂 Project Structure

```text
ai-chatbot-prompt-engineering/
│
├── app.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── chatbot/
│   ├── __init__.py
│   ├── chatbot.py
│   └── memory.py
│
└── config/
    ├── __init__.py
    ├── prompts.py
    └── personas.py
```

### File Responsibilities

| File | Description |
|---|---|
| `app.py` | Streamlit UI, persona selection, chat interface, and response streaming |
| `chatbot/chatbot.py` | Gemini API integration, persona prompts, memory, streaming, and error handling |
| `chatbot/memory.py` | Conversation history management |
| `config/prompts.py` | System prompts for the three personas |
| `config/personas.py` | Persona names, icons, and UI descriptions |
| `.env.example` | Example environment variable configuration |
| `.gitignore` | Prevents sensitive and unnecessary files from being committed |

> The actual `.env` file is intentionally excluded from the repository because it contains the Gemini API key.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/abhinaymeshram01/ai-chatbot-prompt-engineering.git
```

Navigate into the project:

```bash
cd ai-chatbot-prompt-engineering
```

---

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

The application loads the API key using `python-dotenv`.

**Never commit your `.env` file to GitHub.**

The repository includes `.env.example` as a template:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

After starting the application, Streamlit will provide a local URL in the terminal.

Open the URL in your browser to use the chatbot.

---

## 🖥️ Application Preview

The application provides:

- 🎭 Persona selector
- 📝 Persona description
- 💬 Interactive chat interface
- ⚡ Streaming responses
- 🧹 Clear Chat functionality
- 🧠 Context-aware conversations

### Available Personas

| Persona | Description |
|---|---|
| 👨‍💻 **Coding Tutor** | Helps users learn programming and debug code |
| 🤝 **Friendly Assistant** | Provides helpful and approachable responses |
| 😏 **Sarcastic Buddy** | Provides helpful responses with light sarcasm |

---

## 🔄 Persona Switching

When the user changes the selected persona:

```text
Current Conversation
        ↓
Persona Changed
        ↓
Conversation History Cleared
        ↓
Backend Memory Cleared
        ↓
New Persona
        ↓
Fresh Conversation
```

This prevents the previous persona's conversation from affecting the new persona.

---

## 🧠 Prompt Flow

The chatbot uses a different system prompt depending on the selected persona.

```text
                User Selects Persona
                        ↓
                   Persona Key
                        ↓
                  System Prompt
                        ↓
              Conversation History
                        ↓
                   Gemini API
                        ↓
                Generated Response
```

This allows the same underlying Gemini model to behave differently based on the selected persona.

---

## 🎯 What I Learned

Through this project, I practiced:

- Working with LLM APIs
- Google Gemini API integration
- System prompts
- Prompt engineering
- Persona-based prompting
- Conversation state management
- Context-aware conversations
- Python generators
- Streaming API responses
- Streamlit session state
- Streamlit chat components
- API error handling
- Environment variable management
- Modular Python architecture

---

## 🚀 Future Improvements

Potential future improvements include:

- Conversation export
- Persistent conversation storage
- Token-aware context management
- Authentication
- Multiple LLM providers
- File-based conversations
- Advanced prompt evaluation
- Automated testing
- Docker deployment
- Cloud deployment

---

## 📌 Project Status

**Completed and Deployed 🚀**

The application is deployed using Streamlit and available as a live web application.

👉 **[Launch AI Persona Assistant](https://ai-chatbot-prompt-engineering.streamlit.app/)**

This project demonstrates the fundamentals of building a conversational Generative AI application using an LLM API, prompt engineering, memory management, streaming responses, and a web-based interface.

---

## 👨‍💻 Author

**Abhinay Meshram**

Built with:

**Python • Google Gemini • Streamlit • Prompt Engineering • Generative AI**
