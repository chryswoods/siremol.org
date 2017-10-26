
# Objects and Classes

C++ is a strongly typed language, meaning that every variable has to have a defined type. You have
already used standard types, such as `float` and `int`, and some of the types provided by the 
standard library, e.g. `std::string` and `std::vector<>`. However, the real power of C++ is that,
[like Python](../intermediate_python/objects.md), it allows you to create you own types.

First, let us consider this simple class from Python, which was used to implement the 
[GuessGame](../intermediate_python/objects.md).

```python
"""A simple guessing game"""
    
class GuessGame:
    """A simple guess the secret game"""
    def __init__(self, secret):
        """Construct a game with the passed secret"""
        self._secret = secret
        self._nguesses = 0   # the number of guesses
    
    def guess(self, value):
        """See if the passed value is equal to the secret"""
    
        if self._nguesses >= 3:
            print( "Sorry, you have run out of guesses." )
    
        elif value == self._secret:
            print( "Well done - you have won the game!" )
            return True
        else:
            print( "Wrong answer. Try again!" )
            self._nguesses += 1  # increase the number of wrong guesses
            return False
```

We can write an exactly equivalent class using C++. Create a new file called `guessgame.h`
and copy in the following;

```c++
#ifndef _GUESSGAME_H
#define _GUESSGAME_H

/* A simple guess the secret game */
class GuessGame
{
public:
    /* Construct the game with the passed secret */
    GuessGame(int secret);

    /* See if the passed value is equal to the secret */
    bool guess(int value);

private:
    /* The secret that will be guessed */
    int _secret;

    /* The number of guesses */
    int _nguesses;
};

#endif
```

Now create a file called `guessgame.cpp` and copy in the following

```c++
#include "guessgame.h"
#include <iostream>

GuessGame::GuessGame(int secret)
{
    //save the secret
    this->_secret = secret;

    //set the number of guesses to zero
    this->_nguesses = 0;
}

bool GuessGame::guess(int value)
{
    if (this->_nguesses >= 3)
    {
        std::cout << "Sorry, you have run out of guesses." << std::endl;
        return false;
    }
    else if (value == this->_secret)
    {
        std::cout << "Well done - you have won the game!" << std::endl;
        return true;
    }
    else
    {
        std::cout << "Wrong answer. Try again!" << std::endl;
        this->_nguesses += 1;
        return false;
    }
}
```

Finally, create a file called `main.cpp` and copy in the following;

```c++
#include "guessgame.h"

int main()
{
    //create a GuessGame with the 'secret' number 42
    GuessGame g(42);

    //now try a couple of wrong guesses
    g.guess( 12 );
    g.guess( 99 );

    //finally, try the correct guess
    g.guess( 42 );

    return 0;
}
```

Compile and run the program using

```
g++ main.cpp guessgame.cpp -o guessgame
./guessgame
```

The C++ version of GuessGame is equivalent to the Python version, but writing it requires many more lines of code. This
is because in C++ it is good practice to separate the declaration of the class (i.e. its name, what functions it contains,
what data it contains) from its definition (i.e. the code of the functions themselves). 

The declaration of the class is placed into the header file `guessgame.h`. The definition is placed in the source file `guessgame.cpp`.

## Examining guessgame.h

Let's first look at the declaration...

The syntax for declaring a new class is `class NAME { ... };`, where `NAME` is the name of the class. All of the functions
and data that are part of the class should be placed within the curly brackets. Note that, unlike all other situations
you have encountered so far, you need a semicolon after these curly brackets.

The functions and data within a class must be placed within one of two sections;

* `public:` - This section is used for functions and data that are public, meaning that they are visible outside of the class.
* `private:` - This section is used for functions and data that are private, meaning that they can only be seen by functions that are part of the class.

Python has the same concept of "public" and "private" functions and data. In Python, any class variable or class function that starts with an underscore is private (e.g. `self._secret`). All other functions or data are public.

While C++ does not use underscores to decide whether variables or data are private, it is considered good practice to 
use underscores in addition to placing the data in the `private:` section, as it helps you remember which functions
and data are private without having to look at the class's header file.

In the case of `GuessGame`, we have declared two functions (called "member functions") and two pieces of class data (called "member data");

* `_secret` and `_nguesses` are two pieces of integer member data that are declared private to `GuessGame`.
* `bool guess(int value)` is a public member function called `guess` that takes an integer argument and returns a boolean.
* `GuessGame(int secret)` is the public constructor for this class, which takes an integer argument.

Like Python, classes in C++ should have constructors that are used to initalise the member data of the class.

## Examining guessgame.cpp

Now, let's look at the definition of `GuessGame` which is in `guessgame.cpp`.

The definition is where you place the code that does the actual work of the functions of the class. In this case there are two functions. The first one to look at is `guess`;

