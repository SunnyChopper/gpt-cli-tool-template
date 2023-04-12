# System Libraries
import os

# External Libraries
from dotenv import load_dotenv
import openai

# Models
from models.Chat import Chat

# Constants
from constants.models import GPT_TURBO
from init import START_PROMPT

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY", "")

if __name__ == "__main__":
    chat: Chat = Chat(model = GPT_TURBO, messages = START_PROMPT)
    chat.print_chat()

    latest_user_message: str = ""

    while latest_user_message.lower() != "exit":
        # 1 - Getting user input
        prompt_user_message: str = input("You: ")
        latest_user_message: str = prompt_user_message.replace("You: ", "")
        chat.add_user_message(latest_user_message)

        # 2 - Getting AI response
        ai_message: str = chat.get_chat_response()
        chat.add_ai_message(message = ai_message)

        # 3 - Printing latest message
        chat.print_latest_message()
        chat.print_total_tokens()
    
    print("Exiting chat...")
