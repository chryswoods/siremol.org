
# Concepts, Default Arguments and Operators

C++ enables you to create new types that correspond to key concepts in your 
program. For example, you created the `PersonData` class to represent the 
concept of personal data of a person. This enabled you to write a program that worked
with people's data via a `PersonData` concept, rather than working with floating point numbers at arbitrary keys in a map.

## Concepts

Representing concepts in your program with classes is a powerful way to 
make your program easier to understand and develop. It also makes it easier
to catch and fix errors. For example, copy the below code into `weight.cpp`.

```c++
#include <iostream>

/* A simple class used to represent a person's weight.
   This ensures that the weight cannot be below zero */
class Weight
{
public:
    Weight(float w=0);

    float value();

private:
    float _weight;
};

Weight::Weight(float w)
{
    if (w > 0)
    {
        this->_weight = w;
    }
    else
    {
        this->_weight = 0;
    }
}

float Weight::value()
{
    return this->_weight;	
}

int main()
{
    //default construct the weight
    Weight w1;

    //construct the weight with a valid value
    Weight w2(55.3);

    //construct the weight with an invalid value
    Weight w3(-10.0);

    std::cout << w1.value() << " "
              << w2.value() << " "
              << w3.value() << std::endl;

    return 0;
}
```

Compile and run using

```
g++ weight.cpp -o weight
./weight
```

You should see printed out;

```
0 55.3 0
```

So, what is happening here? First, we have created the concept of a weight, 
which is being represented using the `Weight` class. A weight differs from a 
normal number in that it is not possible to have a negative weight. This
is checked (and if necessary fixed) in the constructor;

```c++
Weight::Weight(float w)
{
    if (w > 0)
    {
        this->_weight = w;
    }
    else
    {
        this->_weight = 0;
    }
}
```

The code in the constructor checks to see if the passed weight is greater than zero. If it is, then this is a valid value, so is saved as `this->_weight`. Otherwise, an invalid weight has been passed, and so `this->_weight` is initialised to zero.

This means that the line;

```c++
    //construct the weight with an invalid value
    Weight w3(-10.0);
```

catches that `-10.0` is an invalid weight, and automatically sets the weight `w3` equal
to zero.

***

## Default Arguments

An interesting feature of this class is that we are using a default-initialised value as the argument, i.e.

```c++
Weight(float w=0);
```

You can use default-initialised values to provide a default value of an argument in case it is not passed to the function. In this case, if an argument is not supplied, then a default value of `0` is used. This is why the line

```c++
    //default construct the weight
    Weight w1;
```

set the value of `w1` to a weight of 0.

Default-initialised arguments can be used with any function, regardless of whether it
is a member function, constructor or normal function. For example;

```c++
#include <iostream>

float sum(float x=0, float y=1, float z=2)
{
    std::cout << "Add " << x << " to " << y 
              << " to " << z << std::endl;

    return x + y + z;
}

int main()
{
    auto a = sum();         // a = sum(0, 1, 2);
    auto b = sum(10);       // b = sum(10, 1, 2);
    auto c = sum(31,40);    // c = sum(31, 40, 2);
    auto d = sum(19,13,17); // d = sum(19, 13, 17);

    std::cout << a << " " << b << " "
              << c << " " << d << std::endl;

    return 0;
}
```

Default-initialised arguments make it easy to use functions that have
lots of arguments. Note that the default value is given in the 
declaration of the function (or class member function), not in the definition.
Also note that if you supply a default argument to the ith argument, then
you must supply default values to all arguments that follow, e.g.

```c++
//this is ok - default value given to 3rd argument,
//so need to supply one to 4th and 5th
int ok_defaults(int a, int b, int c=5, int d=1, int e=6)
{
    return a + b + c + d + e;
}

//this is broken - you cannot have an argument that doesn't have
//a default value after an argument that does...
int broken_defaults(int a, int b, int c=5, int d, int e)
{
    return a + b + c + d + e;
}

int main()
{
    return 0;
}
```

When I try to compile the above code I get the error;

```
broken.cpp:10:48: error: missing default argument on parameter 'd'
int broken_defaults(int a, int b, int c=5, int d, int e)
                                               ^
broken.cpp:10:55: error: missing default argument on parameter 'e'
int broken_defaults(int a, int b, int c=5, int d, int e)
                                                      ^
2 errors generated.
```

***

## Operators

The above `Weight` class captures the concept of a weight. However, it is very basic,
and doesn't include simple features of the concept, such as the ability to 
add two weights together.

In reality, you can add one weight to another, and subtract one weight from another.
Equally, it should not be possible to add a height to a weight (e.g. if there
was a `Height` class the represented the concept of height).
 
For our class `Weight` to match this concept, we have to add code to support things
like;

```c++
int main()
{
    Weight c;

    // it should be possible to add a weight
    c = c + Weight(8.0);

    // it should also be possible to subtract a weight
    c = c - Weight(3.4);

    // we want the below code to raise a compiler error
    // as it should not be possible to add a height to a weight
    c = c + Height(1.8);

    return 0;
}
```

