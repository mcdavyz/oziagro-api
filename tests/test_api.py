from fastapi.testclient import TestClient

from app.api.server import app

client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Welcome to OziAgro DSS!"
    }


def test_sample_analysis():

    response = client.get("/analyze/sample")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    assert len(data) > 0


def test_missing_upload():

    response = client.post("/analyze")

    assert response.status_code == 422


def test_invalid_file():

    response = client.post(
        "/analyze",
        files={
            "file": (
                "notes.txt",
                b"Hello World",
                "text/plain"
            )
        }
    )

    assert response.status_code == 200

    assert "error" in response.json()

def test_upload_real_excel():

    with open("data/raw/bende_daily_rainfall.xlsx", "rb") as f:

        response = client.post(
            "/analyze",
            files={
                "file": (
                    "bende_daily_rainfall.xlsx",
                    f,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            }
        )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["records"] > 0
    assert len(data["results"]) > 0