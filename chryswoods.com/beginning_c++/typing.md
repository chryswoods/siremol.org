
# Types, Scopes and Auto

You have now seen how the basic syntax for C++ compares to what you know 
of Python. Where C++ differs is that it is strongly typed,
and has strict and clear variable scoping rules. In this page, you will
see what this means, and will see how it changes the way you write C++
compared to writing Python.

## Types

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

   //fails as we cannot convert a string to an integer
   a = "Cat";

   //fails as we cannot declare 'a' twice
   std::string a = "Cat";

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

It is not possible for a variable to change type within a function. However, it is possible for the data held in a variable to be converted so that it can be held by a variable of another type. This is known as type conversion. Simple cases of type conversion are automatically converting an integer to a float, or a float to a double. More complex cases are automatically converting a float to an integer, as in these cases, data may be lost (e.g. the floating point number may need to be rounded).

You can examine type conversion by copying the below source code into `convert.cpp`.

```c++
#include <iostream>

int main()
{
    // set up the initial values
    int a = 42;
    float b = 3.141;
    double c = 1.0e50;  // 1 * 10^50

    std::cout << "Original values" << std::endl;
    std::cout << a << " " << b << " " << c << std::endl;

    // safe conversions - no loss of data as converting
    // to a type that supports a wider range of values
    float a1 = a;
    double b1 = b;

    std::cout << "Safe conversions" << std::endl;
    std::cout << a1 << " " << b1 << " " << c << std::endl;

    // unsafe conversions - potential loss of data
    // as converting to a type that supports a narrower 
    // range of values
    int b2 = b;
    float c2 = c;

    std::cout << "Unsafe conversions" << std::endl;
    std::cout << a << " " << b2 << " " << c2 << std::endl;

    return 0;
}
```

Compile and run the above program and examine the output. How have the unsafe narrowing 
conversions changed the saved values?

***

## Variable scopes

A variable in C++ must be assigned a type, which cannot change for the lifetime of that variable. The lifetime of a variable is defined by its scope. A variable's scope is the area of the program in which the variable is visible and accessible.

Scope is controlled using the curly brackets `{  }`. Any variable declared within a set of curly brackets is only visible from within those brackets (and within any brackets nested within). The variable is not visible and does not exist outside the brackets.

Copy the below example into `scope.cpp`;

```c++
#include <iostream>

int main()
{
    //declare 'a' - this is visible from this point in
    //the program onwards, until the closing '}' of main()
    int a = 84;

    if (a == 84)
    {
        // a is visible here, as this is a nested scope of main()
        std::cout << "a = " << a << std::endl;

        // declare 'b' - this is visible from this point in
        // the program onwards, until the closing '}' of this
        // if statement (the end of the if statement's scope)
        int b = 102;

        std::cout << "b = " << b << std::endl;
    }

    // we have now left the scope of the if statement. This means
    // that 'b' no longer exists and is not visible here.

    // if you uncomment this code, it is an error
    // std::cout << "b = " << b << std::endl;

    // however, 'a' is still visible as it was declared in the
    // scope of 'main()' and we are still in this scope
    std::cout << "a = " << a << std::endl;

    return 0;
}
```

Compile and run this code. You should see that it prints out `a = 84`, `b = 102` and `a = 84`.

This program has two main scopes;

* the scope of the `main()` function, which extends between the curly brackets that contain all of the code of the main function, and
* the scope of the `if (a == 84)` statement, which extends between the curly brackets that contain all of the code executed within the if statement.

The scope of the if statement is nested within the scope of the main function. This means that any variable declared in `main()` is also visible within the scope of the if statement. However, variables declared within the scope of the if statement are not visible within the scope of main. This means that `a` can be seen within the if statement, but `b` cannot be seen within the main function. To test this, uncomment the line that is indicated in `scope.cpp` and try to compile again. You should see an error that is something like;

```
scope.cpp:26:28: error: use of undeclared identifier 'b'
    std::cout << "b = " << b << std::endl;
                           ^
1 error generated.
```

A variable exists and is visible from the point it is declared to the end of the scope in which it is contained. Every set of curly brackets defines a scope. This means that functions have their own scope, as do for loops. One interesting and useful feature is that variables declared in the initialiser of the for loop exist only in the scope of the for loop. This means that the iterator variable is created for, and exists only within the for loop. For example;

```c++
#include <iostream>

int main()
{
    // 'i' is declared in the initialiser of the for loop
    // so only exists within the scope of the for loop
    for (int i=0; i<10; ++i)
    {
        std::cout << "i = " << i << std::endl;
    }

    // we are now outside the scope of the for loop so 'i'
    // no longer exists. The below line will cause a compiler error
    std::cout << "i does not exists here? " << i << std::endl;

    return 0;
}
```

You can use scope to create global variables (although these are not really recommended).
This is because the file itself is a scope. For example, copy the below into `global.cpp`;

