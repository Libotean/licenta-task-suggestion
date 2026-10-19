from dataclasses import dataclass

@dataclass
class Task:
    id: str
    duration: float
    importance: float
    urgency: float
    effort: float
    context: str