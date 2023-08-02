from fastapi.testclient import TestClient
from sql_app.main import app

client = TestClient(app)

token = ""  # 실제 사용할 토큰
headers = {"Authorization": f"Bearer {token}"}

def test_read_root():
    response = client.get("/")
    print(response.status_code)
    assert response.status_code == 200
    # 응답 내용이 정확한지 확인하는 추가 로직이 필요할 수 있습니다.

def test_read_users():
    response = client.get("/users/", headers=headers)
    assert response.status_code == 200
    response = client.get("/users/susong")
    assert response.status_code == 200
    # 응답 내용이 정확한지 확인하는 추가 로직이 필요할 수 있습니다.

def test_make_user():
    response = client.post("/users/", headers=headers,json={"name": "test2", "email": "asd@naver.com"})
    assert response.status_code == 401
    response = client.post("/users/", json={"name": "test2", "email": "asd@naver.com"})
    assert response.status_code == 401

def test_get_user_list():
    response = client.get("/users/", headers=headers)
    assert response.status_code == 200
    assert response.json()[0]["name"] == "susong"
    assert response.json()[1]["name"] == "test"
    assert response.json()[2]["name"] == "test2"
