# Part 1 : Memory Layout - Example answer

```c++
#include "workshop.h"

class People
{
public:
    People(int npeople = 0)
    {
        if (npeople > 0)
        {
            height = workshop::Array<float>(npeople,0.0);
            weight = workshop::Array<float>(npeople,0.0);
            girth = workshop::Array<float>(npeople,0.0);
        }
    }

    People(const workshop::Array<workshop::Person> &people)
    {
        height = workshop::Array<float>(people.size());
        weight = workshop::Array<float>(people.size());
        girth = workshop::Array<float>(people.size());

        for (int i=0; i<people.size(); ++i)
        {
            height[i] = people[i].height;
            weight[i] = people[i].weight;
            girth[i] = people[i].girth;
        }
    }

    workshop::Person operator[](int i) const
    {
        return workshop::Person(height[i], weight[i], girth[i]);
    }

    void set(int i, workshop::Person person)
    {
        height[i] = person.height;
        weight[i] = person.weight;
        girth[i] = person.girth;
    }

    workshop::Array<workshop::Person> toArray() const
    {
        workshop::Array<workshop::Person> people(height.size());

        for (int i=0; i<height.size(); ++i)
        {
            people[i].height = height[i];
            people[i].weight = weight[i];
            people[i].girth = girth[i];
        }

        return people;
    }

    workshop::Array<float> height;
    workshop::Array<float> weight;
    workshop::Array<float> girth;
};

int main(int argc, char **argv)
{
    const int npeople = 1024;

    auto people = People(npeople);

    //construct a random sample of people (in reality, you would
    //read this from real data - here we are just randomly generating
    //it using functions already provided in workshop.h
    for (int i=0; i<npeople; ++i)
    {
        people.set(i, workshop::Person( workshop::getRandomHeight(), 
                                        workshop::getRandomWeight() ) );
    }

    auto timer = workshop::start_timer();

    float avg_ratio = 0;

    for (int j=0; j<100000; ++j)
    {
        avg_ratio = 0;

        for (int i=0; i<npeople; ++i)
        {
            avg_ratio += (people.height[i] / people.weight[i]);
        }

        avg_ratio /= npeople;
    }

    auto duration = workshop::get_duration(timer);

    timer = workshop::start_timer();

    float vec_avg_ratio = 0;

    for (int j=0; j<100000; ++j)
    {
        vec_avg_ratio = 0;

        #pragma omp simd reduction(+:vec_avg_ratio)
        for (int i=0; i<npeople; ++i)
        {
            vec_avg_ratio += (people.height[i] / people.weight[i]);
        }

        vec_avg_ratio /= npeople;
    }

    auto vector_duration = workshop::get_duration(timer);

    std::cout << "The standard loop took " << duration
              << " microseconds to complete. The average ratio is " 
              << avg_ratio << std::endl;

    std::cout << "The vectorised loop took " << vector_duration
              << " microseconds to complete. The average ratio is " 
              << vec_avg_ratio << std::endl;

    return 0;
}
```

***

# [Previous](memory.md) [Up](memory.md) [Next](memory.md)
