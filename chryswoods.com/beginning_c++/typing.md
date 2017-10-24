
# Typing

The type of a variable specifies what class of data the variable can hold. For example;

```c++
#include <string>

int main()
{
    // This is an integer variable. It can only hold integers
    int a = 42;

    // This is a float variable. It can only hold floats
    float b = 3.141;

    // This is a string variable. It can only hold strings.
    std::string c = "Hello World";

    // We can change the data in 'a' to be a different integer
    // (you don't specify the type again)
    a = 15;    

    return 0;
}
```

In this example there are three variables;

* `a` is an integer variable, which contains the integer data `42` at the beginning
of the program, but which is changed to contain the integer `15` at the end of the program
* `b` is a float variable, wich contains the float data `3.141`
* `c` is a string variable, which contains the string data `Hello World`

Every variable in C++ has a type, which must be specified the first time the variable is declared. The type of the variable must only be specified once, and cannot change during the program. This is different to Python, which allows a variable to change its type at any time. For example, the below is valid Python...

```python
a = 42
a = 15
a = "Cat"
```

but the equivalent in C++ is not permitted, e.g.

```c++
#include <string>

int main()
{
   int a = 42;
   a = 15;
   a = "Cat";
   return 0;
}
```

Create a source file called `broken.cpp` and try to compile the above incorrect C++ code. What error message do you get? On my computer, I get the error

```
broken.cpp:7:6: error: assigning to 'int' from incompatible type 'const char [4]'
   a = "Cat";
     ^ ~~~~~
1 error generated.
```

The compiler here is complaining that you cannot assign text data (const char [4]) into a variable which has integer type.

## Type conversion

It is not possible for a variable to change type during a program. However, it is possible for the data held in a variable to be converted so that it can be held by a variable of another type. This is known as type conversion. Simple cases of type conversion are automatically converting an integer to a float, or a float to a double. More complex cases are automatically converting a float to an integer, as in these cases, data may be lost (e.g. the floating point number may need to be rounded).

You can examine type conversion by copying the below source code into `convert.cpp`.

```c++
#include <iostream>

int main()
{
    // safe conversions - no loss of data...


    // unsafe conversions - potential loss of data...
}
```

## Variable scopes

Variables have scope. Variables exist only in scope. Cannot have two variables with the 
same name in the same scope. Variables declared in an inner scope hide the variables
in the outer scope. Not to be recommended...

## auto

The auto keyword can automatically determine the type of a variable. Very useful.

***

# [Previous](syntax.md) [Up](README.md) [Next](lists.md)  
