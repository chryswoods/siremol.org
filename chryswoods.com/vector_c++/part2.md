
# Part 2: Vectorisation using Intrinsics

A more direct, but more difficult, way of vectorising your code
is to use vector intrinsics. Intrisics provide data types
for vectors (i.e. `__m128 a;` would declare the 
variable `a` to be a vector of 4 floats). They also provide functions
that operate directly on vectors (i.e. `_mm_add_ps(a,b)` would
add together the two vectors `a` and `b`).

Working directly with intrinsics means that you have taken
responsibility for vectorising your code. The advantage is that
you can be confident that any compiler will produce roughly similar
output, and that you have complete control of what is vectorised
and how. This makes it easier to achieve performance portability,
as you know that your code should run at a similar speed regardless
of the compiler used. However, a major disadvantage is that the 
intrinsic data types and functions are specific for a particular
processor and vectorisation architecture. For example `__m128 a` is
specific to SSE, meaning the code will only run on processors
that support SSE. This means that the gain of performance 
portability comes with a loss of code portability.

In this part of the workshop you will learn about the vector
intrinsics available to support SSE and AVX. You will also
learn how to write code that uses intrinsics, but remains
code portable (i.e. will still run on computers that don't
support SSE or AVX).

* [SSE Intrinsics](emmintrin.md)
* [AVX Intrinsics](immintrin.md)
* [Portable vectorisation](portable.md)
* [What next?](whatnext.md)

***

# [Previous](README.md) [Up](README.md) [Next](emmintrin.md)

