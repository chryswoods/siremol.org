
# Concepts and Operators

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

Should see...

Default value of argument...

Check to see if the argument is valid... Fix the problem at the source.

## Operators

What if we want to change. Ideally would like to add two weights together. Can do this using operators.

```c++
weight with operators example

loop that keeps subtracting but cannot go below zero.
```

We can now add weights together. Also can subtract weights knowing that the total will never go below zero.

Key operators are

* `operator+` : addition
* `operator-` : subtraction
* `operator*` : multiplication
* `operator/` : division
* `bool operator==` : equals to
* `bool operator!=` : not equal to 
* `bool operator<` : less than
* `bool operator<=` : less than or equal to
* `bool operator>` : greater than
* `bool operator>=` : greater than or equal to

Note that comparison operators must return a `bool`, as the result is either true or false. The other operators are free to return whatever type is most appropriate.

Full example, here is the `PersonData` example that has been rewritten to use
`Weight`, `Height` and operators to make it easy to work with the data. First, 
here is the code that should be in `persondata.h`;

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
};

#endif
```

Next, here is the implementation in `persondata.cpp`;

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

Finally, here is the `main.cpp` that uses these classes;

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

SOMETHING

Use of operators means that developers using `PersonData` are able to write code such as;

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
checks to ensure that the height or weight can't drop below zero.

Take a look through this code and make sure you are happy with the functions that are
being called, and why subtracting a `Weight` from a `PersonData` is safe (i.e.
which code stops the weight dropping below zero).

***

# [Previous](objects.md) [Up](README.md) [Next](whatnext.md)  
