from models.ChatMessage import ChatMessage
from typing import Dict

class ChatCompletionChoice:
    def __init__(self, finish_reason: str, index: int, message: ChatMessage):
        self.finish_reason = finish_reason
        self.index = index
        self.message = message

    @staticmethod
    def from_dict(raw_choice: Dict) -> "ChatCompletionChoice":
        return ChatCompletionChoice(
            finish_reason = raw_choice["finish_reason"],
            index = raw_choice["index"],
            message = ChatMessage.from_dict(raw_choice["message"])
        )

    def to_dict(self) -> Dict:
        return {
            "finish_reason": self.finish_reason,
            "index": self.index,
            "message": self.message.to_dict()
        }