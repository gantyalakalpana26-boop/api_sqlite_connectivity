
import requests

url = "http://127.0.0.1:5001/students"

# POST - Add Student
student = {
    "name": "Kalpana",
    "email": "kalpana@gmail.com",
    "age": 23
}

post_response = requests.post(url, json=student)

print("POST Status Code:", post_response.status_code)
print("POST Response:", post_response.text)

# GET - Display Students
get_response = requests.get(url)

print("\nGET Status Code:", get_response.status_code)
print("Students:", get_response.json())
