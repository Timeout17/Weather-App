from enum import Enum

class UserType(Enum):
    USER: str = "user"
    SYSTEM: str = "system"
    ASSISTANT = "assistant"