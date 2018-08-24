# Step 4 - JupyterHub

In the last lesson you learned how to build a docker image that contained all of the software and notebooks needed for the workshop-in-a-workshop. You also learned how to run the container and connect to the workshop.

While this worked, the user experience was not satisfactory. You had to copy and paste an access token, and for this to work, the user has to have docker installed. Ideally, we would like to move this docker container to the cloud. This would enable your learner to simply connect to the cloud-based container from their webbrowser, so will not need docker (or your container image) installed.

The first step to moving to the cloud is we need to prepare the container so that it can be used by multiple learners. To do this, we will use [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/). JupyterHub is a multi-user hub that can spawn, manage and proxy multiple instances of single-user Jupyter notebooks. JupyterHub provides a single server to which learners can connect. When a learner connects, JupyterHub will spin out a new jupyter-notebook kernel, one for each learner, based on the docker container image that you supply.

## Building your JupyterHub image

To get this to work, we need to add JupyterHub to our workshop-in-a-workshop jupyter image. This is a little complex. To make it easier, JupyterHub provides a range of base images. I have modified this to generate the below Dockerfile to build a JupyterHub container for the workshop-in-a-workshop. This can be found in the in the [`jupyterhub`](jupyterhub) directory.

```
# Based on the JupyterHub docker image that is
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
# Ubuntu 16.04 (xenial) from 2017-07-23
# https://github.com/docker-library/official-images/commit/0ea9b38b835ffb656c497783321632ec7f87b60c

# This has been extensively modified by C.Woods, so blame him
# for any errors or problems

# Start from ubuntu :-)
FROM ubuntu@sha256:84c334414e2bfdcae99509a6add166bbb4fa4041dc3fa6af08046a66fed3005f

LABEL maintainer="Christopher Woods <Christopher.Woods@bristol.ac.uk>"

USER root

# Install all OS dependencies for notebook server that starts but lacks all
# features (e.g., download as all possible file formats)
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get -yq dist-upgrade \
 && apt-get install -yq --no-install-recommends \
    git \
    sudo \
    locales \
    ca-certificates \
    fonts-liberation \
    wget \
    bzip2 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen

# Install Tini - this is a tiny init system that is useful
# for containers that need to start many processes
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.10.0/tini && \
    echo "1361527f39190a7338a0b434bd8c88ff7233ce7b9a4876f3315c22fce7eca1b0 *tini" | sha256sum -c - && \
    mv tini /usr/local/bin/tini && \
    chmod +x /usr/local/bin/tini

# Configure environment
ENV CONDA_DIR=/opt/conda \
    SHELL=/bin/bash \
    NB_USER=jovyan \
    NB_UID=1000 \
    NB_GID=100 \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

ENV PATH=$CONDA_DIR/bin:$PATH \
    HOME=/home/$NB_USER

ADD fix-permissions /usr/local/bin/fix-permissions

# Create jovyan user with UID=1000 and in the 'users' group
# and make sure these dirs are writable by the `users` group.
RUN useradd -m -s $SHELL -N -u $NB_UID $NB_USER && \
    fix-permissions $HOME

# Install a mini anaconda for Python 3. This is needed as
# JupyterHub is best installed from conda
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    chmod a+x miniconda.sh && \
    ./miniconda.sh -b -p /opt/conda && \
    chown -R $NB_USER:$NB_GID /opt/conda && \
    fix-permissions /opt/conda && \
    rm miniconda.sh

# Configure container startup. This starts the tini init system
# telling it to run the start_notebook.sh as the primary process.
# This is a script provided by JupyterHub that will start different
# processes depending on whether this is the hub or a notebook
ENTRYPOINT ["tini", "--"]
CMD ["start-notebook.sh"]

# Make sure that the jupyter notebook port is accessible from
# outside the container
EXPOSE 8888

# Now copy in all of the files that are needed to run JupyterHub
# This includes jupyter-notebook_config.py that is used to
# configure the jupyterhub server
COPY start.sh /usr/local/bin/
COPY start-notebook.sh /usr/local/bin/
COPY start-singleuser.sh /usr/local/bin/
COPY jupyter_notebook_config.py /etc/jupyter/
RUN fix-permissions /etc/jupyter/

# Do all conda work as $NB_USER
USER $NB_USER
WORKDIR $HOME

# Install Jupyter Notebook and Hub and other useful packages
RUN conda config --system --prepend channels conda-forge && \
    conda config --system --set auto_update_conda false && \
    conda config --system --set show_channel_urls true && \
    conda install --quiet --yes 'notebook=5.2.*' 'jupyterhub=0.8.*' 'jupyterlab=0.31.*'

# Now install the dependencies of our workshop
RUN pip install qrcode[pil] && \
    pip install git+git://github.com/ojii/pymaging.git#egg=pymaging && \
    pip install git+git://github.com/ojii/pymaging-png.git#pymaging-png

# Now installed tmpauthenticator. This is a module that allows anybody
# to log into this jupyterhub using a hidden URL
RUN pip install jupyterhub-tmpauthenticator

# Reinstall an older version of tornado as tornado 5 doesn't work
# with the current version of jupyterhub
# Also clean up after conda, including clearing the cache
RUN conda install tornado=4.5.3 && \
    conda clean -tipsy && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    fix-permissions $CONDA_DIR && \
    rm -rf $HOME/.cache $HOME/.jupyter $HOME/.local/share/jupyter

# Add all of the workshop files to the home directory
ADD example_workshop/lesson*.ipynb $HOME/

# End as the User to make sure that we don't
# accidentally run the container as root
USER $NB_USER
```

