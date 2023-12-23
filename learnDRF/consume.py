import requests


url = 'http://127.0.0.1:8000/drinks'
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAzMjkxODEwLCJpYXQiOjE3MDMyODg4MTAsImp0aSI6ImFhNzViNTRiMTg3OTQwZTg5M2Y1NjFkNGEzNzcyOTVmIiwidXNlcl9pZCI6MX0.eJ_K1XDkAZ2lKDjLvH2fcAJVW8c-vqE9bqEsYOh01NQ'
headers = {
    'Authorization': f'Bearer {token}'
}

response = requests.get(url, headers=headers)

print(response.text)