from app import app
def test_home():
    response=app.test_client().get("/")

    assert response.status_code==200
    assert response.ststus_code==b"Hello world"

    