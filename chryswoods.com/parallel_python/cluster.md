# Running Scoop on a Cluster

Scoop uses SSH to connect to and communicate between computers in a cluster.
This means that you must have set up passwordless connections between the 
computer on which you submit the job and the computers on which the worker
processes will be running. This is described in full in the 
[Scoop install guide](http://scoop.readthedocs.org/en/latest/install.html#remote-usage).
This has normally be done for you automatically if you are running on an
HPC cluster.

You specify which computers to use for your job using a host file. This
contains a list of hostnames of the machines that will be used, e.g.
it could be a file called `hostfile` that contains

```
node001-01 4
node001-02 12
node001-03 2
```

This (fictional) hostfile will tell Scoop to run the script using
four workers on computer `node001-01`, twelve workers on `node001-02`
and two workers on `node001-03`.

You pass this hostfile to Scoop via the command line when you call
the script, using the `--hostfile` argument, e.g.

```
python -m scoop --hostfile hostfile script.py
```

## Running using a Cluster Scheduler

Scoop comes with in-built support for many cluster schedulers, e.g.
Sun Grid Engine (SGE), Torque (PBS-compatible, Moab, Maui) and SLURM. 
That means that a Scoop automatically recognises the nodes assigned to your task
without you needing to specify a hostfile.

***

# [Previous](mapreduce_part3.md) [Up](part3.md) [Next](whatnext.md)
