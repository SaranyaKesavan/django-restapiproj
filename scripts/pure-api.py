# this file and its folder can be outside django project also 
# i'm keeping it inside my django project for github purpose

import requests # third party python library that allows to do http requests

BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"

def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    data = r.json()
    print(r.headers)
    print(r.status_code)
    for obj in data:
        if obj['id'] == 1:
            r = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            print(r.json())
    return data


#print(get_list()) 


def create_update():
    new_data = {
        'user' : 3,
        'content' : "Trying to find the serialize error!!"
    }
    r = requests.post(BASE_URL + ENDPOINT + "1", data=new_data)
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        #print(r.json())
        return r.json()
    return r.text

print(create_update())

def delete_update():
    new_data = {
        'user' : 3,
        'content' : "Testing api with python requests"
    }
    r = requests.delete(BASE_URL + ENDPOINT, data=new_data)
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        #print(r.json())
        return r.json()
    return r.text

#print(delete_update())