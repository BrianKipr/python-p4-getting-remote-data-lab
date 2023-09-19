import json
import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)
            return response.text
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch data from {self.url}: {e}")

    def load_json(self):
        response_body = self.get_response_body()
        try:
            return json.loads(response_body)  # Parse JSON data from the response
        except ValueError as e:
            raise Exception(f"Failed to parse JSON data from {self.url}: {e}")

# You can test your GetRequester class using the provided URL
if __name__ == "__main__":
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(url)
    
    try:
        data = requester.load_json()
        print(data)  # This should print the JSON data
    except Exception as e:
        print(f"An error occurred: {e}")


