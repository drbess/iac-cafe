import requests
from wrksp_token import get_terraform_cloud_token

# Retrieve the Terraform Cloud token from terraform_token.py
TERRAFORM_CLOUD_TOKEN = get_terraform_cloud_token(token='')
ORGANIZATION_NAME = "roycecom" # The 404 error came from a space in the organization name -__-

url = f"https://app.terraform.io/api/v2/organizations/{ORGANIZATION_NAME}/workspaces"

headers = {
    "Authorization": f"Bearer {TERRAFORM_CLOUD_TOKEN}",
    "Content-Type": "application/vnd.api+json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Token is valid. Workspaces:", response.json())
else:
    print(f"Failed to authenticate. Status code: {response.status_code}")
    print("Error:", response.json())
