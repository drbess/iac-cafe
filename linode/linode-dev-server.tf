terraform {
  required_providers {
    linode = {
      source  = "linode/linode"
      version = "2.5.2"
    }
  }
}

provider "linode" {
  token = var.token
}

resource "linode_instance" "web" {
  label           = "simple_instance"
  image           = "linode/ubuntu22.04"
  region          = "us-east"
  type            = "g6-standard-1"
  authorized_keys = var.authorized_keys
  root_pass       = var.root_password

}