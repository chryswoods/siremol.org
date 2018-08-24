# Step 5 - Uploading your image to the cloud

To run your workshop on the cloud the next step is to upload your JupyterHub workshop container to a cloud docker container repository.

There are several docker container repositories. If you have a dockerhub account you could upload to there. As we will be using the [Azure Kubernetes Service](https://azure.microsoft.com/en-gb/services/kubernetes-service/) later to host our workshop, it is a good idea to use the [Azure Container Repository (acr)](https://azure.microsoft.com/en-gb/services/container-registry/).

The first step is to connect to Azure. We will use the Azure command line interface tool, `az`. Login to Azure using the command;

```
$ az login
Note, we have launched a browser for you to login. For old experience with device code, use "az login --use-device-code"
You have logged in. Now let us find all subscriptions you have access to...
[
  {
    "cloudName": "AzureCloud",
    "id": "XXXXXXXXXXXXXXXXXXX",
    "isDefault": true,
    "name": "Free Trial",
    "state": "Enabled",
    "tenantId": "XXXXXXXXXXXXXXXXX",
    "user": {
      "name": "XXXXXXXXXXXXX",
      "type": "user"
    }
  },
  {
    "cloudName": "AzureCloud",
    "id": "XXXXXXXXXXXXXXXXXXX",
    "isDefault": false,
    "name": "Microsoft Azure Sponsorship",
    "state": "Enabled",
    "tenantId": "XXXXXXXXXXXXXXXXX",
    "user": {
      "name": "XXXXXXXXXXXXXXX",
      "type": "user"
    }
  }
]
```

The command will open up a page in your webbrowser in which you can type your Microsoft Azure username and password (for me this is my login.live.com Microsoft password that is associated with my Azure cloud credits). If you login successfully you should see similar output as above, e.g. showing your Azure username, tenancy etc.

Everything in Azure is held in a resource group. We need to create a resource group for the workshop. We will create a resource group called `rseworkshop` in the WestEurope region using the command;

```
$ az group create --name rseworkshop --location westeurope
{
  "id": "/subscriptions/235d329c-dea9-479d-9a72-632f40ff6f57/resourceGroups/rseworkshop",
  "location": "westeurope",
  "managedBy": null,
  "name": "rseworkshop",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null
}
```

Hopefully this has worked and you see similar output as above.

Next, we need to create an Azure Container Repository (acr) within this resource group. The name of the repository has to be unique across all of Azure. Thus use the name `UsernameContainers` where `username` is a unique name for you. For me, I will use `ChryswoodsContainers`. Do that using the following command;

```
$ az acr create --resource-group rseworkshop --name ChryswoodsContainers --sku Basic
{
  "adminUserEnabled": false,
  "creationDate": "2018-08-10T15:48:25.399833+00:00",
  "id": "/subscriptions/235d329c-dea9-479d-9a72-632f40ff6f57/resourceGroups/rseworkshop/providers/Microsoft.ContainerRegistry/registries/ChryswoodsContainers",
  "location": "westeurope",
  "loginServer": "chryswoodscontainers.azurecr.io",
  "name": "ChryswoodsContainers",
  "provisioningState": "Succeeded",
  "resourceGroup": "rseworkshop",
  "sku": {
    "name": "Basic",
    "tier": "Basic"
  },
  "status": null,
  "storageAccount": null,
  "tags": {},
  "type": "Microsoft.ContainerRegistry/registries"
}
```

Hopefully this works and you will see output similar to the above.

Next, you need to get the login server used for your new acr. You can get that using this command (remembering to substitute `ChryswoodsContainers` with the name of your container repository);

```
$ az acr list --resource-group rseworkshop --query "[].{acrLoginServer:loginServer}" --output table
AcrLoginServer
-------------------------------
chryswoodscontainers.azurecr.io
```

Again, hopefully this worked and you now know the name of the login server for your acr. For me, it is `chryswoodscontainers.azurecr.io` (so you now see why you have to have a unique name across the whole of Azure...)

Next you need to tag your workshop docker image with the name of the login servier. You should also add a version number to your workshop image, so that you can choose different versions later if you need to make any changes.

The name for your image should have the format `servername/imagename:version`. In my case, it will be `chryswoodscontainers.azurecr.io/workshop-hub:v1`. You can tag your container image using the command;

```
$ docker tag workshop-hub chryswoodscontainers.azurecr.io/workshop-hub:v1
```

(remembering to change the above command to use the name of your login server)

You can check this worked by typing

```
$ docker images
REPOSITORY                                     TAG                 IMAGE ID            CREATED             SIZE
chryswoodscontainers.azurecr.io/workshop-hub   v1                  9a3dd661420c        5 hours ago         1.09GB
workshop-hub                                   latest              9a3dd661420c        5 hours ago         1.09GB
ubuntu                                         <none>              14f60031763d        12 months ago       120MB
```

which should output something similar to the above (e.g. you can see your azurecr.io tagged image).

Now that your image is tagged, you can push it to the Azure cloud. To do this, you need to login to your acr using the command

```
$ az acr login --name ChryswoodsContainers
Login Succeeded
```

(remembering to change the name of the acr to your name)

Now (finally!) you can push your docker image to your repository, using;

```
$ docker push chryswoodscontainers.azurecr.io/workshop-hub:v1
The push refers to repository [chryswoodscontainers.azurecr.io/workshop-hub]
1c1ed2b89879: Pushed 
2701ed893798: Pushed 
c60d0a50097a: Pushed 
734d695de587: Pushed 
3fdcb4749dfb: Pushed 
6857c3270238: Pushed 
786ff4427a78: Pushed 
941a357031eb: Pushed 
92a073691801: Pushed 
1258495045c3: Pushed 
76f599f34869: Pushed 
8f8812bb756c: Pushed 
4c934cc894ff: Pushed 
fc76bf81f91b: Pushed 
58bb2276f5f0: Pushed 
0c2c3f53c1e4: Pushed 
26b126eb8632: Pushed 
220d34b5f6c9: Pushed 
8a5132998025: Pushed 
aca233ed29c3: Pushed 
e5d2f035d7a4: Pushed 
v1: digest: sha256:fcb0b029258cbc5f7a9d7f7f90f9339753a983f28671b82b08a0867744f298c3 size: 4703
```

Note that this will push the whole 1.1GB image, so may take some time depending on the speed of your network connection. If the network is too slow, then you can use the `chryswoodscontainers.azurecr.io/workshop-hub:v1` image that has already been uploaded in later steps in this workshop.

Hopefully your push worked and you saw output similar to the above. Congratulations - we are half-way to a working cloud workshop :-)

***

# [Previous](part04.md) [Up](../README.md) [Next](part06.md)

