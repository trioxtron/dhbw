output "master_ip" {
  value = openstack_compute_instance_v2.master.network[0].fixed_ip_v4
}

output "worker_ips" {
  value = openstack_compute_instance_v2.worker[*].network[0].fixed_ip_v4
}

resource "local_file" "ansible_inventory" {
  filename = "${path.module}/generated-inventory.yml"
  content = yamlencode({
    all = {
      children = {
        gridflex = {
          children = {
            gridflex_k3s_server = {
              hosts = {
                (openstack_compute_instance_v2.master.network[0].fixed_ip_v4) = {
                  interpreter_python = "/usr/bin/python3"
                  ansible_user       = "ubuntu"
                  ip_family          = "ipv4"
                  k3s_role           = "server"

                }
              }
            }
            gridflex_k3s_agent = {
              vars = {
                interpreter_python = "/usr/bin/python3"
                k3s_server_host    = openstack_compute_instance_v2.master.network[0].fixed_ip_v4
                k3s_role           = "agent"
              }
              hosts = {
                for w in openstack_compute_instance_v2.worker :
                w.network[0].fixed_ip_v4 => {
                  ansible_user = "ubuntu"
                }
              }
            }
          }
        }
      }
    }
  })
}
