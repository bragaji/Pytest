import json

import requests
import pytest

BASE_URL="https://reqres.in/api"

def test_get_users():
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200
    assert response.json()["page"]==2
    result = json.dumps(response.json(), indent=4)
    print(result)