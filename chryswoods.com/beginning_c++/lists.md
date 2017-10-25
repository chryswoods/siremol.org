
# Lists and Dictionaries

Like Python, C++ comes with a great set of containers. The most commonly used are vectors and dictionaries.

## Lists

C++ vectors are very similar to [Python lists](../intermediate_python/lists.md), i.e. they provide 
containers for a list/array of values that can be accessed by their index. The big difference between
Python lists and C++ vectors is that C++ vectors can only hold values of a single type, which must
be specified when you create the vector. For example, create the source file `vector.cpp` and copy in
the below code;

```c++
#include <iostream>
#include <vector>

int main()
{
    //create a vector that can hold integers
    std::vector<int> v;

    //append values onto the end of the vector
    v.push_back( 4 );
    v.push_back( 2 );

    //the vector can only hold integers, so if you append
    //a float, it will be converted to an integer
    v.push_back(10.5);

    //loop through every item in the vector and print out
    //the value
    std::cout << "std::vector{ ";

    for (int i=0; i<v.size(); ++i)
    {
        std::cout << v[i] << " ";
    }

    std::cout << "}" << std::endl;

    return 0;
}
```

Compile and run this program using

```
g++ vector.cpp -o list
./vector
```

Things to note about a C++ vector compared to a Python list are;

* You use angle brackets `<  >` to specify the type of items held in the vector, e.g. `std::vector<int>`.
* You use the `.push_back()` function to append items to the C++ vector. This is equivalent to the `.append()` function in Python.
* You use the `.size()` function to get the number of items in the vector. This is equivalent to using `len(list)` in Python.
* Just like Python, you use square brackets to access the ith element of the vector, e.g. `v[i]`
* Unlike Python, you must specify the type of items that can be contained in the vector, e.g. `std::vector<int>` can only store 
integers. Likewise, `std::vector<double>` would only store doubles, and `std::vector<std::string>` would only store strings.
* Because `std::vector<int>` can only store integers, the line `v.push_back(10.5)` implicitly converts the floating point number
`10.5` to the integer `10` when it is added to the vector.

Because C++ vectors can store only a single type of data, they are less versatile than Python lists.

It is possible to nest vectors inside vectors, but the syntax is not very elegant e.g.

```c++
#include <iostream>
#include <vector>

int main()
{
    std::vector< std::vector<int> > m;

    //create a 3x3 matrix
    for (int i=1; i<=3; ++i)
    {
        //create space for a row
        std::vector<int> row;

        for (int j=1; j<=3; ++j)
        {
            row.push_back( i * j );
        }

        //now save the row in the matrix
        m.push_back(row);
    }

    //now print the matrix out
    for (int i=0; i<3; ++i)
    {
        for (int j=0; j<3; ++j)
        {
            std::cout << m[i][j] << " ";
        }

        std::cout << std::endl;
    }

    return 0;
}
```

The C++ 2014 (c++14) standard provides some useful syntax that reduces the amount of typing needed
to intialise a vector with values, and to loop over the items in a vector. Create a new source
file called `vector14.cpp` and copy into it;

```c++
#include <iostream>
#include <vector>

int main()
{
    // create a new vector that is initialised to contain the
    // values on the right (held between curly brackets)
    std::vector<int> v = { 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 };

    // loop over every item in the vector using an iterator for loop
    for (auto x : v)
    {
        std::cout << x << " ";
    }

    std::cout << std::endl;

    return 0;
}
```

Compile and run this example using

```
g++ --std=c++14 vector14.cpp -o vector14
./vector14
```

Note you have had to add `--std=c++14` to tell the compiler to compile according to the C++ 2014 standard. This
should not be needed for newer compilers, which will use this standard by default.

The above example shows how you can initialise a vector with a set of values using curly brackets (e.g. `{ 1, 4, 9 etc... }`). 
This is a very useful shorthand that prevents you from having to write `v.push_back(...)` for every element you want
to add.

The example also shows how you can use an iterator for loop to iterate over every item contained in the vector.
Also called a "for each" loop, the syntax is;

```
for ( auto item : vector )
{
    // do something with the item
    std::cout << item << std::endl;
}
```

which will loop sequentially over every item in the vector. Note that we can use `auto` to automatically deduce the 
type of the items contained in the vector. 

If you want to find out more about C++ vectors, [please take a look here](http://en.cppreference.com/w/cpp/container/vector).

***

## Dictionaries

Like Python, C++ has a great dictionary type, which in C++ is called a map. This is a container that stores values that
are indexed by a key. C++ maps are less versatile than Python dictionaries as all of the keys have to be the same
type, and all of the values have to be the same type. For example, copy the following into the source file 
`map.cpp`;

```c++
#include <iostream>
#include <map>
#include <string>

int main()
{
    //create a map that stores strings indexed by strings
    std::map<std::string, std::string> m;

    //add some items to the map
    m["cat"] = "mieow";
    m["dog"] = "woof";
    m["horse"] = "neigh";
    m["fish"] = "bubble";

    //now loop through all of the key-value pairs
    //in the map and print them out
    for ( auto item : m )
    {
        //item.first is the key
        std::cout << item.first << " goes ";

        //item.second is the value
        std::cout << item.second << std::endl;
    }

    return 0;
}
```

Compile and run the above example using

```
g++ --std=c++14 map.cpp -o map
./map
```

Lots to note...

Keys and values don't have to be the same type.
Values can be vectors, e.g.


***

# [Previous](typing.md) [Up](README.md) [Next](calling.md)  
