locals {
    openstack_auth_url = "https://dhbw.cloud:5000/"
    openstack_host_user = "pfisterer-cloud-lecture"

    public_key    = file("~/.ssh/id_ed25519.pub")
    private_key   = file("~/.ssh/id_ed25519")
    machine_name  = "cloud-lecture"
}

