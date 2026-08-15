import streamlit as st
from chatbot.chatbot import generate_content_stream, clear_memory
from config.personas import PERSONA_INFO

st.set_page_config(
    page_title="AI Persona Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>

    /* Main container */
    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Main title */
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }

    .subtitle {
        text-align: center;
        color: #888888;
        margin-bottom: 2rem;
    }

    /* Persona card */
    .persona-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        margin-top: 0.8rem;
        margin-bottom: 1rem;
    }

    .persona-name {
        font-size: 1.15rem;
        font-weight: 600;
        margin-bottom: 0.3rem;
    }

    .persona-description {
        color: #888888;
        font-size: 0.9rem;
    }models

    /* Sidebar */
    section[data-testid="stSidebar"] {
        padding-top: 1.5rem;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 8px;
    }

    /* Chat spacing */
    .stChatMessage {
        margin-bottom: 0.5rem;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #888888;
        font-size: 0.8rem;
        margin-top: 2rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "persona" not in st.session_state:
    st.session_state.persona = "coding_tutor"

st.markdown(
    '<div class="main-title">🤖 AI Persona Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'One AI. Three personalities. Choose how you want to interact.'
    '</div>',
    unsafe_allow_html=True
)

with st.sidebar:

    st.header("🎭 Persona")

    persona_keys = list(PERSONA_INFO.keys())

    selected_persona = st.selectbox(
        "Choose how the AI should behave",
        persona_keys,
        index=persona_keys.index(st.session_state.persona),
        format_func=lambda key: (
            f"{PERSONA_INFO[key]['icon']} "
            f"{PERSONA_INFO[key]['name']}"
        )
    )

    # Persona information
    persona_data = PERSONA_INFO[selected_persona]

    st.markdown(
        f"""
        <div class="persona-card">
            <div class="persona-name">
                {persona_data['icon']} {persona_data['name']}
            </div>
            <div class="persona-description">
                {persona_data['description']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # Clear chat
    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        clear_memory()

        st.rerun()

    st.divider()

    st.caption("Powered by Google Gemini")
    st.caption("Built with Python + Streamlit")

if selected_persona != st.session_state.persona:

    st.session_state.messages = []

    clear_memory()

    st.session_state.persona = selected_persona

    st.rerun()

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])

user_input = st.chat_input(
    "Ask me something..."
)

if user_input and user_input.strip():

    user_input = user_input.strip()

    # Add user message to UI history
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Display user message
    with st.chat_message("user"):

        st.write(user_input)

    # Display streaming assistant response
    with st.chat_message("assistant"):

        response = st.write_stream(
            generate_content_stream(
                user_input,
                selected_persona
            )
        )

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

st.markdown(
    """
    <div class="footer">
        AI Persona Assistant • Gemini • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)