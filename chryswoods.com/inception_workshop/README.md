# Building and Deploying Custom JupyterHub Images using Docker and Kubernetes to run Workshops in the Cloud

Jupyter provides an excellent interactive environment for running workshops. While there are many free services that let you explore Jupyter, you will need to run your own JupyterHub server if you want to use a custom image that includes your own software, if you want more cores than are provided by the free service, or you want to run a workshop with large numbers of attendees. Building and deploying your own JupyterHub using Docker, Kubernetes and the Cloud is very easy, and this workshop will show you how. You will build your own Docker image, create your own Cloud Kubernetes cluster, and will then deploy JupyterHub to this cluster using Helm. We will also provide tips and tricks we’ve learned from running Jupyter workshops ourselves. So, in short, this is a workshop in which you will learn how to build and run your own workshop

## Recommended prerequisites
You should be comfortable using the Linux command line, should have a very basic understanding of what Docker (or containers) are, and have some knowledge of what Jupyter is (we will provide background reading on Docker and Jupyter, and will teach you about Kubernetes, JupyterHub, and deploying these to the cloud).

## Installing the material onto the VM

The VM needs to have the following installed:

1. Git (so you can download and update this material)
1. A Python that includes jupyter (we will use the installed python3)
1. Docker, with a running docker service
1. The Microsoft "az" command line interface
1. The "kubectl" interface installed via "az"
1. Helm

## Getting Started

If you are attending a workshop then all of the necessary software should have already be installed in your workshop VM. For the RSE18 workshop you can validate this is the case by typing;

```
workshops@RSE2018-workshops:~$ cd woods
workshops@RSE2018-workshops:~/woods$ git pull
workshops@RSE2018-workshops:~/woods$ source conda.sh
workshops@RSE2018-workshops:~/woods$ conda activate idp
(idp) workshops@RSE2018-workshops:~/woods$ python test_workshop.py 
Tesing git...  PASS
Testing jupyter...  PASS
Testing docker...  PASS
Testing az...  PASS
Testing kubectl...  PASS
Testing helm...  PASS
Success. Looks like everything has installed correctly :-)
```

If you see the "Success. Looks like everything has installed correctly :-)" message, then you can [move onto the next section](course/part01.md).

## Installation Instructions

If you are running this at home on your own computer, then you will need to install the software yourself. The below instructions provide all of the necessary instructions. If you are taking part in a workshop, then all of the software is installed, so you can [move onto the next section](course/part01.md).

Instructions to install and test all of these are below.

### git

Install

```
# sudo apt install git
```

Test

```
# git clone https://github.com/chryswoods/k8s_jupyter_workshop ./woods
# cd woods
# ls
Dockerfile       README.md        course           fix-permissions  test_workshop.py
LICENSE          conda.sh         example_workshop jupyterhub
```

(this should result in the contents of this GitHub repository being
 downloaded into the local directory called ./woods)

### Jupyter

We need a Python that includes Jupyter. The easiest way to do this is to use
the existing python3 and install jupyter into a virtualenv

First, we need to make sure that virtualenv is installed

```
# sudo apt install virtualenv
```

Now install jupyter into the virtualenv in the workshop directory

```
# virtualenv --python=python3 woods_project
# source woods_project/bin/activate
# pip install jupyter
```

Once jupyter has installed, you can test using

```
# jupyter-notebook
```

This should print out a lot to the screen showing that Jupyter is starting, 
and then it will launch a web browser with a Jupyter file dialog.

You can close the web browser and use "CTRL+C" to shut down the 
Jupyter server.

When you have finished in the virtualenv, you can exit by typing

```
# deactivate
```

### Docker

Install `docker-ce` using the instructions [here](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce)

```
# sudo apt-get update
# sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# sudo apt-key fingerprint 0EBFCD88

pub   4096R/0EBFCD88 2017-02-22
      Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid                  Docker Release (CE deb) <docker@docker.com>
sub   4096R/F273FCD8 2017-02-22

# sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   edge"

# sudo apt-get update
# sudo apt-get install docker-ce
```

(note we had to use the "edge" repository as a "stable" version for docker-ce
does not exist yet for Ubuntu 18.04).

Next, you need to add the current user to the "docker" group. Do this
using

```
# sudo usermod -a -G docker $USER
```

You will now need to log out and in again (actually have to reboot!)

Once you have logged in again, test, by running

```
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
Digest: sha256:f5233545e43561214ca4891fd1157e1c3c563316ed8e237750d59bde73361e77
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```

and you should see the output as printed below the command.

## Microsoft "az" command line interface

We will install following the instructions [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest)

```
# AZ_REPO=$(lsb_release -cs)
# echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | sudo tee /etc/apt/sources.list.d/azure-cli.list
# curl -L https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add 
# sudo apt-get install apt-transport-https
# sudo apt-get update && sudo apt-get install azure-cli
```

