import requests
import json


class ApiPage:
    def __init__(self):
        self.url = "https://petstore.swagger.io/v2/pet"
        self.headers = {
            'Content-Type': 'application/json',
        }

    def add_new_pet_with_api(self, pet_id, name):
        data = json.dumps({
            "id": pet_id,
            "category": {
              "id": 0,
              "name": "string"
            },
            "name": name,
            "photoUrls": [
              "string"
            ],
            "tags": [
              {
                "id": 0,
                "name": "string"
              }
            ],
            "status": "available"
          })
        resp = requests.request("POST", url=self.url, data=data, headers=self.headers)
        assert resp.status_code == 200

    def check_new_pet_with_api(self, pet_id):
        new_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        url = self.url + f"/{pet_id}"
        resp = requests.request("GET", url=url, headers=new_headers)
        count = 0
        while resp.status_code != 200 and count != 10:
            resp = requests.request("GET", url=url, headers=new_headers)
            count += 1
        return resp.json()

    def update_pet_with_api(self, pet_id, new_name):
        data = json.dumps({
            "id": pet_id,
            "category": {
              "id": 0,
              "name": "string"
            },
            "name": new_name,
            "photoUrls": [
              "string"
            ],
            "tags": [
              {
                "id": 0,
                "name": "string"
              }
            ],
            "status": "available"
          })
        resp = requests.request("PUT", url=self.url, data=data, headers=self.headers)
        return resp.json()

    def check_new_pet_after_update(self, pet_id, new_name):
        new_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        url = self.url + f"/{pet_id}"
        resp = requests.request("GET", url=url, headers=new_headers)
        count = 0
        while resp.json().get('name') != new_name and count != 10:
            resp = requests.request("GET", url=url, headers=new_headers)
            count += 1
        return resp.json()