Before we build this image, we should clean out all old docker images. This saves space, particularly if you are running this as part of the RSE workshop, for which disk space is very limited. The below command will remove all unused and untagged docker image containers;

```
$ docker system prune -a
```

We need at least 1 GB of free space, so you may need to also delete other workshops, e.g. choose a workshop that takes up a lot of space a which you are not attending and remove that;

```
$ rm -rf /home/workshops/Cownie
```

You can build the image using

```
$ cd jupyterhub
$ docker build . -t workshop-hub
```

This build will take a while and will create a docker container that is tagged as "workshop-hub". You can see this image using

```
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
workshop-hub        latest              9a3dd661420c        5 seconds ago       1.09GB
ubuntu              <none>              14f60031763d        12 months ago       120MB
```

You can now run the container using the command

```
$ docker run workshop-hub -p 8888:8888
Executing the command: jupyter notebook
[I 11:12:15.753 NotebookApp] Writing notebook server cookie secret to /home/jovyan/.local/share/jupyter/runtime/notebook_cookie_secret
[W 11:12:16.356 NotebookApp] WARNING: The notebook server is listening on all IP addresses and not using encryption. This is not recommended.
[I 11:12:16.393 NotebookApp] JupyterLab beta preview extension loaded from /opt/conda/lib/python3.6/site-packages/jupyterlab
[I 11:12:16.393 NotebookApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
[I 11:12:16.397 NotebookApp] Serving notebooks from local directory: /home/jovyan
[I 11:12:16.397 NotebookApp] 0 active kernels
[I 11:12:16.397 NotebookApp] The Jupyter Notebook is running at:
[I 11:12:16.397 NotebookApp] http://[all ip addresses on your system]:8888/?token=09f92d061506b98662a24213d53d42677176bede8ca66378
[I 11:12:16.398 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 11:12:16.398 NotebookApp] 
    
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=09f92d061506b98662a24213d53d42677176bede8ca66378
```

You should see similar output as above, including the link at the bottom that you can use to connect to the workshop. Copy the link and paste it into your web browser.

## Exercise

Check through the lessons in your workshop and make sure that they all work.


***

# [Previous](part03.md) [Up](../README.md) [Next](part05.md)

