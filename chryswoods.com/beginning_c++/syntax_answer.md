#Basic Syntax: Answer to exercise

timestable.h
```c++
#ifndef _TIMESTABLE_H
#define _TIMESTABLE_H

/* Function to print 'x' times table from 1*i to n*i
   to the screen */
void timestable(int x, int n);

#endif
```

timestable.cpp
```c++

#include <iostream>

#include "timestable.h"

void timestable(int x, int n)
{
    for (int i=1; i<=n; ++i)
    {
        std::cout << i << " times " << x
                  << " equals " << (i*x) << std::endl;
    }
}
```

***

# [Previous](syntax.md) [Up](syntax.md) [Next](syntax.md)
