#Files Answer to exercise 3

    from __future__ import print_function
    import sys
    
    start = int( sys.argv[1] )
    end = int( sys.argv[2] )
    
    lines = open( sys.argv[3], "r" ).readlines()
    
    nlines = len(lines)
    
    if start < 0:
        start = 0
    elif start >= nlines:
        start = nlines-1
    
    if end >= nlines:
        end = nlines-1
    elif end < 0:
        end = 0

    if end >= start:
        for i in range(start, end+1):
            print(lines[i], end="")
    else:
        for i in range(start, end-1, -1):
            print(lines[i], end="")

# [Previous](files.md) [Up](README.md) [Next](files.md)
