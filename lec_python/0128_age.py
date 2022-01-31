import requests



# 1. URL
#URL = 'https://api.agify.io?name=michael'
URL = 'https://api.agify.io'
params = {
    'name' : 'michael',
    'name1' : 'eric'
}
# 2. 요청
# JSON이므로 굳이 beautiful 쓸 필요가 없다.
response = requests.get(URL, params = params).json()
print(response)
print(response.get('age'))