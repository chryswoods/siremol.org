# What next?

You've now learned the basics of creating a JupyterHub docker image and then deploying this to a cloud-based JupyterHub kubernetes service running on top of Azure's Kubernetes Service (AKS).

If you want to learn more then I strongly recommend the excellent [Zero to JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/) tutorial. This was the resource I used to learn how to do this (and is the source of many of the more cryptic commands).

You will also likely have to learn how to set up HTTPS if you want to secure your cluster.  This is detailed in the [security](https://zero-to-jupyterhub.readthedocs.io/en/latest/security.html) part of the Zero to JupyterHub guide. This also provides lots of information about more generally securing kubernetes and JupyterHub (remember, you are letting random people run shell commands on your kubernetes servers! - this is one of the reasons I strongly prefer running JupyterHub on the cloud rather than running it locally inside the firewall on an on-premise server)

The JupyterHub I demonstrated is good for workshops, because everything the user does is cleaned up when they log out. This means that all of the files they write are lost, as there is no permanent storage. To learn how to set up persistent storage, then take a look at the [storage guide](https://zero-to-jupyterhub.readthedocs.io/en/latest/user-storage.html#user-storage) to see how to set up kubernetes Persistent Volume Claims (PVCs).

Finally, you should also take a look at the alternatives to running your own JupyterHub kubernetes service. It is necessary when you need to install your own modules, have guarantees of availability, or when your workshop uses more than just Python (e.g. your notebooks are driving other programs as part of, e.g. a computational chemistry workshop).

If you are just running pure python, then you can consider these services which enable you to host pure python notebooks;

* [Binder](https://blog.jupyter.org/binder-2-0-a-tech-guide-2017-fd40515a3a84) - this provides a hosting service for Jupyter notebooks provided by the Jupyter project itself. It allows you to specify dependencies and have them automatically packaged into a docker image that is hosted and launched from Binder.

* [Azure Notebooks](https://notebooks.azure.com) - this is a Jupyter notebook hosting service provided by Microsoft Azure.

Finally, you should also think hard about how to write your Jupyter-notebook-based workshop. You should avoid creating a workshop that just teaches people to press "SHIFT+Return" over and over again. Mix information with python with exercises that ask people to write their own code or run their own commands. A workshop should impart knowledge and make your attendees think and do. It is not a set of cryptic commands that are run one after another in a magic sequence.

Finally, while Jupyter notebooks are great teaching tools, they are a barrier for new programmers. They have a confusing state and are terrible programming development environments. [This excellent talk](https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/mobilepresent?slide=id.g3d168d2fd3_0_159) clearly discusses the limitations of Jupyter notebooks. Put simply, no, Jupyter notebooks are not an IDE, no, they shouldn’t be used to teach beginning python, and no, they shouldn’t be used to package and publish software.

When I teach Python to new users, I teach beginning Python using simple text files and calling Python manually from the command line (e.g. see my [beginner's course here](http://chryswoods.com/beginning_python). I only introduce Jupyter once people understand what Python is, and I use an [Introduction to JupyterHub](https://ccpbiosim.github.io/python_and_data/html/answers/01_jupyter_howto.html) or a short [Beginning Jupyter](https://chryswoods.com/python_and_data/python1/answers_01_jupyter.html) notebook that then teaches Jupyter and JupyterHub itself separately.

Good luck with your workshop!

***

# [Previous](part08.md) [Up](../README.md) [Next](../README.md)