To test, run the command `az`, which should result in something similar to;

```
# az

     /\
    /  \    _____   _ _ __ ___
   / /\ \  |_  / | | | \'__/ _ \
  / ____ \  / /| |_| | | |  __/
 /_/    \_\/___|\__,_|_|  \___|


Welcome to the cool new Azure CLI!

Here are the base commands:

    account          : Manage Azure subscription information.
    acr              : Manage Azure Container Registries.
    acs              : Manage Azure Container Services.
    ad               : Synchronize on-premises directories and manage Azure Active Directory
                       resources.
    advisor          : (PREVIEW) Manage Azure Advisor.
    aks              : Manage Kubernetes clusters.
    appservice       : Manage App Service plans.
    backup           : Commands to manage Azure Backups.
    batch            : Manage Azure Batch.
    batchai          : Batch AI.
    billing          : Manage Azure Billing.
    cdn              : Manage Azure Content Delivery Networks (CDNs).
    cloud            : Manage registered Azure clouds.
    cognitiveservices: Manage Azure Cognitive Services accounts.
    configure        : Display and manage the Azure CLI 2.0 configuration. This command is
                       interactive.
    consumption      : Manage consumption of Azure resources.
    container        : (PREVIEW) Manage Azure Container Instances.
    cosmosdb         : Manage Azure Cosmos DB database accounts.
    disk             : Manage Azure Managed Disks.
    dla              : (PREVIEW) Manage Data Lake Analytics accounts, jobs, and catalogs.
    dls              : (PREVIEW) Manage Data Lake Store accounts and filesystems.
    eventgrid        : Manage Azure Event Grid topics and subscriptions.
    extension        : Manage and update CLI extensions.
    feature          : Manage resource provider features.
    feedback         : Loving or hating the CLI?  Let us know!
    find             : Find Azure CLI commands.
    functionapp      : Manage function apps.
    group            : Manage resource groups and template deployments.
    identity         : Managed Service Identities.
    image            : Manage custom virtual machine images.
    interactive      : Start interactive mode.
    iot              : (PREVIEW) Manage Internet of Things (IoT) assets.
    keyvault         : Safeguard and maintain control of keys, secrets, and certificates.
    lab              : Manage Azure DevTest Labs.
    lock             : Manage Azure locks.
    login            : Log in to Azure.
    logout           : Log out to remove access to Azure subscriptions.
    managedapp       : Manage template solutions provided and maintained by Independent Software
                       Vendors (ISVs).
    monitor          : Manage the Azure Monitor Service.
    mysql            : Manage Azure Database for MySQL servers.
    network          : Manage Azure Network resources.
    policy           : Manage resource policies.
    postgres         : Manage Azure Database for PostgreSQL servers.
    provider         : Manage resource providers.
    redis            : Access to a secure, dedicated Redis cache for your Azure applications.
    reservations     : Manage Azure Reservations.
    resource         : Manage Azure resources.
    role             : Manage user roles for access control with Azure Active Directory and service
                       principals.
    sf               : Manage and administer Azure Service Fabric clusters.
    snapshot         : Manage point-in-time copies of managed disks, native blobs, or other
                       snapshots.
    sql              : Manage Azure SQL Databases and Data Warehouses.
    storage          : Manage Azure Cloud Storage resources.
    tag              : Manage resource tags.
    vm               : Provision Linux or Windows virtual machines.
    vmss             : Manage groupings of virtual machines in an Azure Virtual Machine Scale Set
                       (VMSS).
    webapp           : Manage web apps.
```

## kubectl interface via az

Next we need to install kubectl using az. Type

```
# sudo az aks install-cli
```

If this works, you should see kubectl being installed. You can type by
typing `kubectl` and seeing if the following is printed

