import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from chatbot.memory import ConversationMemory
from config.prompts import CODING_TUTOR_PROMPT, FRIENDLY_ASSISTANT_PROMPT, SARCASTIC_BUDDY_PROMPT

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is not set. "
        "Please add your Gemini API key to the .env file."
    )

client = genai.Client(
    api_key=api_key
)

memory = ConversationMemory()

PERSONAS = {
    "coding_tutor": CODING_TUTOR_PROMPT,
    "friendly_assistant": FRIENDLY_ASSISTANT_PROMPT,
    "sarcastic_buddy": SARCASTIC_BUDDY_PROMPT
}

def generate_content_stream(prompt, persona):

    memory.add_user_message(prompt)
    history = memory.get_history()

    system_prompt = PERSONAS[persona]

    full_response = ""

    try:
        response_stream = client.models.generate_content_stream(
            model='models/gemini-3.5-flash-lite',
            contents=history,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt
            )
        )

        for chunk in response_stream:

            if chunk.text:
                full_response += chunk.text
                yield chunk.text
            
        if full_response:
            memory.add_assistant_message(full_response)
    
    except Exception as e:
        print(f'Gemini api error {e}')
        memory.remove_last_message()
        error_message = (
            "⚠️ Sorry, I couldn't generate a response right now. "
            "Please check your API connection and try again."
        )

        yield error_message

def clear_memory():
    memory.clear()