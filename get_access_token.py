import base64
import requests

def get_access_token(client_id, client_secret, environment):
    # Replace with your Genesys Cloud environment
    # For example, mypurecloud.com
    auth_url = f"https://login.{environment}/oauth/token"

    # Encode client ID and client secret using base64
    auth_string = f"{client_id}:{client_secret}".encode("utf-8")
    base64_encoded_auth_string = base64.b64encode(auth_string).decode("utf-8")

    response = requests.post(
        auth_url,
        headers={
            "Authorization": f"Basic {base64_encoded_auth_string}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "client_credentials",
        },
    )

    if response.status_code == 200:
        response_data = response.json()
        access_token = response_data["access_token"]
        return access_token
    else:
        raise Exception(f"Failed to obtain access token: {response.status_code}")


# Example usage
if __name__ == '__main__':
    client_id = "672367d5-fa5b-4c8e-a3b9-7b8d74291fa3"
    client_secret = "GMpUk_EXRH0NUFHlzT7g4inVhULCmk-Y-AOOn9YTky4"
    environment = "usw2.pure.cloud"
    access_token = get_access_token(client_id, client_secret, environment)
    print(access_token)