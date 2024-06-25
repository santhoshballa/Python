import requests
import base64
import time

client_id = "672367d5-fa5b-4c8e-a3b9-7b8d74291fa3"
client_secret = "GMpUk_EXRH0NUFHlzT7g4inVhULCmk-Y-AOOn9YTky4"
environment = "usw2.pure.cloud"
base_url = "https://api.usw2.pure.cloud"
auth_url = f"https://login.{environment}/oauth/token"
data = dict(grant_type="client_credentials")

# Encode client ID and client secret using base64
auth_string = f"{client_id}:{client_secret}".encode("utf-8")
base64_encoded_auth_string = base64.b64encode(auth_string).decode("utf-8")

headers = {
    "Authorization": f"Basic {base64_encoded_auth_string}",
    "Content-Type": "application/x-www-form-urlencoded",
}


response = requests.post(auth_url,headers=headers, data=data)
if response.status_code == 200:
    response_data = response.json()
    access_token = response_data["access_token"]
    print(access_token)


# access_token = "Xmu1cqw73HaV5Ek0Znn40RpzSYEAjuYGZJ4rqWSIJwFuLjar6rOP2Q8_YV_iKruh47IxFJZBgTStMTPUQybM0w"
api_url = "https://api.usw2.pure.cloud/api/v2/audits/query"
data = {"interval": "2023-10-01T00:00:00Z/2023-10-30T00:00:00Z", "serviceName": "PeoplePermissions"}

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

response = requests.post(api_url, headers=headers, json=data)
jsonResponse = response.json()
id = jsonResponse['id']
print(id)

if response.status_code == 202:
    print(response.json())
else:
    print(response.json())
    print(f"Error: {response.status_code}")

time.sleep(5)
api_url_status = f"{base_url}/api/v2/audits/query/{id}"
print(api_url_status)
response = requests.get(api_url_status, headers=headers)
jsonResponse = response.json()
print(jsonResponse)
state = jsonResponse['state']
print(state)

api_url_result = f"{base_url}/api/v2/audits/query/{id}/results"
print(api_url_result)

if state == "Succeeded":
    response = requests.get(api_url_result, headers=headers)
    jsonResponse = response.json()
    print(jsonResponse)
    with open("response.txt", "w") as f:
        # Write your data to the file
        jsonResponseStr = str(jsonResponse)
        f.write(jsonResponseStr)
    f.close()


