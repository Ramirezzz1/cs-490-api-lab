from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

QUESTION = "What's on the telly?"
QUESTION = "What have the Romans ever done for us?"
ANSWER = "I think it's a duck."
ANSWER = "The aqueducts?"


class AnswerRequest(BaseModel):
    answer: str


@router.get("/question")
def get_question():
    return {"question": QUESTION}


@router.post("/answer")
def post_answer(request: AnswerRequest):
    correct = request.answer.strip().lower() == ANSWER.strip().lower()

    return {
        "correct": correct,
        "message": "You may pass." if correct else "Into the Gorge of Eternal Peril!",
    }
