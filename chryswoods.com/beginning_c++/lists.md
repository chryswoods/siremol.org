
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

    //finally, look up the sound of a cat
    std::cout << "What is the sound of a cat? " << m["cat"] 
              << std::endl;

    return 0;
}
```

Compile and run the above example using

```
g++ --std=c++14 map.cpp -o map
./map
```

Things to note about a C++ map versus a Python dictionary are;

* You must specify the type of the key and the type of the value, between the angle brackets, e.g. `std::map<int,double>` would be a map that uses integer keys to look up double values.
* Like Python, you look up items in the map using square brackets, e.g. `m["cat"]` looks up the value for `"cat"`.
* Like Python, if the item doesn't exist, then it is created and assigned, e.g. `m["cat"] = "mieow"` sets the value associated with the key `cat` to `mieow`.
* Unlike Python, there is no `.insert()` function. You can only add items using lookup.
* Unlike Python, there is no `.keys()` or `.values()` function. You have to write these yourself...
* When you loop through the values in a map, the iterated item is a key-value pair. In `for ( auto item : m )`, the type of `item` is a key-value pair. The key is the first item in the pair `item.first`, while the value is the second item `item.second`.
* All keys in a map have to have the same type, and all values in a map have to have the same type, buy keys and values don't have to have the same type. For example, `std::map<float,std::string>` creates a map in which all keys are floats, and all values are strings.

You can use any type as a value in a map, including vectors or indeed other maps. For example, here we use a map of maps to record the weight and height of a range of people;

```c++
#include <iostream>
#include <string>
#include <map>
#include <vector>

int main()
{
    //declare the map that uses a person's name as a key, and looks
    //up a map that stores the person's weight and height
    std::map< std::string, std::map<std::string,float> > database;

    //let's first put the data in three vectors
    std::vector<std::string> names = { "James", "Jane", "Janet", "John" };
    std::vector<float> heights = { 1.7, 1.8, 1.5, 1.4 };
    std::vector<float> weights = { 75.4, 76.5, 56.8, 52.0 };

    //now put all of the data into the database
    for (int i=0; i<names.size(); ++i)
    {
        std::map<std::string,float> data;

        data["height"] = heights[i];
        data["weight"] = weights[i];

        database[names[i]] = data;
    }

    //now print out the entire database
    for ( auto item : database )
    {
        //print out the name
        std::cout << item.first << " : ";

        //now print out all of the data about the person
        for ( auto data : item.second )
        {
            std::cout << data.first << "=" << data.second << " ";
        }

        std::cout << std::endl;
    }

    return 0;
}
```

***

#Exercise

Copy the above example into a file called `data.cpp`. Compile using

```
g++ --std=c++14 data.cpp -o data
./data
```

You should see printed

```
James : height=1.7 weight=75.4 
Jane : height=1.8 weight=76.5 
Janet : height=1.5 weight=56.8 
John : height=1.4 weight=52 
```

Now edit `data.cpp` to add the function `float bmi(float height, float weight)`. Write the function so that it returns the body
mass index (BMI, weight divided by the square of the height).

Next, add a loop before the line `//now print out the entire database` that will loop over every person and calls your new `bmi` function to calculate that person's BMI. You should update the data for each person to save the BMI using the key `bmi`. 

Once you have written the function, compile and run the program again. The output should be;

```
James : bmi=26.09 height=1.7 weight=75.4 
Jane : bmi=23.6111 height=1.8 weight=76.5 
Janet : bmi=25.2444 height=1.5 weight=56.8 
John : bmi=26.5306 height=1.4 weight=52 
```

If you get stuck or need help, take a look at an [example answer here](lists_answer.md).

***

# [Previous](typing.md) [Up](README.md) [Next](objects.md)  
