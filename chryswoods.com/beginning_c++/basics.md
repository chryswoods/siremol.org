
# C++ Basics

You write C++ using a simple text editor, like `nano`. Open a command prompt and use a text editor to open a file called `hello.cpp`, e.g.

```
nano hello.cpp
```

C++ source files traditionally end in `.cpp`. This isn't a requirement, but it does make it easier to recognise the file.

Now type the following into the file;

```c++
#include <iostream>

int main()
{
    std::cout << "Hello from C++" << std::endl;

    return 0;
}
```

Save the file. You have just written a simple C++ program! C++ is a compiled programming language, meaning that we now need to compile the C++ source file you have just written to create an executable program that you can run.

To compile your C++ source file, type;

```
g++ hello.cpp -o hello
```

This will use your C++ compiler (in this case `g++`) to compile your C++ source file (`hello.cpp`) to create a new executable program called `hello`. You can run the program by typing

```
./hello
```

You should see that this prints out `Hello from C++`. If so, then congratulations as you have now written, compiled and run your first C++ program.

This was a simple program. C++ is a language designed to help you write powerful and full-featured programs, and as such, it is a large language with a lot of concepts and features.

This program introduced some of the basic building blocks of C++;

* The `main` function. All C++ programs must have a function called `main`. This is the function that is 
executed when you start the program.
* A command `std::cout`. Commands are instructions to tell C++ to do something, in this case to print the passed
  strings to the screen.
* A string `Hello from C++`. A string is just a piece of text. Strings are always enclosed in either double quotes or single quotes.
* A line of code `std::cout << "Hello from C++!" << std::endl;`. A line of code forms a complete instruction which will be executed by the C++ program. The C++ program executes each line of code, one at a time in order, from the first line of the `main` function to the last. Note that every line of code must end with a semicolon.
* A header file `iostream`. This contains a set of functions, classes and objects that extend C++. In this case, the header file `iostream` is part of the standard C++ library, and provides here `std::cout` and `std::endl`. These objects are used for printing text to the screen.

In C++ you use `std::cout` to print text to the screen. It is an object provided by the C++ standard library (hence the `std::` before the name). You use it to print things to the screen using the `<<` operator. For example, use a text editor to write a new C++ source file called `variables.cpp`

```
nano variables.cpp
```

Type into the source file the following lines;

```c++
#include <iostream>
#include <string>

int main()
{
    std::string a = "Hello";
    std::string b = "from";
    std::string c = "C++!";

    std::cout << a << " " << b << " " << c << std::endl;

    return 0;
}
```

What do you think will be printed when you compile and run this program? Have a go by typing;

```
g++ variables.cpp -o variables
./variables
```

Did you see what you expected? In this program we created three variables of type `std::string`, called `a`, `b` and `c`. 
The line `std::string a = "Hello";` sets the variable `a` to type `std::string` and sets it equal to the string `Hello`.
The next lines set `b` equal to `from` and `c` equal to `C++!`.

The three variables are printed to the screen using `std::cout`. They are printed by pushing them into `std::cout` 
using its `<<` operator. We push the value of `a` first (printing 'Hello' to the screen). We follow this
with a space, before pushing the value of `b`, then a space, then the value of `c`. We finish by pushing
`std::endl`, which represents the end of line character (`\n` on Linux/OS X or `\r\n` on Windows).

Note that `a`, `b` and `c` are all of type `std::string`. This type is provided in the `string` header
file that is included at the top of the script. Also note that every complete line of code ends with 
a semicolon. C++ uses semicolons to separate different lines, and (mostly) ignores actual line breaks. This
means that you could write the above program as a small number of real lines of text, e.g.

```c++
#include <iostream>
#include <string>
int main(){ std::string a = "Hello"; std::string b = "from"; std::string c = "C++!"; std::cout << a << " " << b << " " << c << std::endl; return 0; }
```

While you could write the program as a small number of lines, it makes it difficult to read and is not recommended. 
It is therefore good practice to write only one line of code per line of text, i.e. finish every line of code
with a semicolon and a newline (return).

As you can see, in C++ you have to specify the type of every variable. C++ has many different variable types, e.g.

* `int` : Integer (whole number)
* `float` : Floating point number
* `double` : Floating point number that has double the precision of a `float`
* `bool` : Boolean (logical true/false) value
* `std::string` : String (text)

You can use `std::cout` to print out values of any of these variable types, e.g. create a new 
C++ source file called `variables2.cpp` and type into it;

```c++
#include <iostream>
#include <string>

int main()
{
    int a = 42;
    float b = 3.14159265;
    std::string c = "Spot the dog";
    bool d = true;

    std::cout << "Use the '<<' operator to push things to print to std::cout, e.g. " 
              << a << std::endl;

    std::cout << "You can print anything you like, e.g. floats such as " << b << std::endl;
    std::cout << " or other strings, like " << c << " or booleans such as " << d << std::endl
              << "and when you type, you can go over "
              << "multiple lines, as 'std::endl' is used to print an 'end of line'."
              << std::endl;
              
    return 0;
}
```

What do you think will be printed to the screen when you compile and run this program? Do this by typing;

```
g++ variables2.cpp -o variables2
./variables2
```

Did you see what you expected? Play with this program by breaking the text over different source
file lines, and moving the `std::endl` so that the text is printed cleanly to the screen
(e.g. the newlines are placed so that each line printed has about the same length).


***

# [Previous](README.md) [Up](README.md) [Next](syntax.md)  
