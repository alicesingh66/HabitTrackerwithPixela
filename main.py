import datetime
import requests



#CREATING_A_NEW_USER
userParam = {
    'token': "rfguyhecgbofggrfuy",
    'username' : 'alice6666666',
    'agreeTermsOfService' : 'yes',
    'notMinor':'yes'
}
# response = requests.post(url="https://pixe.la/v1/users", json=userParam)
# print(response.text)
PIXELAend = "https://pixe.la/v1/users"
TOKEN = "rfguyhecgbofggrfuy"
USER_NAME = 'alice6666666'
graphEndpoint = f'{PIXELAend}/{USER_NAME}/graphs'




#ADDING GRAPH
graph_params = {
    'id': "graph01",
    'name': "Walking",
    'unit': "Km",
    'type': "float",
    'color': "sora"
}
header = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graphEndpoint, json=graph_params, headers=header)
# print(response)

#ADD_NEW_PIXEL_TO_A_DATE
TODAY = datetime.date.today().strftime("%Y%m%d")
print(TODAY)
QUANTITY = 5.8
GRAPH_ID = 'graph01'
NEW_PIXEL_ADD_END = f"{PIXELAend}/{USER_NAME}/graphs/{GRAPH_ID}"
PARAM_PIXEL = {
    "date": f"{TODAY}",
    "quantity": f"{QUANTITY}"
}
# response = requests.post(url=PIXEL_END,json=PARAM_PIXEL,headers=header)
# print(response)



#MODIFY_DATA
DATE = "20231001" #day wished to be updated
NEW_DATA = 3.1
UPDATE_END = f"{PIXELAend}/{USER_NAME}/graphs/{GRAPH_ID}/{DATE}"
UPDATE_PARAMS = {
    "quantity": f"{NEW_DATA}"
}
# response = requests.put(url=UPDATE_END,json=UPDATE_PARAMS,headers=header)
# print(response.text)


#DELETE_PIXEL
DATE_TO_DELETE = "20231001"
DELETE_ENDPOINT = f"{PIXELAend}/{USER_NAME}/graphs/{GRAPH_ID}/{DATE_TO_DELETE}"
response = requests.delete(url=DELETE_ENDPOINT,headers=header)
print(response.text)