from models.ChatCompletionChoice import ChatCompletionChoice
from models.ChatUsage import ChatUsage
from typing import List, Dict

class ChatCompletion:
    def __init__(self, choices: List[ChatCompletionChoice], created: int, completion_id: str, model: str, completion_object: str, usage: ChatUsage):
        self.choices = choices
        self.created = created
        self.completion_id = completion_id
        self.model = model
        self.completion_object = completion_object
        self.usage = usage

    @property
    def total_tokens(self) -> int:
        return self.usage.total_tokens
    
    @staticmethod
    def from_dict(raw_completion: Dict) -> "ChatCompletion":
        return ChatCompletion(
            choices = [ChatCompletionChoice.from_dict(choice) for choice in raw_completion["choices"]],
            created = raw_completion["created"],
            completion_id = raw_completion["id"],
            model = raw_completion["model"],
            completion_object = raw_completion["object"],
            usage = ChatUsage.from_dict(raw_completion["usage"])
        )

    def to_dict(self) -> Dict:
        return {
            "choices": [choice.to_dict() for choice in self.choices],
            "created": self.created,
            "id": self.completion_id,
            "model": self.model,
            "object": self.completion_object,
            "usage": self.usage.to_dict()
        }
