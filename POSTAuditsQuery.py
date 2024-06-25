import requests

def post_audits_query():
    # Genesys Cloud API URL
    api_url = "https://api.usw2.pure.cloud/api/v2/audits/query"

    # Set authorization header with access token
    access_token = "qt7Fm4RQ5xxfJD-Qx6m7qb-suxl9rnHCJoL1xrCFipCFKhuf_FUt1vIDJEfNiItNDN_VTpzqwu3dg1cswcDlig"
    headers = {
        "Authorization": f"Basic {access_token}",
        "Content-Type": "application/json",
    }
    payload = {"interval": "2023-10-01T00:00:00Z/2023-10-30T00:00:00Z","serviceName": "PeoplePermissions"}

    # Send POST request to Genesys Cloud Audits API
    response = requests.post(api_url, headers=headers, data=payload)
    print(response)

    if response.status_code == 200:
        # Parse JSON response and extract audit query execution status
        response_data = response.json()
        return response_data
    else:
        raise Exception(f"Failed to post audit query: {response.status_code}")