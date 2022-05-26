import requests
from datetime import datetime

pixel_endpoint = "https://pixe.la/v1/users"
user_name = "arunkrish"
token = "kquiduhuiqlh923e89312"
graph_id = "graph007"
headers = {
    "X-USER-TOKEN": token
}

user_param = {
    "token":"kquiduhuiqlh923e89312",
    "username":"arunkrish",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixel_endpoint,json=user_param)
# print(response.text)

graph_endpoint = f"{pixel_endpoint}/{user_name}/graphs"
graph_config = {
    "id": graph_id,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixel_endpoint}/{user_name}/graphs/{graph_id}"
today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

"""To update the update pixela"""
# update_endpoint = f"{pixel_endpoint}/{user_name}/graphs/{graph_id}/20220525"
# new_pixel_data = {
#     "quantity": "16.5"
# }
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


"""To delete the posted pixela"""
# delete_endpoint = f"{pixel_endpoint}/{user_name}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)