```c++
bool GuessGame::guess(int value)
{
    if (this->_nguesses >= 3)
    {
        std::cout << "Sorry, you have run out of guesses." << std::endl;
        return false;
    }
    else if (value == this->_secret)
    {
        std::cout << "Well done - you have won the game!" << std::endl;
        return true;
    }
    else
    {
        std::cout << "Wrong answer. Try again!" << std::endl;
        this->_nguesses += 1;
        return false;
    }
}
```

To name a function as being part of a class you need to use the syntax `NAME::function_name`. So, in this case, the `guess` function of `GuessGame` is called `GuessGame::guess`.

Other than the special naming convention, a member function of a class is written in the same way as any normal function.
The arguments are placed in round brackets (e.g. `GuessGame::guest(int value)`) and the return value is specified before
the name (e.g. `bool GuessGame::guess(int value)`). The code for the function is between the curly brackets.

The advantage of a member function over a normal function is that a member function of a class has access to the private 
member data of that class, and can call the private member functions of that class. You gain access to member data
and member functions by using `this->`, e.g. `this->_secret`. This is very similar to Python, with `this->` in C++ being
equivalent to `self.` in Python.

The second function to look at is the constructor;

```c++
GuessGame::GuessGame(int secret)
{
    //save the secret
    this->_secret = secret;

    //set the number of guesses to zero
    this->_nguesses = 0;
}
```

The constructor always has the same name as the class, hence why the name is written twice (`GuessGame::GuessGame`). Like other functions, you can specify arguments between the round brackets. However, constructors are special in that they
don't have a return value. This is why you don't specify a return type as for other functions.

The job of the constructor is to initialise the member data of an object of the class when it is first constructed. In this
case, the constructor is setting the value of `_secret` to the value passed as an argument to the constructor, and it is
initialising the value of `_nguesses` to zero. Note that we have used `this->` to gain access to this data.

## Examining main.cpp

This is (hopefully) the simplest of the source files to understand. In this file we are using the `GuessGame` class.
First, we have to include the header file `guessgame.h` so that the class is available. Then we construct an
object of class `GuessGame` using the syntax

```c++
GuessGame g(42);
```

This creates a new variable, `g`, which is of type `GuessGame`, and which is initialised with the secret value of `42`.
Note, an equivalent way of creating objects of a class is to use the (more Python-like) syntax;

```c++
auto g = GuessGame(42);
```

You call functions of a class in the same way as Python, namely `object.function()`, e.g. `g.guess( 12 )`.

***
# Exercise

Copy the following into the file `persondata.h`

```c++
#ifndef _PERSONDATA_H
#define _PERSONDATA_H

/* The data about a person in the database */
class PersonData
{
public:
    PersonData();

    void setHeight(float height);
    void setWeight(float weight);

    float height();
    float weight();
    float bmi();

private:
    /* The person's height */
    float _height;

    /* The person's weight */
    float _weight;
};

#endif
```

Next, copy the following into the file `main.cpp`

```c++
#include <iostream>
#include <map>
#include <string>
#include <vector>

#include "persondata.h"

int main()
{
    //declare the map that uses a person's name as a key to look
    //up their personal data stored in the PersonData object
    std::map<std::string,PersonData> database;

    //let's first put the data in three vectors
    std::vector<std::string> names = { "James", "Jane", "Janet", "John" };
    std::vector<float> heights = { 1.7, 1.8, 1.5, 1.4 };
    std::vector<float> weights = { 75.4, 76.5, 56.8, 52.0 };

    //now put all of the data into the database
    for (int i=0; i<names.size(); ++i)
    {
        PersonData data;
        data.setHeight( heights[i] );
        data.setWeight( weights[i] );

        database[names[i]] = data;
    }

    //now print out the entire database
    for ( auto item : database )
    {
        //print out the name
        std::cout << item.first << " : ";

        auto data = item.second;

        std::cout << "height=" << data.height()
                  << " weight=" << data.weight()
                  << " bmi=" << data.bmi() << std::endl;
    }

    return 0;
}
```

Your task is to write the file `persondata.cpp` that will provide the definitions of the 
member functions from `persondata.h` that will enable the code in `main.cpp` to run correctly.

When you have finished, compile and run using;

```
g++ --std=c++14 main.cpp persondata.cpp -o persondata
./persondata
```

You should see output;

```
James : height=1.7 weight=75.4 bmi=26.09
Jane : height=1.8 weight=76.5 bmi=23.6111
Janet : height=1.5 weight=56.8 bmi=25.2444
John : height=1.4 weight=52 bmi=26.5306
```

If you get stuck, take a look at this [completed example](objects_answer.md).

***

# [Previous](lists.md) [Up](README.md) [Next](operators.md)  
