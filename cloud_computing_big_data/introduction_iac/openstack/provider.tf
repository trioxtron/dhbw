terraform {
    required_version = ">= 0.12"
    required_providers {
        openstack = {
            source  = "terraform-provider-openstack/openstack"
            version = "~> 1.53.0"
        }
    }
}

provider "openstack" {
  user_name = local.openstack_host_user 
  auth_url = local.openstack_auth_url
  tenant_id = var.project_id
  password = var.openstack_host_password 
}

variable "openstack_host_password" {
    type = string
    sensitive = true
}
