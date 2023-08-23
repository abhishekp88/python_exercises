import requests
from datetime import datetime
USERNAME = 'abhipalo'
TOKEN = 'q1w2e3r4t5y6'
pixela_endpoint = "https://pixe.la/v1/users"
req_body = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}



# for user creation
# create_user = requests.post(url=pixela_endpoint, json=req_body)
# print(create_user.text)

# graph creation
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = 'graph1'
# graph_req = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "momiji"
# }
headers = {
    "X-USER-TOKEN": TOKEN
}
# create_graph = requests.post(url=graph_endpoint, json=graph_req, headers=headers)
# print(create_graph.text)


# post pixel on graph
#
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
#
today_date = datetime(2023,8,22)
#
# post_pixel_req = {
#     "date": today_date.strftime("%Y%m%d"),
#     "quantity": "130.5"
# }
# create_pixel = requests.post(url=post_pixel_endpoint, json=post_pixel_req, headers=headers)
# print(create_pixel.text)



# put and delete  entry
d = today_date.strftime("%Y%m%d")
put_pixel_endpoint = f"{post_pixel_endpoint}/{d}"
update_req = {
    "quantity": "30.2"
}
update_pixel = requests.put(put_pixel_endpoint, json=update_req, headers=headers)
print(update_pixel.text)

# delete pixel

delete_pixel = requests.delete(put_pixel_endpoint, headers=headers)
print(delete_pixel.text)
