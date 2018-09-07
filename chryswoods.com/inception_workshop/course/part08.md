# Step 8 - Configuring your JupyterHub workshop

The `values.yaml` file provides a way for your to configure your JupyterHub session. This is described in detail in the excellent [Zero to JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/) project website.

Key values are;

## Secret Token

```
secretToken: "32f0d34e18e6da51136a5de768e2e4bc2464c8cc6c650a41fcb5db1b4ffc6469
```

This is the secret token that is used by the different parts of the service to talk to each other. This should be secret! (so it is a mistake to use the value written above). You can generate the secret using the command

```
$ openssl rand -hex 32
e4cbc940f1d3697455e6e356a1a489f2c778ad00b770360fd35e7880c42165e2
```

Just copy and paste the output from running the command yourself into the `secretToken` field.

## Image

```
  image:
    name: chryswoodscontainers.azurecr.io/workshop-hub
    tag: v1
```

This sets the docker image to use for the notebook (and the version). If you make changes, remember to update the version. Always use a specific version number, rather than "latest", as this ensures that your JupyterHub will be told to update themselves whenever you change the image.

## Limits

```
  memory:
    limit: 0.5G
    guarantee: 0.2G
  cpu:
    limit: 0.5
    guarantee: 0.25
```

These are the minimum and maximum limits for each user who is logged into your JupyterHub service. Each user who logs in is guaranteed the "guarantee" value of memory and cpu (e.g. in this case 0.2 GB and 0.25 of a processor core). They are then limited to a maximum of "limit" (e.g. in this case 0.5 GB and 0.5 of a processor core). You need to use the limits to ensure that one user doesn't max out the memory or processors on your kubernetes servers. Memory is particularly important to limit, as otherwise your server could run out of memory, which would cause your cluster to break down.

In general, I find that memory usage is the limit, and that I use this to work out how to size my cluster. If I have 40 people in the workshop, then with a limit of 0.5 GB you would need a server with at least 20 GB of memory (or several servers with at least 20 GB of memory). If each attendee is guaranteed 0.25 of a core, then you would need at least 10 cores (remembering you need resource for JupyterHub itself). I generally prefer to size for 20-25% extra, to protect against some attendees accidentally logging in more than once. So, for 40 people with these limits I would size a cluster that has a total of 25 GB of memory and 12 cores.

## Culling

```
cull:
  timeout: 2400
  every: 600
```

This is used to control how JupyterHub culls idle logins. If the user closes their web browser without logging out of JupyterHub, then their login will be automatically culled every "timeout" seconds (in this case 2400 seconds / 40 minutes). This is checked every "every" seconds - in this case every 600 seconds / 10 minutes.

## Authentication

```
auth:
  type: custom
  custom:
    className: tmpauthenticator.TmpAuthenticator
```

This sets the method used to log into JupyterHub. I've set things up to use `TmpAuthenticator`. This generates a new login for every user, i.e. there are no usernames or passwords. This is easiest for a workshop, as it means I can supply just the URL for the workshop, and not have to worry about setting up user accounts or passwords. It obviously has the problem that anyone who knows the login URL can log in. I've not found this to be an issue, even though I leave my login URLs up on public websites.

If you want to use a proper authentication system, then JupyterHub supports a range of options, from OATH to LDAP. Full details are provided in the [Zero to JupyterHub Authentication Guide](https://zero-to-jupyterhub.readthedocs.io/en/latest/authentication.html).

## Updating your JupyterHub service

If you make any changes to `values.yaml` you need to update your JupyterHub service. You do this by typing;

```
$ helm upgrade workshop jupyterhub/jupyterhub --timeout=3600 --version=v0.6 -f values.yaml
```

This upgrades your workshop in the background, meaning it won't affect existing user sessions. It may take about 10 minutes for everything to update, during which time new logins may fail or be delayed.

## Scaling your kubernetes cluster

Kubernetes is great because you can dynamically scale up or down the number of nodes in your cluster. This means that you have a small cluster of just 1-2 nodes most of the time, which you can then scale up to a large cluster during your workshop. You scale your cluster to use 3 nodes using the command;

```
$ az aks scale --resource-group rseworkshop --name jupyter --node-count 3
```

It will take some time (about 10 minutes) to scale your cluster. Have a go at both increasing the number of nodes and decreasing the number of nodes. You can follow the progress of the scale command using kubectl, e.g.

```
$ kubectl get nodes
```

will print out the nodes in your cluster, including their state (spinning up or shutting down)

***

# [Previous](part07.md) [Up](../README.md) [Next](whatnext.md)

