import requests
from .constants import ENDPOINTS

class Refir:
    def __init__(self):
        self.api_key = None

    def configure(self, options):
        self.api_key = options.get("api_key")

    def add_user(self, user):
        if not self.api_key:
            raise ValueError("Please configure the apiKey first.")

        if not all(k in user for k in ("userId", "name", "email")):
            raise ValueError("Please pass in a correct user object")

        try:
            response = requests.post(
                ENDPOINTS["WEBHOOK"],
                json={
                    "leadId": user["userId"],
                    "name": user["name"],
                    "email": user["email"],
                },
                headers={"x-api-key": self.api_key},
            )

            if response.json().get("status"):
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def get_user_by_id(self, id):
        if not self.api_key:
            raise ValueError("Please configure the apiKey first.")
        if not id:
            raise ValueError("Please pass the userId")

        try:
            response = requests.get(
                f"{ENDPOINTS['GET_LEAD']}{id}",
                headers={"x-api-key": self.api_key},
            )

            if response.json().get("status"):
                return response.json().get("lead", {}).get("referralCode")
            else:
                return False
        except Exception as e:
            print(e)
            return False
