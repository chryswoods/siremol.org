#Splitting Lines Answer to exercise 1

    import sys
    
    lines = open( sys.argv[1], "r" ).readlines()
    
    nlines = 5
    
    if nlines > len(lines):
        nlines = len(lines)
    
    for i in range(0, nlines):
        words = lines[i].split()
    
        if len(words) > 0:
            print(words[0])

# [Previous](splitting.md) [Up](README.md) [Next](splitting.md)
