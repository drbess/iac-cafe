terraform {
  required_providers {
    linode = {
      source  = "linode/linode"
      version = "2.5.2"
    }
  }
}

provider "linode" {
  token = var.api_token
}

resource "linode_instance" "rycm-dev" {
  label           = "rycm-dev-instance"
  image           = "linode/fedora41"
  region          = "us-east"
  type            = "g6-standard-1" # Look up type
  authorized_keys = var.authorized_keys
  root_pass       = var.root_password

}