resource "openstack_compute_instance_v2" "master" {
  name            = "gridflex-master"
  image_id        = var.image_id
  flavor_name     = var.flavor_name
  key_pair        = var.key_pair
  security_groups = ["default"]
  network { name = var.network_name }
}

resource "openstack_compute_instance_v2" "worker" {
  count           = 2
  name            = "gridflex-worker-${count.index + 1}"
  image_id        = var.image_id
  flavor_name     = var.flavor_name
  key_pair        = var.key_pair
  security_groups = ["default"]
  network { name = var.network_name }
}
