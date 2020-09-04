import requests
import json

response = requests.get("http://localhost:5000/todos")

print(response)

tasks = response.json()
print(tasks)
print("Número de tasks:", len(tasks))

response = requests.post(
    'http://localhost:5000/todos', 
    json = {'content':'Carol teimosa da maritaca!'})

task = response.json()
print(task)
