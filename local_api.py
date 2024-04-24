import json
import requests

# TODO: send a GET using the URL http://127.0.0.1:8000
# @app.get("http://127.0.0.1:8000")
# or??
# client = TestClient(app)
# replace requests with client if below doesn't work
# r = requests.get("http://127.0.0.1:8000")

# TODO: print the status code
# print(r.status_code)
# TODO: print the welcome message
# print(r.json()["message"])


data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# TODO: send a POST using the data above
# @app.post(data)
# r = # Your code here

# TODO: print the status code
# print()
# TODO: print the result
# print()
