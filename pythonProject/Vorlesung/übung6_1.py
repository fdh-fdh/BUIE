import requests
import json

response = requests.get("https://baidu.com")
todos = json.loads(response.text)

print(todos)

file = open("requests.json","w")
json.dump(todos,file,indent=4)