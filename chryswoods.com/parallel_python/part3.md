# Part 3: Multinode (distributed/cluster) Parallel Programming

Python comes with built-in support for parallelising scripts locally
over the compute cores of a single computer. However, as yet, there
is no in-built support for parallelising scripts over the nodes
of a cluster, e.g. distributed parallel programming.

Fortunately, there are several third party libraries that are 
beginning to appear that support distributed clusters. Most of these
are based on the concepts of mapping, asynchronous functions,
futures, and functional programming, so you should find that the 
concepts you have learned in parts 1 and 2 will be useful as you 
explore the developing ecosystem of distributed parallel
Python libraries.

In this part, we will take a quick look at one such library,
called Scoop.

 * [Scoop](scoop.md)
 * [Distributed map/reduce](mapreduce_part3.md)
 * [Running Scoop on a Cluster](cluster.md)
 * [What Next?](whatnext.md)

***

# [Previous](async_map.md) [Up](README.md) [Next](scoop.md)

