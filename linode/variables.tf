
variable "token" {
  type        = string
  description = "API token for authentication"
  sensitive   = true
}

# Make sure this block contains type = list(string)""
variable "authorized_keys" {
  type        = list(string)
  description = "List of SSH public keys for authorized access"
  sensitive   = true
}


variable "root_password" {
  type        = string
  description = "root password for the system"
  sensitive   = true
}

# variable "ssh_public_key" {
#   type        = string
#   description = "SSH public key for remote access"
# }