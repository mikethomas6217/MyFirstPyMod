'''
Created on Jun 30, 2017

@author: MikeT
'''
import json, requests
print ("Returning ISS Location")

parameters = {"lat": 40.71, "lon": -74}
response = requests.get("http://api.open-notify.org/iss-now.json?lat=40.71&lon=-74")
print(response.content)
response = requests.get("http://api.open-notify.org/iss-now.json", params=parameters)
print(response.content)
data = json.loads(response.text)
print(data['iss_position']['latitude'])
# iterating though JSON 
json_data = open("MikeJson.json").read()
data = json.loads(json_data)
print(data)
for i in data:
    print (i)

#for value in json_data['response']['groups']
def traverse(obj):
    if isinstance(obj, dict):
        for key, value in obj.iteritems():
            print('dict_key', key)
            traverse(value)
    elif isinstance(obj, list):
        for value in obj:
            traverse(value)
    else:
        print('value', obj)

traverse(data)

