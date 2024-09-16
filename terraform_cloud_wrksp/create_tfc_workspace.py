import json
import requests
from wrksp_token import get_terraform_cloud_token


# TERRAFORM_CLOUD_TOKEN = get_terraform_cloud_token(token='')
ORGANIZATION_NAME = 'roycecom'
WORKSPACE_NAME = 'ryc_dev0'

# Terraform Cloud API URL
API_URL = f'https://app.terraform.io/api/v2/organizations/{ORGANIZATION_NAME}/workspaces'

# Headers for authentication and content type
headers = {
    'Authorization': f'Bearer {get_terraform_cloud_token}',
    'Content-Type': 'application/vnd.api+json'
}

# Data payload to create a workspace
data = {
    'data': {
        'type': 'workspaces',
        'attributes': {
            'name': WORKSPACE_NAME,
            'terraform_version': '>= 1.5.0',  # Specify the Terraform version
            'working-directory': '/rdev0'    # Specify the working directory if needed
        }
    }
}

# Make the POST request to create the workspace
response = requests.post(API_URL, headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 201:
    print(f"Workspace '{WORKSPACE_NAME}' created successfully.")
else:
    print(f"Failed to create workspace. Status code: {response.status_code}")
    print(f"Error: {response.json()}")