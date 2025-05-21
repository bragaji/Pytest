import json

import requests
import pytest

BASE_URL="https://reqres.in/api"
HEADERS = {
    "x-api-key": "reqres-free-v1"
}

def test_get_users():
    response = requests.get(f"{BASE_URL}/users?page=2",headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["page"]==2
    result = json.dumps(response.json(), indent=4)
    print(result)

def test_single_user():
    response =  requests.get(f"{BASE_URL}/users/2",headers=HEADERS)
    assert response.status_code ==200
    assert response.json()["data"]["first_name"]=="Janet"
    result = json.dumps(response.json(),indent=4)
    print(result)

def test_create_user():
    payload ={
    "name": "morpheus",
    "job": "leader"
}
    response= requests.post(f"{BASE_URL}/users",headers=HEADERS,json=payload)
    assert response.status_code == 201
    assert response.json()["name"]=="morpheus"
    result =json.dumps(response.json(),indent=4)
    print(result)

def test_update_user():
    payload ={
        "name": "Prashant",
    }
    response= requests.put(f"{BASE_URL}/users/2",headers=HEADERS,json=payload)
    assert response.status_code==200
    assert response.json()["name"]=="Prashant"
    result = json.dumps(response.json()["name"])
    print(result)

def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/2",headers=HEADERS)
    assert response.status_code==204


def test_login():
    payload = {

            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
    }
    response = requests.post(f"{BASE_URL}/login",headers=HEADERS,json=payload)
    assert response.status_code==200
    result = json.dumps(response.json()["token"])
    print(result)