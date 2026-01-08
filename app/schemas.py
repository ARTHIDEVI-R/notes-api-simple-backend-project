from pydantic import BaseModel
from datetime import datetime

# Request body for creating a note
class NoteCreate(BaseModel):
    title: str
    content: str

# Request body for updating a note
class NoteUpdate(BaseModel):
    title: str
    content: str

# Response schema
class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    sentiment: str
    created_at: datetime

    class Config:
        from_attributes = True
