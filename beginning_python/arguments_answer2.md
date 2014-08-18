#Arguments! Answer to exercise 2

    import sys
    
    t = int( sys.argv[1] )
    
    n = int( sys.argv[2] )
    
    numbers = [ "zero", "one", "two", "three", "four",
                "five", "six", "seven", "eight", "nine",
                "ten", "eleven", "twelve" ]
    
    print("This is the %s times table." % numbers[t])
    
    for i in range(1, n+1):
        t_times_i = t * i
    
        print("%s times %s equals %d" % ( numbers[i], numbers[t], t_times_i ))

# [Previous](arguments.md) [Up](README.md) [Next](arguments.md)
