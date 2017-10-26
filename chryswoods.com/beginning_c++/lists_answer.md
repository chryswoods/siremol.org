#Lists and Dictionaries : Answer to exercise

```c++
#include <iostream>
#include <string>
#include <map>
#include <vector>

/* Function to return the body mass index */
float bmi(float height, float weight)
{
    return weight / (height*height);
}

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

    //loop over every person to calculate their bmi
    for ( auto person : database )
    {
        //get the map of the data for this person
        auto data = person.second;

        auto b = bmi( data["height"],
                      data["weight"] );

        //now save the bmi into the data
        data["bmi"] = b;

        //finally, update the database to store the bmi
        database[person.first] = data;
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

# [Previous](lists.md) [Up](lists.md) [Next](lists.md)