C++ provides operators as a way to support such code. Operators are functions that
are added to classes to specify what code should be used when we operate on them
with other classes. There are several operators that can be specified, for example
key operators are;

* `operator+` : addition, e.g. `Weight Weight::operator+(Weight other)`
* `operator-` : subtraction, e.g. `Weight Weight::operator-(Weight other)`
* `operator*` : multiplication, e.g. `Weight Weight::operator*(float other)`
* `operator/` : division, e.g. `Weight Weight::operator/(float other)`
* `bool operator==` : comparison equals to, e.g. `bool Weight::operator==(Weight other)`
* `bool operator!=` : not equal to, e.g. `bool Weight::operator!=(Weight other)`
* `bool operator<` : less than, e.g. `bool Weight::operator<(Weight other)`
* `bool operator<=` : less than or equal to, e.g. `bool Weight::operator<=(Weight other)`
* `bool operator>` : greater than, e.g. `bool Weight::operator>(Weight other)`
* `bool operator>=` : greater than or equal to, e.g. `bool Weight::operator>=(Weight other)`

Note that comparison operators must return a `bool`, as the result is either true or false. The other operators are free to return whatever type is most appropriate.
Note also that the mathematical operators are free to mix types, e.g. it doesn't
make sense to multiply or divide a weight by another weight, but it does make
sense to multiply or divide a weight by a floating point number. Finally, note that
the choice of the argument name `other` is arbitrary (the argument could be named
anything). However, it is a nice convention that makes your code easier to follow.

We can add an operator to a class by adding an operator function. For example, here
is the `Weight` class which has operators added to handle adding and subtracting
weights.

```c++
#include <iostream>

/* A simple class used to represent a person's weight.
   This ensures that the weight cannot be below zero */
class Weight
{
public:
    Weight(float w=0);

    float value();

    Weight operator+(Weight other);
    Weight operator-(Weight other);

private:
    float _weight;
};

Weight::Weight(float w)
{
    if (w > 0)
    {
        this->_weight = w;
    }
    else
    {
        this->_weight = 0;
    }
}

float Weight::value()
{
    return this->_weight;	
}

Weight Weight::operator+(Weight other)
{
    return Weight( this->_weight + other._weight );
}

Weight Weight::operator-(Weight other)
{
    return Weight( this->_weight - other._weight );
}

int main()
{
    Weight w;

    std::cout << "default " << w.value() << std::endl;

    w = w + Weight(5.0);

    std::cout << "add 5.0 " << w.value() << std::endl;

    for (int i=0; i<6; ++i)
    {
        w = w - Weight(1.0);
        std::cout << "subtract 1.0 " << w.value() << std::endl;
    }

    return 0;
}
```

Copy the above code into `weight.cpp` and compile and run using

```
g++ weight.cpp -o weight
./weight
```

You should see printed;

```
default 0
add 5.0 5
subtract 1.0 4
subtract 1.0 3
subtract 1.0 2
subtract 1.0 1
subtract 1.0 0
subtract 1.0 0
```

The line `w = w + Weight(5.0)` calls the function
`Weight Weight::operator+(Weight other)`, while `w = w - Weight(1.0)` calls the
function `Weight Weight::operator-(Weight other)`.

Because these two operators use the constructor to construct a new `Weight`, the condition
that catches negative weights is tested, and so the code automatically ensures that
the weight cannot go below zero. Thus `Weight(0) - Weight(1)` equals `Weight(0)`.

***

## Putting it all together...

We can put everything we have learned together to update the `PersonData` class so that
it captures the concept of heights and weights, and so that it provides an easier
user interface, e.g. enabling heights or weights to be subtracted from the data.
The new user interface aims to support code that looks like this;

```c++
    //now, we have heard that James and Janet have lost weight...
    database["Janet"] = database["Janet"] - Weight(3.2);
    database["James"] = database["James"] - Weight(1.4);

    //meanwhile, John has gained weight
    database["John"] = database["John"] + Weight(4.5);

    //and Jane has grown a bit taller...
    database["Jane"] = database["Jane"] + Height(0.1);
```

To implement this, we need to create a `Weight` class (based on `Weight` above), 
a `Height` class, that is very similar to `Weight`, and have to update
`PersonData` to use these classes, and to have operators that do the right
thing if a `Weight` or `Height` is added or subtracted.

The complete code is written below. Please copy and paste into the specified
files;

First, copy the declarations of the classes into `persondata.h`;

```c++
#ifndef _PERSONDATA_H
#define _PERSONDATA_H

/* A simple class that holds the weight of a person */
class Weight
{
public:
    Weight(float w=0);

    float value();

    Weight operator+(Weight other);
    Weight operator-(Weight other);

private:
    float _weight;
};

/* A simple class that holds the height of a person */
class Height
{
public:
    Height(float h=0);

    float value();

    Height operator+(Height other);
    Height operator-(Height other);

private:
    float _height;
};

/* The data about a person in the database */
class PersonData
{
public:
    PersonData();

    Height height();
    Weight weight();

    float bmi();

    PersonData operator+( Height height );
    PersonData operator+( Weight weight );
    PersonData operator-( Height height );
    PersonData operator-( Weight weight );

private:
    Height _height;
    Weight _weight;
};

#endif
```

