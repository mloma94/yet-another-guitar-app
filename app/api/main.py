import itertools
from typing import Dict
from uuid import uuid4

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.exercises.chord_practice import ChordPractice

app = FastAPI(title="Yet Another Guitar App")
app.mount("/static", StaticFiles(directory="app/static", html=True), name="static")

sessions: Dict[str, list[str]] = {}

@app.get("/")
def index():
    return FileResponse("app/static/index.html")

@app.post("/exercise/chord-practice/start")
def chord_practice_start():
    exercise = ChordPractice(difficulty=3)

    generator = exercise.generate_exercise()
    chords = [c.display_name() for c in itertools.islice(generator, 5)]

    session_id = str(uuid4())
    sessions[session_id] = chords
    
    return {"session_id": session_id}

@app.get("/exercise/chord-practice/{session_id}/next")
def chord_practice_next(session_id: str):
    chords = sessions.get(session_id)
    if not chords:
        return {"message": "Exercise complete"}

    return {"prompt": chords.pop(0)}