
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
# region = PureCloudPlatformClientV2.PureCloudRegionHosts.us_west_2
# PureCloudPlatformClientV2.configuration.host = region.get_api_host()

PureCloudPlatformClientV2.configuration.access_token = 'OEkm4UNTdlH6V4_aL83DczQ4dZcnY6L2uMLPHrQsO3WrFG7u1gl29LMK0hmeDmYYUtPtL_mU6t-FvpsN3b4C4w'
# or use get_client_credentials_token(...), get_saml2bearer_token(...) or get_code_authorization_token(...)

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuditApi();
body = PureCloudPlatformClientV2.AuditQueryRequest() # AuditQueryRequest | query

try:
    # Create audit query execution
    api_response = api_instance.post_audits_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->post_audits_query: %s\n" % e)