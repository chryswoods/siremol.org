# Step 6 - Creating the kubernetes cluster

In the last lesson you uploaded your custom jupyterhub docker image to your private Azure Container Registry.

The next step is to create your own Kubernetes cluster on the [Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-gb/services/kubernetes-service/).

[Kubernetes](https://kubernetes.io/) is an example of a container orchestrator service. It is production quality, widely used and fully open source. Kubernetes works by spinning up and down pods, which are containers running on hardware. [Lots of documentation and tutorials are available here](https://kubernetes.io/docs/tutorials/). I have also written a [nice talk](https://drive.google.com/file/d/1kI7NB7jsIReVm2rznBTOcSMaLCuz7O9Q/view) that shows how Kubernetes and JupyterHub work together (from slide 32 onwards). There is also a nice [quickstart guide to using Kubernetes on Azure via AKS](https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough).

We are going to now create a kubernetes cluster called `jupyter` in your `rseworkshop` resource group. For this workshop we will give the cluster just 2 cores on a single A2v2 machine instance. This costs about $0.076 per hour, so is pretty inexpensive ;-). Feel free to use more or larger machine instances for larger workshops. The full list of instances available and prices are [available here](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/).

To create the cluster use the command;

```
$ az aks create --resource-group rseworkshop --name jupyter --node-count 1 --node-vm-size Standard_A2_v2 --generate-ssh-keys
 - Running ..
{
  "aadProfile": null,
  "addonProfiles": null,
  "agentPoolProfiles": [
    {
      "count": 1,
      "dnsPrefix": null,
      "fqdn": null,
      "maxPods": 110,
      "name": "nodepool1",
      "osDiskSizeGb": null,
      "osType": "Linux",
      "ports": null,
      "storageProfile": "ManagedDisks",
      "vmSize": "Standard_A2_v2",
      "vnetSubnetId": null
    }
  ],
  "dnsPrefix": "jupyter-rseworkshop-235d32",
  "enableRbac": true,
  "fqdn": "jupyter-rseworkshop-235d32-7b4b2571.hcp.westeurope.azmk8s.io",
  "id": "/subscriptions/235d329c-dea9-479d-9a72-632f40ff6f57/resourcegroups/rseworkshop/providers/Microsoft.ContainerService/managedClusters/jupyter",
  "kubernetesVersion": "1.9.9",
  "linuxProfile": {
    "adminUsername": "azureuser",
    "ssh": {
      "publicKeys": [
        {
          "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDbcwy6GSucnCESfPRfJFZynateh7QMBICeHpCkd3ufIt/4GaYCeeCe+hZXwZq0V32cOkloGXJcBik9GLJp3zTr5NztEntIJ6U6KMrtpWQ559Bt6+tTwejxO97O3dc0ZQNgG87b4ONhdsgUhqNr4Sy2kNu6/QY5/UXwCUXpJLKcx1NW+bxetf9O0ADymz+Q0bepVLXLwk+XUpJ0i7h4+ONxSJhFaFoeTlo1ycOdZdCjKhl9NbetSBcc+JEMWvmBf/rhE1/YwoNpTnusciIgCw0tLB1NqxgRP6QwBD5FdmXzpMmJjoqBnZ1B6LqCkWNwwqnz0k+4Ma9KKro9SamKBTSj workshops@RSE2018-workshops\n"
        }
      ]
    }
  },
  "location": "westeurope",
  "name": "jupyter",
  "networkProfile": {
    "dnsServiceIp": "10.0.0.10",
    "dockerBridgeCidr": "172.17.0.1/16",
    "networkPlugin": "kubenet",
    "networkPolicy": null,
    "podCidr": "10.244.0.0/16",
    "serviceCidr": "10.0.0.0/16"
  },
  "nodeResourceGroup": "MC_rseworkshop_jupyter_westeurope",
  "provisioningState": "Succeeded",
  "resourceGroup": "rseworkshop",
  "servicePrincipalProfile": {
    "clientId": "074f373f-83cc-4c6c-a33f-2e772163c2b7",
    "keyVaultSecretRef": null,
    "secret": null
  },
  "tags": null,
  "type": "Microsoft.ContainerService/ManagedClusters"
}
```

This may take a few minutes (I spent ten minutes watching the spinning ascii running logo...). When it finishes, you will hopefully see output similar to the above.

## Connecting to your kubernetes cluster

You connect to your kubernetes cluster using `kubectl`. We have already installed this program for you in this image. If you don't have it installed, then you can install it using the command;

```
$ az aks install-cli
```

The connect to your cluster you need to download its login credentials. You can get the credentials using the command;

```
$ az aks get-credentials --resource-group rseworkshop --name jupyter
Merged "jupyter" as current context in /home/workshops/.kube/config
```

Hopefully this succeeds and you see output similar to the above.

If it has succeeded, then you can query the nodes in your kubernetes cluster using the command;

```
$ kubectl get nodes
NAME                       STATUS    ROLES     AGE       VERSION
aks-nodepool1-21146987-0   Ready     agent     9m        v1.9.9
```

If this works, you should see that you have 1 node available. Normally you should have 3 nodes, as this gives resilience. For this workshop, and generally for testing, we use 1 node. It is possible to change the number of nodes dynamically after creating the workshop, so good practice is to create the initial workshop with 1 node, and to then scale up to as many nodes as needed during your workshop. Once the workshop is over you can then scale back down to 1 node.

## Giving your Kubernetes cluster permission to access your acr

Now you have a kubernetes cluster, you have to give it permission to download containers from your Azure container repository (acr). Do that by executing the below three commands (yes - yet more quite cryptic commands!)

```
$ CLIENT_ID=$(az aks show --resource-group rseworkshop --name jupyter --query "servicePrincipalProfile.clientId" --output tsv)
$ ACR_ID=$(az acr show --name ChryswoodsContainers --resource-group rseworkshop --query "id" --output tsv)
$ az role assignment create --assignee $CLIENT_ID --role Reader --scope $ACR_ID
{
  "canDelegate": null,
  "id": "/subscriptions/235d329c-dea9-479d-9a72-632f40ff6f57/resourceGroups/rseworkshop/providers/Microsoft.ContainerRegistry/registries/ChryswoodsContainers/providers/Microsoft.Authorization/roleAssignments/b776b62c-65f0-4244-bafb-8a4fe67012e2",
  "name": "b776b62c-65f0-4244-bafb-8a4fe67012e2",
  "principalId": "2fffb5c4-2c33-45e4-a950-1cb956305fa9",
  "resourceGroup": "rseworkshop",
  "roleDefinitionId": "/subscriptions/235d329c-dea9-479d-9a72-632f40ff6f57/providers/Microsoft.Authorization/roleDefinitions/acdd72a7-3385-48ef-bd42-f606fba81ae7",
  "scope": "/subscriptions/235d329c-dea9-479d-9a72-632f40ff6f57/resourceGroups/rseworkshop/providers/Microsoft.ContainerRegistry/registries/ChryswoodsContainers",
  "type": "Microsoft.Authorization/roleAssignments"
}
```

(remembering to substitute `ChryswoodsContainers` with the name of your acr. Note that you don't need to execute these commands if you are using the pre-supplied ChryswoodsContainers acr, as this is public)

***

# [Previous](part05.md) [Up](../README.md) [Next](part07.md)