```
# kubectl

kubectl controls the Kubernetes cluster manager. 

Find more information at https://github.com/kubernetes/kubernetes.

Basic Commands (Beginner):
  create         Create a resource from a file or from stdin.
  expose         Take a replication controller, service, deployment or pod and
expose it as a new Kubernetes Service
  run            Run a particular image on the cluster
  set            Set specific features on objects
  run-container  Run a particular image on the cluster. This command is
deprecated, use "run" instead

Basic Commands (Intermediate):
  get            Display one or many resources
  explain        Documentation of resources
  edit           Edit a resource on the server
  delete         Delete resources by filenames, stdin, resources and names, or
by resources and label selector

Deploy Commands:
  rollout        Manage the rollout of a resource
  rolling-update Perform a rolling update of the given ReplicationController
  scale          Set a new size for a Deployment, ReplicaSet, Replication
Controller, or Job
  autoscale      Auto-scale a Deployment, ReplicaSet, or ReplicationController

Cluster Management Commands:
  certificate    Modify certificate resources.
  cluster-info   Display cluster info
  top            Display Resource (CPU/Memory/Storage) usage.
  cordon         Mark node as unschedulable
  uncordon       Mark node as schedulable
  drain          Drain node in preparation for maintenance
  taint          Update the taints on one or more nodes

Troubleshooting and Debugging Commands:
  describe       Show details of a specific resource or group of resources
  logs           Print the logs for a container in a pod
  attach         Attach to a running container
  exec           Execute a command in a container
  port-forward   Forward one or more local ports to a pod
  proxy          Run a proxy to the Kubernetes API server
  cp             Copy files and directories to and from containers.
  auth           Inspect authorization

Advanced Commands:
  apply          Apply a configuration to a resource by filename or stdin
  patch          Update field(s) of a resource using strategic merge patch
  replace        Replace a resource by filename or stdin
  convert        Convert config files between different API versions

Settings Commands:
  label          Update the labels on a resource
  annotate       Update the annotations on a resource
  completion     Output shell completion code for the specified shell (bash or
zsh)

Other Commands:
  api-versions   Print the supported API versions on the server, in the form of
"group/version"
  config         Modify kubeconfig files
  help           Help about any command
  plugin         Runs a command-line plugin
  version        Print the client and server version information

Use "kubectl <command> --help" for more information about a given command.
Use "kubectl options" for a list of global command-line options (applies to all
commands).
```

## Helm

The final step is to install helm, following the instructions from 
[here](https://github.com/kubernetes/helm/blob/master/docs/install.md)

```
# curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get > get_helm.sh
# chmod 700 get_helm.sh
# ./get_helm.sh
```

Test by trying to run the command `helm`, which should produce the 
output that is similar to the below

```
# helm

The Kubernetes package manager

To begin working with Helm, run the 'helm init' command:

	$ helm init

This will install Tiller to your running Kubernetes cluster.
It will also set up any necessary local configuration.

Common actions from this point include:

- helm search:    search for charts
- helm fetch:     download a chart to your local directory to view
- helm install:   upload the chart to Kubernetes
- helm list:      list releases of charts

Environment:
  $HELM_HOME          set an alternative location for Helm files. By default, these are stored in ~/.helm
  $HELM_HOST          set an alternative Tiller host. The format is host:port
  $HELM_NO_PLUGINS    disable plugins. Set HELM_NO_PLUGINS=1 to disable plugins.
  $TILLER_NAMESPACE   set an alternative Tiller namespace (default "kube-system")
  $KUBECONFIG         set an alternative Kubernetes configuration file (default "~/.kube/config")

Usage:
  helm [command]

Available Commands:
  completion  Generate autocompletions script for the specified shell (bash or zsh)
  create      create a new chart with the given name
  delete      given a release name, delete the release from Kubernetes
  dependency  manage a chart's dependencies
  fetch       download a chart from a repository and (optionally) unpack it in local directory
  get         download a named release
  history     fetch release history
  home        displays the location of HELM_HOME
  init        initialize Helm on both client and server
  inspect     inspect a chart
  install     install a chart archive
  lint        examines a chart for possible issues
  list        list releases
  package     package a chart directory into a chart archive
  plugin      add, list, or remove Helm plugins
  repo        add, list, remove, update, and index chart repositories
  reset       uninstalls Tiller from a cluster
  rollback    roll back a release to a previous revision
  search      search for a keyword in charts
  serve       start a local http web server
  status      displays the status of the named release
  template    locally render templates
  test        test a release
  upgrade     upgrade a release
  verify      verify that a chart at the given path has been signed and is valid
  version     print the client/server version information

Flags:
      --debug                     enable verbose output
  -h, --help                      help for helm
      --home string               location of your Helm config. Overrides $HELM_HOME (default "/home/chris/.helm")
      --host string               address of Tiller. Overrides $HELM_HOST
      --kube-context string       name of the kubeconfig context to use
      --tiller-namespace string   namespace of Tiller (default "kube-system")

Use "helm [command] --help" for more information about a command.
```

Once you are happy, you can remove the `get_helm.sh` script, e.g.

```
# rm get_helm.sh
```

## Everything installed - let's run a final test

Congratulations - everything should now be installed. Please
confirm this by running the following command, which is included
with this repository (and so should have been downloaded by
the git clone command above)

```
# source woods_project/bin/activate
# python test_workshop.py

Tesing git...  PASS
Testing jupyter...  PASS
Testing docker...  PASS
Testing az...  PASS
Testing kubectl...  PASS
Testing helm...  PASS

Success. Looks like everything has installed correctly :-)
```

Hopefully you will see the "Success" message. If not, check the instructions
above or send me an [email](mailto:chryswoods@gmail.com)

