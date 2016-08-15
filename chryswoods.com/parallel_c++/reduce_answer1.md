# Reduction : Answer to exercise 1

```c++
#include "part1.h"
#include "filecounter.h"

using namespace part1;
using namespace filecounter;

int sum(int x, int y)
{
    return x + y;
}

int main(int argc, char **argv)
{
    auto filenames = get_arguments(argc, argv);

    auto results = map( count_lines, filenames );

    for (size_t i=0; i<filenames.size(); ++i)
    {
        std::cout << filenames[i] << " = " << results[i] << std::endl;
    }

    auto total = reduce( sum, results );

    std::cout << "The total number of lines is " << total << std::endl;

    return 0;
}
```

***

# [Previous](reduce.md) [Up](reduce.md) [Next](reduce.md)
