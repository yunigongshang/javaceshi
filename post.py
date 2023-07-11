
import requests

req = requests.post(
    url='http://localhost:8084/ent',
    data={
        'name':'jo',
        'age':'30'
        })
print(req.text)
