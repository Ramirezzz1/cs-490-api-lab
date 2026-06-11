from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

TEAMS = [
    "instructor",
]


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Bridge of Death API",
        "docs": "/docs",
    }


def test_question_endpoints_return_contract_shape():
    for team in TEAMS:
        response = client.get(f"/{team}/question")

        assert response.status_code == 200

        data = response.json()
        assert isinstance(data, dict)
        assert "question" in data
        assert isinstance(data["question"], str)
        assert data["question"].strip() != ""


def test_answer_endpoints_require_answer_field():
    for team in TEAMS:
        response = client.post(f"/{team}/answer", json={})

        assert response.status_code == 422


def test_answer_endpoints_return_contract_shape():
    for team in TEAMS:
        response = client.post(
            f"/{team}/answer",
            json={"answer": "wrong answer"},
        )

        assert response.status_code == 200

        data = response.json()
        assert isinstance(data, dict)
        assert "correct" in data
        assert "message" in data
        assert isinstance(data["correct"], bool)
        assert isinstance(data["message"], str)
        assert data["message"].strip() != ""
