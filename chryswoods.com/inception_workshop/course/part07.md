# Step 7 - Using Helm to install JupyterHub

[Helm](https://helm.sh/) is the package manager for kubernetes. It is used to simplify the process of installing software into a kubernetes cluster. Helm is already installed in the RSE workshop VM. We need to give permission to helm to access and manage our kubernets cluster. To do this, we need to create a kubernetes service account (which we will call tiller). This is defined in the file `helm-rbac.yaml` which is included with this workshop. We create the account by applying this file in the kubernetes cluster using the command;

```
$ kubectl apply -f helm-rbac.yaml
serviceaccount/tiller created
clusterrolebinding.rbac.authorization.k8s.io/tiller created
```

Nex we need to initialise the kubernetes cluster with helm, telling it to use the tiller service account. To do this, run the command;

```
$ helm init --service-account tiller
Creating /home/workshops/.helm 
Creating /home/workshops/.helm/repository 
Creating /home/workshops/.helm/repository/cache 
Creating /home/workshops/.helm/repository/local 
Creating /home/workshops/.helm/plugins 
Creating /home/workshops/.helm/starters 
Creating /home/workshops/.helm/cache/archive 
Creating /home/workshops/.helm/repository/repositories.yaml 
Adding stable repo with URL: https://kubernetes-charts.storage.googleapis.com 
Adding local repo with URL: http://127.0.0.1:8879/charts 
$HELM_HOME has been configured at /home/workshops/.helm.

Tiller (the Helm server-side component) has been installed into your Kubernetes Cluster.

Please note: by default, Tiller is deployed with an insecure 'allow unauthenticated users' policy.
For more information on securing your installation see: https://docs.helm.sh/using_helm/#securing-your-helm-installation
Happy Helming!
```

If this works, you should output similar to the above. 

The package installation scripts for helm are called helm charts. We need to add the repository that contains the JupyterHub helm chart. Do this using the commands

```
$ helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
"jupyterhub" has been added to your repositories
$ helm repo update
Hang tight while we grab the latest from your chart repositories...
...Skip local chart repository
...Successfully got an update from the "jupyterhub" chart repository
...Successfully got an update from the "stable" chart repository
Update Complete. ⎈ Happy Helming!⎈ 
```

## Giving your kubernetes cluster access to your docker repository

Next, you need to give your kubernetes cluster read access to your
acr docker repository. To do this you have to create a service account
with password that has access. This is performed using a set of
cryptic commands that are contained in the script `get_acr_login.sh`.
You need to edit this file to change the `ACR_NAME` to match the name
of your acr repository, and to set `EMAIL_ADDRESS` to your email address.

Do this by editing the file, e.g. using vim

```
$ vim get_acr_login.sh
#!/bin/bash

##################################
# You will need to change the below two lines to match
# your acr
ACR_NAME=ChryswoodsContainers
EMAIL_ADDRESS=chryswoods@gmail.com
##################################
```

Once you have made the changes, execute the script using

```
$ ./get_acr_login.sh 
Service principal ID: XXXXXXXXXXXXXXXXXXXX
Service principal password: XXXXXXXXXXXXXXXXXXX
secret/acr-auth created
```

You should see that the service account userID and password are created, and that these have been saved into a kubernetes secret called `secret/acr-auth`.

## Configuring your JupyterHub install

You need to setup the configuration for your JupyterHub install. The configuration files are in [yaml format](http://yaml.org/start.html). You are provided with a demonstration configuration file called `values.yaml`. You will need to edit to set the name of the image you created. To do this, edit `values.yaml` and change the docker image name to match your image, e.g.

```
$ vim values.yaml
proxy:
  secretToken: "32f0d34e18e6da51136a5de768e2e4bc2464c8cc6c650a41fcb5db1b4ffc64$
hub:
  db:
    type: sqlite-memory
singleuser:
  image:
    name: chryswoodscontainers.azurecr.io/workshop-hub
    tag: v1
  storage:
```

and change `chryswoodscontainers.azurecr.io/workshop-hub` to `your-acr-name.azurecr.io/workshop-hub`.

## Installing JupyterHub using Helm

To (finally!!!) install your JupyterHub using Helm onto your Azure Kubernetes cluster use the following command;

```
$ helm install jupyterhub/jupyterhub --version=0.6 --timeout=3600 --name=workshop --namespace=workshop -f values.yaml
Error: watch closed before Until timeout
```

As above, this command can take a long time and you may see it error with a timeout. Don't worry - it is actually working. It is slow because your cloud node has to download the 1.1GB workshop container image from the Azure container repository, which can be a little slow. If it times out with an error, simply run the command again. This will resume the pull :-)

```
$ helm install jupyterhub/jupyterhub --version=0.6 --timeout=3600 --name=workshop -f values.yaml
NAME:   workshop
LAST DEPLOYED: Fri Aug 10 18:37:37 2018
NAMESPACE: default
STATUS: DEPLOYED

RESOURCES:
==> v1/ConfigMap
NAME                DATA  AGE
hub-config          29    7s
nginx-proxy-config  1     7s

==> v1/Service
NAME          TYPE          CLUSTER-IP    EXTERNAL-IP  PORT(S)                     AGE
hub           ClusterIP     10.0.215.128  <none>       8081/TCP                    5s
proxy-api     ClusterIP     10.0.169.162  <none>       8001/TCP                    5s
proxy-http    ClusterIP     10.0.6.197    <none>       8000/TCP                    4s
proxy-public  LoadBalancer  10.0.161.144  <pending>    80:31930/TCP,443:31242/TCP  4s

==> v1beta1/DaemonSet
NAME                     DESIRED  CURRENT  READY  UP-TO-DATE  AVAILABLE  NODE SELECTOR  AGE
continuous-image-puller  1        1        0      1           0          <none>         4s

==> v1beta1/PodDisruptionBudget
NAME   MIN AVAILABLE  MAX UNAVAILABLE  ALLOWED DISRUPTIONS  AGE
hub    1              N/A              0                    4s
proxy  1              N/A              0                    4s

==> v1/Pod(related)
NAME                                  READY  STATUS             RESTARTS  AGE
continuous-image-puller-wf722         0/1    Init:1/2           0         4s
pre-pull-workshop-1-1533922452-dnnjl  1/1    Running            0         3m
hub-85c76b5f48-ghwf6                  0/1    ContainerCreating  0         4s
proxy-695f48c594-559mm                0/2    ContainerCreating  0         3s

==> v1beta1/RoleBinding
NAME       AGE
hub        5s
kube-lego  5s
nginx      5s

==> v1beta1/Deployment
NAME   DESIRED  CURRENT  UP-TO-DATE  AVAILABLE  AGE
hub    1        1        1           0          4s
proxy  1        1        1           0          4s

==> v1/Secret
NAME        TYPE    DATA  AGE
hub-secret  Opaque  1     7s

==> v1/ServiceAccount
NAME   SECRETS  AGE
hub    1        7s
proxy  1        6s

==> v1beta1/ClusterRole
NAME            AGE
nginx-workshop  6s

==> v1beta1/ClusterRoleBinding
NAME            AGE
nginx-workshop  6s

==> v1beta1/Role
NAME       AGE
hub        6s
kube-lego  6s
nginx      5s


NOTES:
Thank you for installing JupyterHub!

Your release is named workshop and installed into the namespace default.

You can find if the hub and proxy is ready by doing:

 kubectl --namespace=default get pod

and watching for both those pods to be in status 'Ready'.

You can find the public IP of the JupyterHub by doing:

 kubectl --namespace=default get svc proxy-public

It might take a few minutes for it to appear!

Note that this is still an alpha release! If you have questions, feel free to
  1. Come chat with us at https://gitter.im/jupyterhub/jupyterhub
  2. File issues at https://github.com/jupyterhub/zero-to-jupyterhub-k8s/issues

```

Once it completes successfully you will see something similar to the above output. You can see the kubernetes pods that are running using the command;

```
$ kubectl get pods
NAME                                     READY     STATUS      RESTARTS   AGE
continuous-image-puller-wf722            1/1       Running     0          2m
hub-85c76b5f48-ghwf6                     1/1       Running     1          2m
pre-pull-workshop-1-1533922452-dnnjl     1/1       Running     0          6m
pre-puller-1533922452-workshop-1-t9czn   0/1       Completed   0          6m
proxy-695f48c594-559mm                   2/2       Running     0          2m
```

To get the IP address of your JupyterHub server type the command

```
$ kubectl get services
NAME           TYPE           CLUSTER-IP     EXTERNAL-IP       PORT(S)                      AGE
hub            ClusterIP      10.0.215.128   <none>            8081/TCP                     3m
kubernetes     ClusterIP      10.0.0.1       <none>            443/TCP                      1h
proxy-api      ClusterIP      10.0.169.162   <none>            8001/TCP                     3m
proxy-http     ClusterIP      10.0.6.197     <none>            8000/TCP                     3m
proxy-public   LoadBalancer   10.0.161.144   137.117.174.168   80:31930/TCP,443:31242/TCP   3m
```

The external IP for my server can be see here as `137.117.174.168`. Your's will be different (and may take a little time to appear). Congratulations, as you now have a working JupyterHub ready for your workshop! You can connect to it by navigating to `http://IP_ADDRESS/hub/tmplogin`, e.g. for me I go to `http://137.117.174.168/hub/tmplogin`.

By navigating to here in my webbrowser, it automatically logs into my jupyterhub, creates a temporary account, and then starts a jupyter-notebook session using the docker container we created [many lessons ago](part04.md).

## Exercise

Log onto your cloud jupyterhub session and check that your workshop works as expected.

Now make some changes to your docker image (e.g. add more course material). Build the image and tag it as a new version of your X.azureio.cr/workshop-hub image. Push it to the Azure container repository, and then update `values.yaml` with the new version.

You can now update your jupyterhub kubernetes installation using the new version via the command;

```
$ helm upgrade workshop jupyterhub/jupyterhub --timeout=3600 --version=v0.6 -f values.yaml
```

***

# [Previous](part06.md) [Up](../README.md) [Next](part08.md)

