import base64
import requests

def post_audit_transactionid(client_id, client_secret, environment):
    # Replace with your Genesys Cloud environment
    # For example, mypurecloud.com
    # auth_url = f"https://login.{environment}/oauth/token"
    auth_url = "https://api.usw2.pure.cloud/api/v2/audits/query"
    print(auth_url)

    # Encode client ID and client secret using base64
    auth_string = f"{client_id}:{client_secret}".encode("utf-8")
    base64_encoded_auth_string = base64.b64encode(auth_string).decode("utf-8")

    response = requests.post(
        auth_url,
        headers={
            "Authorization": "Bearer Xmu1cqw73HaV5Ek0Znn40RpzSYEAjuYGZJ4rqWSIJwFuLjar6rOP2Q8_YV_iKruh47IxFJZBgTStMTPUQybM0w",
            "Content-Type": "application/json",
        },
        data={
            "interval": "2023-10-01T00:00:00Z/2023-10-30T00:00:00Z",
            "serviceName": "PeoplePermissions"
        },
    )

    if response.status_code == 400:
        response_data = response.json()
        print(response_data)
        #id = response_data["id"]
        # access_token = response_data["access_token"]
        # return id
    else:
        raise Exception(f"Failed to obtain access token: {response.status_code}")


# Example usage
if __name__ == '__main__':
    client_id = "672367d5-fa5b-4c8e-a3b9-7b8d74291fa3"
    client_secret = "GMpUk_EXRH0NUFHlzT7g4inVhULCmk-Y-AOOn9YTky4"
    environment = "usw2.pure.cloud"
    # access_token = post_audit_transactionid(client_id, client_secret, environment)
    id = post_audit_transactionid(client_id, client_secret, environment)
    print(id)