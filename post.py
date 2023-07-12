
import requests

req = requests.post(
    url='http://localhost:8083/user/add',
    data={
        'name':'jo',
        'age':'30'
        })
print(req.text)
