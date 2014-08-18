#Splitting Lines Answer to exercise 2

    import sys
    
    lines = open( sys.argv[1], "r" ).readlines()
    
    # print our own header
    print("Make   Premium($)   Insurance_class")
    
    # skip the header line (start at 1 rather than 0)
    for i in range( 1, len(lines) ):
        line = lines[i].rstrip()
        words = line.split(",")

        if len(words) >= 4:
            print("%s  %s  %s" % (words[0], words[2], words[3]))

# [Previous](splitting.md) [Up](README.md) [Next](splitting.md)
