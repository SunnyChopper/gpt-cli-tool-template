from typing import Dict

class ChatUsage:
    def __init__(self, completion_tokens: int, prompt_tokens: int, total_tokens: int):
        self.completion_tokens = completion_tokens
        self.prompt_tokens = prompt_tokens
        self.total_tokens = total_tokens

    @staticmethod
    def from_dict(raw_usage: Dict) -> "ChatUsage":
        return ChatUsage(
            completion_tokens = raw_usage["completion_tokens"],
            prompt_tokens = raw_usage["prompt_tokens"],
            total_tokens = raw_usage["total_tokens"]
        )

    def to_dict(self) -> Dict:
        return {
            "completion_tokens": self.completion_tokens,
            "prompt_tokens": self.prompt_tokens,
            "total_tokens": self.total_tokens
        }