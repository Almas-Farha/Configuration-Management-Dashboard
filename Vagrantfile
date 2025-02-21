Vagrant.configure("2") do |config|
  # Define Development Server
  config.vm.define "dev" do |dev|
    dev.vm.box = "ubuntu/bionic64"
    dev.vm.network "private_network", ip: "192.168.56.10"
    dev.vm.hostname = "dev-server"
  end

  # Define Staging Server
  config.vm.define "staging" do |staging|
    staging.vm.box = "ubuntu/bionic64"
    staging.vm.network "private_network", ip: "192.168.56.20"
    staging.vm.hostname = "staging-server"
  end

  # Define Production Server
  config.vm.define "prod" do |prod|
    prod.vm.box = "ubuntu/bionic64"
    prod.vm.network "private_network", ip: "192.168.56.30"
    prod.vm.hostname = "prod-server"
  end
end
config.vm.network "forwarded_port", guest: 5000, host: 5000
