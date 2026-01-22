import requests

url = "http://127.0.0.1:5000/predict"
files = {"image": open("test_img.jpg", "rb")}

response = requests.post(url, files=files)
print("MODEL OUTPUT:")
print(response.json())
