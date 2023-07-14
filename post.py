
import requests

req = requests.post(
    url='http://localhost:8083/api/post',
    data={
        'name':'jo',
        'age':'30'
        })
print(req.text)
