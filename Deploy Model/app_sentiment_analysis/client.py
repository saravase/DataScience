#curl -XPOST http://localhost:5000/api -H 'Content-Type: application/json' -d @test_data.json

import requests

url= "http://localhost:5000/api"
request = requests.post(url, json={"x": ["I love juice"]})
print(request.json())