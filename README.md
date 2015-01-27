# nimbble-dev

Development Environment with Vagrant 
-----------------------------------

* This is recomended if you are in a windows environment and a very good idea for other enviroments in general to isolate and configure your dev. environments.

### Requirements

* VirtualBox
* Vagrant
* Shell with SSH support. Cygwin or Cmder (windows)

### Steps

####Make sure you open your shell as an Administrator.

1. Clone repo
2. Navigate to repo folder.
  * cd nimbble-dev
3. type: vagrant up
  * This will download the image if it is the first time it is ran.
  * After the image is loaded it will provision the commands on bootstrap.sh
  * Could take some time the first time.
4. To ssh into your dev environment type: vagrant ssh
5. When you ssh into the VM some scripts will run and finish insalling dependencies. Your viertual enviroment will be automatically setup. Your prompt should look like this:
  * (nimbble-dev)vagrant@vagrant-ubuntu-trusty-64:/nimbble-dev$
6. The first time you ssh you will need to run:
  * pip install -r requirements/local.txt
7. python nimbble/manage.py migrate
8. grunt serve
9. From your host machine you can now:
  * Browse to http://localhost:8000/
  * Edit your files with your favorite IDE.

### Notes:

* To shutdown the vm from running, you can exit ssh and run:
  * vagrant halt (Prefer if you want to shutdown the machine to free up some resources)
* To suspend the vm. (A suspend effectively saves the exact point-in-time state of the machine, so that when you resume it later)
  * vagrant suspend
  * vagrant resume (To start guest vm again.)
* To completely clean up and remove the guest image use:
  * vagrant destroy (This command stops the running machine Vagrant is managing and destroys all resources that were created during the machine creation process. )






