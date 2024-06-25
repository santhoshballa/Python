import requests
import base64
import time

def get_token (client_id, client_sccret, environment):
    auth_string = f"{client_id}:{client_secret}".encode("utf-8")
    base64_encoded_auth_string = base64.b64encode(auth_string).decode("utf-8")
    auth_url = f"https://login.{environment}/oauth/token"
    headers = {
        "Authorization": f"Basic {base64_encoded_auth_string}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = dict(grant_type="client_credentials")
    response = requests.post(auth_url, headers=headers, data=data)
    if response.status_code == 200:
        response_data = response.json()
        access_token = response_data["access_token"]
        print(access_token)
        return str(access_token)
    
def post_audit_query (environment, access_token, data):
    api_url = f"https://api.{environment}/api/v2/audits/query"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 202:
        jsonResponse = response.json()
        id = jsonResponse['id']
        print(id)
        assert isinstance(id, object)
        return str(id)

def get_audit_query_status(environment, access_token, id):
    api_url_status = f"https://api.{environment}/api/v2/audits/query/{id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    print(api_url_status)
    response = requests.get(api_url_status, headers=headers)
    if response.status_code == 200:
        jsonResponse = response.json()
        print(jsonResponse)
        state = jsonResponse['state']
        print(state)
        return str(state)

def get_audit_query_result(environment, access_token, id, state):
    api_url_result = f"https://api.{environment}/api/v2/audits/query/{id}/results"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    if state == "Succeeded":
        response = requests.get(api_url_result, headers=headers)
        jsonResponse = response.json()
        print(jsonResponse)
        return str(jsonResponse)

def create_result_output_to_file(filename, result):
    with open(filename, "w") as f:
        # Write your data to the file
        f.write(result)
    f.close()


if __name__ == '__main__':
    client_id = "123456-34567-4c8e-a3b9-7b445574291fa3"
    client_secret = "1234564rft7g4inVhULCmk-Y-A4455n9YTky4"
    environment = "usw2.pure.cloud"
    data = {"interval": "2023-10-01T00:00:00Z/2023-10-30T00:00:00Z", "serviceName": "PeoplePermissions"}
    access_token = get_token(client_id, client_secret, environment)
    print(access_token)
    id = post_audit_query(environment, access_token, data)
    print(id)
    time.sleep(10)
    state = get_audit_query_status(environment, access_token,id)
    print(state)
    result = get_audit_query_result(environment, access_token, id, state)
    print(result)
    filename = "output/OutputAuditResult.txt"
    create_result_output_to_file(filename, result)



