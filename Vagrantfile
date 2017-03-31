# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
    config.vm.box = "hashicorp/precise64"
    config.vm.box_url = "http://files.vagrantup.com/precise64.box"
    config.vm.network :forwarded_port, guest: 8080, host: 8080
    config.vm.synced_folder "src/", "/home/vagrant/src", create:true
    config.vm.provision :shell, path: "bootstrap.sh"
end