Next, copy the implementations of the classes into `persondata.cpp`;

```c++
#include "persondata.h"

Height::Height(float h)
{
    if (h > 0)
    {
        this->_height = h;
    }
    else
    {
        this->_height = 0;
    }
}

float Height::value()
{
    return this->_height;
}

Height Height::operator+(Height other)
{
    return Height( this->_height + other._height );
}

Height Height::operator-(Height other)
{
    return Height( this->_height - other._height );
}

Weight::Weight(float w)
{
    if (w > 0)
    {
        this->_weight = w;
    }
    else
    {
        this->_weight = 0;
    }
}

float Weight::value()
{
    return this->_weight;
}

Weight Weight::operator+(Weight other)
{
    return Weight(this->_weight + other._weight);
}

Weight Weight::operator-(Weight other)
{
    return Weight(this->_weight - other._weight);
}

PersonData::PersonData()
{}

Height PersonData::height()
{
    return this->_height;
}

Weight PersonData::weight()
{
    return this->_weight;
}

float PersonData::bmi()
{
    return this->weight().value() / 
            (this->height().value() * this->height().value());
}

PersonData PersonData::operator+(Height height)
{
    PersonData ret;
    ret._height = this->_height + height;
    ret._weight = this->_weight;

    return ret;
}

PersonData PersonData::operator+(Weight weight)
{
    PersonData ret;
    ret._height = this->_height;
    ret._weight = this->_weight + weight;

    return ret;
}

PersonData PersonData::operator-(Height height)
{
    PersonData ret;
    ret._height = this->_height - height;
    ret._weight = this->_weight;
                                    
    return ret;
}

PersonData PersonData::operator-(Weight weight)
{
    PersonData ret;
    ret._height = this->_height;
    ret._weight = this->_weight - weight;
                                   
    return ret;
}
```

Finally, copy into `main.cpp` some code that uses these classes;

```c++
#include <iostream>
#include <map>
#include <string>
#include <vector>

#include "persondata.h"

/* Function to print the database to the screen */
void print( std::map<std::string,PersonData> database )
{
    //now print out the entire database
    for ( auto item : database )
    {
        //print out the name
        std::cout << item.first << " : ";

        auto data = item.second;

        std::cout << "height=" << data.height().value()
                  << " weight=" << data.weight().value()
                  << " bmi=" << data.bmi() << std::endl;
    }
}

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
        data = data + Height(heights[i]);
        data = data + Weight(weights[i]);

        database[names[i]] = data;
    }

    //now print out the entire database
    print(database);

    //now, we have heard that James and Janet have lost weight...
    database["Janet"] = database["Janet"] - Weight(3.2);
    database["James"] = database["James"] - Weight(1.4);

    //meanwhile, John has gained weight
    database["John"] = database["John"] + Weight(4.5);

    //and Jane has grown a bit taller...
    database["Jane"] = database["Jane"] + Height(0.1);

    //print out the entire database again
    std::cout << std::endl << "Some time later..." << std::endl;

    print(database);

    return 0;
}
```

Compile and run using

```
g++ --std=c++14 main.cpp persondata.cpp -o persondata
./persondata
```

You should see printed;

```
James : height=1.7 weight=75.4 bmi=26.09
Jane : height=1.8 weight=76.5 bmi=23.6111
Janet : height=1.5 weight=56.8 bmi=25.2444
John : height=1.4 weight=52 bmi=26.5306

Some time later...
James : height=1.7 weight=74 bmi=25.6055
Jane : height=1.9 weight=76.5 bmi=21.1911
Janet : height=1.5 weight=53.6 bmi=23.8222
John : height=1.4 weight=56.5 bmi=28.8265
```

The use of operators and classes that represent concepts has caused
you as the developer to write a lot of lines of code. However, it means 
that people who use `PersonData` are able to use your classes more
easily, and to write code such as;

```c++
    //now, we have heard that James and Janet have lost weight...
    database["Janet"] = database["Janet"] - Weight(3.2);
    database["James"] = database["James"] - Weight(1.4);

    //meanwhile, John has gained weight
    database["John"] = database["John"] + Weight(4.5);

    //and Jane has grown a bit taller...
    database["Jane"] = database["Jane"] + Height(0.1);
```

This is much cleaner than manipulating floats in maps directly, and has the in-built
checks to ensure that the heights or weights can't drop below zero.

Take a look through this code and make sure you are happy with the functions that are
being called, and why subtracting a `Weight` from a `PersonData` is safe (i.e.
which code stops the weight dropping below zero).

***

# [Previous](objects.md) [Up](README.md) [Next](whatnext.md)  
