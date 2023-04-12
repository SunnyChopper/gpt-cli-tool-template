# System Libraries
from typing import List, Dict
import openai

# Models
from models.ChatCompletion import ChatCompletion
from models.ChatMessage import ChatMessage

# Constants
from constants.roles import AI, SYSTEM, USER

class Chat:
    def __init__(self, model: str, messages: List[ChatMessage]):
        self.model = model
        self.messages = messages
        self.token_count = 0

    def add_ai_message(self, message: str) -> None:
        new_message: ChatMessage = ChatMessage(role = AI, content = message)
        self.messages.append(new_message)

    def add_system_message(self, message: str) -> None:
        new_message: ChatMessage = ChatMessage(role = SYSTEM, content = message)
        self.messages.append(new_message)

    def add_user_message(self, message: str) -> None:
        new_message: ChatMessage = ChatMessage(role = USER, content = message)
        self.messages.append(new_message)
    
    def get_chat_response(self) -> str:
        response: dict = openai.ChatCompletion.create(
            model = self.model,
            messages = [message.to_dict() for message in self.messages]
        )

        completion: ChatCompletion = ChatCompletion.from_dict(response)
        self.token_count += completion.total_tokens

        # NOTE: Will always only have one choice.
        return completion.choices[0].message.content
    
    def print_chat(self, include_system_message: bool = False) -> None:
        for message in self.messages:
            if message.role == SYSTEM and not include_system_message:
                continue

            print(f"{message.role.capitalize()}: {message.content}\n")

    def print_latest_message(self) -> None:
        latest_message: ChatMessage = self.messages[-1]
        print(f"{latest_message.role.capitalize()}: {latest_message.content}\n")
    
    def print_total_tokens(self) -> None:
        print(f"Total tokens used: {self.token_count}")
    
    def to_dict(self) -> Dict:
        return {
            "model": self.model,
            "messages": [message.to_dict() for message in self.messages]
        }