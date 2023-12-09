from dotenv import load_dotenv
import os
import httpx

load_dotenv()

TOKEN = "https://oauth-sandbox.rabobank.nl/openapi/sandbox/oauth2-premium/token"
AUTH = "https://oauth-sandbox.rabobank.nl/openapi/sandbox/oauth2-premium/authorize"


params = {
    "client_id": os.environ["CLIENT_ID"],
    "scope": "ais.balances.read",
    "response_type": "code",
}

with open("cert.pem", "rb") as cert_file:
    cert = cert_file.read()

r = httpx.get(AUTH, params=params, cert=cert)

print(vars(r))
