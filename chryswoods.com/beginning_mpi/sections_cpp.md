#C++

Create the file `mpi_sections.cpp` and copy in the following;

```c++
#include <mpi.h>
#include <iostream>
#include <unistd.h>

void times_table(int n)
{
    int rank = MPI::COMM_WORLD.Get_rank();

    for (int i=1; i<=n; ++i)
    {
        int i_times_n = i * n;
        std::cout << "Process " << rank << " says " << i
                  << " times " << n << " equals " << i_times_n << std::endl;
        sleep(1);
    }
}

void countdown()
{
    int rank = MPI::COMM_WORLD.Get_rank();

    for (int i=10; i>=1; --i)
    {
        std::cout << "Process " << rank << " says " << i << "...\n";
        sleep(1);
    }

    std::cout << "Process " << rank << " says \"Lift off!\"\n";
}

void long_loop()
{
    double sum = 0;

    int rank = MPI::COMM_WORLD.Get_rank();

    for (int i=1; i<=10; ++i)
    {
        sum += (i*i);
        sleep(1);
    }

    std::cout << "Process " << rank << " says the sum of the long loop is "
              << sum << std::endl;
}

int main(int argc, char **argv)
{
    MPI::Init(argc, argv);

    int rank = MPI::COMM_WORLD.Get_rank();

    if (rank == 0)
    {
        std::cout << "This is the main process\n";
        times_table(12);
    }
    else if (rank == 1)
    {
        countdown();
    }
    else if (rank == 2)
    {
        long_loop();
    }
    else
    {
        std::cout << "I am not needed...\n";
    }

    MPI::Finalize();

    return 0;
}
```

Note that we have included the header file `unistd.h` to use the function `sleep`, 
to add one second pauses (via `sleep(1)`) within each function.

In this example we use the function `MPI::COMM_WORLD.Get_rank()`. This function 
returns the rank of the calling process. This allows the `if` block to be used to 
control which function is called by which process in the MPI process team. While 
it is possible to write the code within each block of the `if` statement directly, 
the code is more readable if you write each section as a function 
(e.g. `countdown`, `long_loop` and `times_table`) and just call the function 
from within each block.

You can compile this program using;

    mpicxx mpi_sections.cpp -o mpi_sections

This will produce the executable, `mpi_sections`.

[Return to the previous page](sections.md).
