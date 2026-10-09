from enum import Enum
from datetime import datetime, timezone

class TodoStatus(Enum):
    INBOX = "inbox"
    IN_PROGRESS = "in_progress"
    WAITING = "waiting"
    DEFERRED = "deferred"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Todo:
    def __init__(self, title, description="", status=TodoStatus.INBOX, priority=Priority.MEDIUM, due_at=None, next_attention_at=None, todo_id=None ):
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        title = title.strip()

        if not title:
            raise ValueError("title cannot be empty")

        if not isinstance(status, TodoStatus):
            raise TypeError("status must be a TodoStatus")

        if not isinstance(priority, Priority):
            raise TypeError("priority must be a Priority")

        if due_at is not None and not isinstance(due_at, datetime):
            raise TypeError("due_at must be a datetime or None")

        if (
            next_attention_at is not None
            and not isinstance(next_attention_at, datetime)
        ):
            raise TypeError(
                "next_attention_at must be a datetime or None"
            )
    
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.created_at = datetime.now(timezone.utc)
        self.next_attention_at = next_attention_at
        self.due_at = due_at
        self.todo_id = todo_id