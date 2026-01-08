from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app import models, schemas
from app.external_api import analyze_sentiment

# IMPORTANT: import models BEFORE creating tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notes API")


# POST(Method) - Create Note
@app.post(
    "/notes",
    response_model=schemas.NoteResponse,
    status_code=status.HTTP_201_CREATED
)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    sentiment = analyze_sentiment(note.content)

    new_note = models.Note(
        title=note.title,
        content=note.content,
        sentiment=sentiment
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note

#GET(Method) - Fetch Note by ID
@app.get("/notes/{note_id}", response_model=schemas.NoteResponse)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()

    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )

    return note

#PUT(Method)- Update the  Note
@app.put("/notes/{note_id}", response_model=schemas.NoteResponse)
def update_note(
    note_id: int,
    note_data: schemas.NoteUpdate,
    db: Session = Depends(get_db)
):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()

    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )

    note.title = note_data.title
    note.content = note_data.content
    note.sentiment = analyze_sentiment(note_data.content)

    db.commit()
    db.refresh(note)

    return note

#Delete the note
@app.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()

    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )

    db.delete(note)
    db.commit()

    return None
