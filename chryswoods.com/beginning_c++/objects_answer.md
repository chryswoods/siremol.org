#Objects and Classes : Answer to exercise

```c++
#include "persondata.h"

PersonData::PersonData()
{
    this->_height = 0;
    this->_weight = 0;
}

void PersonData::setHeight(float height)
{
    this->_height = height;
}

void PersonData::setWeight(float weight)
{
    this->_weight = weight;
}

float PersonData::height()
{
    return this->_height;
}

float PersonData::weight()
{
    return this->_weight;
}

float PersonData::bmi()
{
    return this->_weight / (this->_height * this->_height);
}
```

***

# [Previous](objects.md) [Up](objects.md) [Next](objects.md)
