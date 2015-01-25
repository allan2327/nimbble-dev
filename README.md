# nimbble-dev

Requirements
------------
 [] python 3
 [] pip
 [] virtualenv (if you are smart)

Quick Startup
-------------
 1) clone repo, open cmd into directory
 2) $>pip install -r requirements
 3) $>python nimbble\manage.py migrate
 4) $>python nimbble\manage.py runserver

Developent Environment with Vagrant
-----------------------------------

### Requirements

* VirtualBox
* Vagrant
* Shell with SSH support. Cygwin or Cmder (windows)

### Steps

1. Clone repo
2. Navigate to repo folder.
  * cd nimbble-dev
3. type: vagrant up
  * This will download the image if it is the first time it is ran.
  * After the image is loaded it will provision the commands on bootstrap.sh
  * Could take some time the first time.
4. Type to ssh into your dev environment: vagrant ssh
5. Type: cd /nimbble-dev
6. Activate virtual env. 
  * Type: source bin/active
  * Propmt should look like this: (nimbble-dev)vagrant@precise32:/nimbble-dev$
7. python nimbble/manage.py migrate
8. python nimbble/manage.py runserver 0.0.0.0:8000
  * The host and the port with 0.0.0.0:8000 are requiered due to a django/virtualbox restriction for localhost and port forwarding.
7. From the host you can go to a browser and navigate to:
  * http://localhost:8000

### Note:

* To shutdown the vm from running you can exit ssh and run:
  * vagrant halt (Prefer if you want to shutdown the machine to free up some resources)
* To suspend the vm. (A suspend effectively saves the exact point-in-time state of the machine, so that when you resume it later)
  * vagrant suspend
  * vagrant resume (To start guest vm again.)
* To completely clean up and remove the guest image use:
  * vagrant destroy (This command stops the running machine Vagrant is managing and destroys all resources that were created during the machine creation process. )






