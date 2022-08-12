import requests 

endpoint = "https://httpbin.org/STATUS/200"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json ={"query":"hello sinan"}) #Http Request 
print(get_response.text) #print raw text response


#HTTP Request ->html
# Rest API HTML REQUEST -> JSON
# javascript Object Notation ~ Python Dict
print(get_response.json())
print(get_response.status_code)