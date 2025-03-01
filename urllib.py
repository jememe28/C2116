import requests

response = requests.post("https://httpbin.org/post")
data = "test data"
headers = {"hi": "Test title"}
print(response.text)    