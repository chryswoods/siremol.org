# Step 2 - Finding all of your dependencies

In the [last lesson](part01.md) you were provided with an example workshop. To prepare this workshop to run on the cloud, we first need to find out what is needed to run it on someone else's computer, i.e. we need to create the list of dependencies of this workshop.

As this is a Python 3 workshop, the first dependency is a good Python 3 environment.

The next dependency is `qcode` itself. We can install that using the command;

```
$ pip install qrcode[pil]
```

Run the above command and you should see output...

```
Collecting qrcode[pil]
  Downloading https://files.pythonhosted.org/packages/79/be/11999004f7e6e5db0fa410c2feacd67c07f472f4500fde0026101f31d0df/qrcode-6.0-py2.py3-none-any.whl
Requirement already satisfied: six in /home/workshops/Cownie/miniconda3/envs/idp/lib/python3.6/site-packages (from qrcode[pil])
Collecting pillow; extra == "pil" (from qrcode[pil])
  Downloading https://files.pythonhosted.org/packages/d1/24/f53ff6b61b3d728b90934bddb4f03f8ab584a7f49299bf3bde56e2952612/Pillow-5.2.0-cp36-cp36m-manylinux1_x86_64.whl (2.0MB)
    100% |████████████████████████████████| 2.0MB 838kB/s 
Installing collected packages: pillow, qrcode
Successfully installed pillow-5.2.0 qrcode-6.0
You are using pip version 9.0.1, however version 18.0 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```

Now you can test the workshop. Move through all of `lesson01.ipynb`. Does it all now work?

## Exercise

Work through the rest of the workshop and see if there are any more dependencies. If there are, then find the commands to install the dependencies, install them, and then make sure that you can work through the entire workshop witout error.

If you get stuck, the full list of dependencies is given in the [next lesson](part03.md)

***

# [Previous](part01.md) [Up](../README.md) [Next](part03.md)

