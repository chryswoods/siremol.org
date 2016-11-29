
# Part 2: Portable Intrinsics

For portability, you should hide use of intrinsics behind `#ifdef` guards, and
provide a scalar fallback if, e.g. SSE or AVX are not available. There are some
libraries that can help, e.g. Intel's math kernel library etc. etc.

Also, look at `MultiFloat` and `MultiDouble` from the Sire package, as
this creates a `MultiFloat` class that holds a vector of floats, and 
manipulates them in a C++-friendly way.

***

# [Previous](immintrin.md) [Up](part2.md) [Next](whatnext.md)