```c++
#include <iostream>

// global variable as it is in the file scope
int a = 35;

/* Function to add the passed value to 'a' */
int add(int x)
{
    //create 'b' which is local to the scope of 'add'
    int b = 35;

    return a + b + x;
}

int main()
{
    for (int i=0; i<10; ++i)
    {
        int c = add(i);

        std::cout << "c = " << c << std::endl;
    }

    // we can see 'a' as it is in the file scope
    std::cout << "a = " << a << std::endl;

    // we cannot see 'b' as it is in the scope of the function 'add'
    // std::cout << "b = " << b << std::endl;

    // we cannot see 'i' or 'c' here as they are in the scope
    // of the for loop
    // std::cout << "i = " << i << std::endl;
    // std::cout << "c = " << c << std::endl;

    return 0;
}
```

Compile and run the code. In this case we have four variables;

* 'a' : this is declared in the file scope. It exists and is usable from the line it is declared until the end of the file.
* 'b' : this is declared in the `add` function scope. It exists and is usable from the line it is declared until the end of the `add` function scope.
* 'c' and 'i' : these are declared within the scope of the for loop that is nested within the scope of the `main` function. They exist and are usable from the line they are declared until the end of the for loop scope.

### Hiding variables

A variable can be declared once and once only within a scope. However, variables with different names in different scopes are different variables. For example;

```c++
#include <iostream>

int func()
{
    //declare 'a' as local to func()
    int a = 315;

    return a;
}

int main()
{
    int a = 10;

    std::cout << "main's 'a' is " << a << std::endl;
    std::cout << "func's 'a' is " << func() << std::endl;

    return 0;
}
```

In the above example we have declared two different variables, that both happen to be called `a`. The first is the variable `a` that is declared in the scope of the function `func`. The second is the variable `a` that is declared in the scope of `main`. These are different variables, so it is not an error that they have the same name.

So what about nested scopes? What happens if we try to use the same variable name in a pair of nested scopes? Copy the below code into `nestedscopes.cpp`;

```c++
#include <iostream>

int main()
{
    int a = 105;

    for (int i=0; i<10; ++i)
    {
        int a = 3;
        std::cout << "a = " << a << std::endl;
    }

    std::cout << "a = " << a << std::endl;

    return 0;
}
```

What do you expect to see when you compile and run this program?

Compile and run using

```
g++ nestedscopes.cpp -o nestedscope
./nestedscopes
```

What do you see? Is it what you expected?

What you should see is `a = 3` printed 10 times, followed by `a = 105`. This is because the `a` in the for loop is a different variable to the `a` in the main function. Because the two variables have the same name, the `a` in the for loop hides the `a` in the main function. This is something that can cause confusion when you are new to C++. In general, you should avoid declaring variables in nested scopes that have the same name as variables in their parent scopes.

***

## auto

As described above, every variable in C++ must be declared once, together with its type. The variable then exists with that type from the line it is declared until the closing curly bracket of the scope in which it is contained (or the last line of the file if it is in the file scope).

Declaring the type of a variable is sometimes annoying, especially if the type is easily deduced from the value against which it is assigned. To make things easier (and save you typing) the C++ 2011 standard (c++11) introduced the `auto` keyword. If you declare a variable as `auto`, then the compiler will automatically work out the type of the variable based on the value to which it is first assigned. For example, copy the below into `auto.cpp`;

```c++
#include <iostream>

double square(double x)
{
    return x * x;
}

int sum(int a, int b)
{
    return a + b;
}

int main()
{
    //r is automatically declared as a 'double' as the compiler
    //can see that 'square' returns a double
    auto r = square(5.3);

    //s is automatically declared as a 'int' as the compiler
    //can see that 'sum' returns an int
    auto s = sum(4, 7);

    //t is automatically declared as a 'float' as the value on the
    //right hand side of '=' is a float
    auto t = 3.141;

    std::cout << "r = " << r << std::endl;
    std::cout << "s = " << s << std::endl;
    std::cout << "t = " << t << std::endl;

    //note that you can't change the type of an 'auto' variable. Like
    //all other variables, it can only be declared once. The below
    //line is an error
    //auto r = sum(10,12);

    return 0;
}
```

Compile and run this program using

```
g++ --std=c++11 auto.cpp -o auto
./auto
```

(note that we have added `--std=c++11` as `auto` was introduced in the c++11 standard. This should not be needed on newer C++ compilers)

As you should see, the types of `r`, `s` and `t` are correctly, and automatically, deduced by the compiler as being double, int and float.

Note that the use of `auto` does not change the rule that a variable can be declared only once within a scope. You cannot use `auto` to try to redeclare a variable with a different type. For example, the line of code at the end of the above example attempts to redeclare `r` from a double to an int. Uncomment this line and try to compile again. You should see an error that looks something like;

```
auto.cpp:34:10: error: redefinition of 'r'
    auto r = sum(10,12);
         ^
auto.cpp:17:10: note: previous definition is here
    auto r = square(5.3);
         ^
1 error generated.
```

***

# [Previous](syntax.md) [Up](README.md) [Next](lists.md)  
