from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class AnswerRequest(BaseModel):
    answer: str


@router.get("/question")
def get_question():
    """
    Return your assigned question.
    """
    pass


@router.post("/answer")
def post_answer(request: AnswerRequest):
    """
    Validate the supplied answer and return:
    {
        "correct": bool,
        "message": str
    }
    """
    pass
