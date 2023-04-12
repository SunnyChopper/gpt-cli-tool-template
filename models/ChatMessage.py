from typing import Dict

class ChatMessage:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

    @staticmethod
    def from_dict(raw_message: Dict) -> "ChatMessage":
        return ChatMessage(
            role = raw_message["role"],
            content = raw_message["content"]
        )

    def to_dict(self) -> Dict:
        return {
            "role": self.role,
            "content": self.content
        }