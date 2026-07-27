import requests


url = "https://reqres.in/api/users/2"

headers = {
    "x-api-key": "pub_8c7500a80eb7a97d20723541ccc8ff5696ff4b9037091ffebe9f5b46841fdd2f"
}


response = requests.get(
    url,
    headers=headers
)


print(response.status_code)
print(response.text)