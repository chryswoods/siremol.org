# Mapping Functions : Answer to exercise 1

```c++
#include "part1.h"
#include "filecounter.h"

using namespace part1;
using namespace filecounter;

int main(int argc, char **argv)
{
    auto filenames = get_arguments(argc, argv);

    auto results = map( count_lines, filenames );

    for (size_t i=0; i<filenames.size(); ++i)
    {
        std::cout << filenames[i] << " = " << results[i] << std::endl;
    }

    return 0;
}
```

***

# [Previous](map.md) [Up](map.md) [Next](map.md)
