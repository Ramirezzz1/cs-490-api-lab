from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class AnswerRequest(BaseModel):
    answer: str


@router.get("/question")
def get_question():
    pass


@router.post("/answer")
def post_answer(request: AnswerRequest):
    pass
