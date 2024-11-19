import requests
from datetime import datetime


class HttpRequestHandler:
    def __init__(self, url):
        self.Url = url

    def getRequest(self):
        try:
            # Replace with your actual API URL
            headers = {
                "Authorization": "Bearer your_token",  # If authentication is required
                "Content-Type": "application/json"
            }
            response = requests.get(self.Url)
            #response.raise_for_status()  # Raise an error for bad status codes

            # Parse the JSON response
            data = response.json()
            return data

        except requests.exceptions.RequestException as e:
            # Handle exceptions such as connection errors or timeouts
            print(f"Error calling external API: {e}")
            with open("GeneralException.txt", "a") as f:
                current_datetime = datetime.now()
                f.write(f"{current_datetime}: Exception in getRequest() {self.Url}: {e}\n")
            raise Exception("Sorry, no numbers below zero")
