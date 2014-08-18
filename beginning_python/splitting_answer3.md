#Splitting Lines Answer to exercise 3

    import sys
    
    lines = open( sys.argv[1], "r" ).readlines()
    
    total_premium = 0
    nmakes = 0
    
    oldest_age = 0
    highest_class = 0
    lowest_class = 1000
    
    for i in range( 1, len(lines) ):
        line = lines[i].rstrip()
        words = line.split(",")
    
        if len(words) >= 4:
            make = words[0]
            car_class = int( words[1] )
            premium = float( words[2] )
            age = float( words[3] )
    
            nmakes += 1
    
            total_premium += premium
    
            if age > oldest_age:
                oldest_make = make
                oldest_age = age
    
            if car_class > highest_class:
                highest_make = make
                highest_class = car_class
        
            if car_class < lowest_class:
                lowest_make = make
                lowest_class = car_class
     
    avg_premium = total_premium / nmakes
    
    print("The average premium is $%f." % avg_premium)
    print("The oldest make is %s." % oldest_make)
    print("The make in the lowest class is %s." % lowest_make)
    print("The make in the highest class is %s." % highest_make)

# [Previous](splitting.md) [Up](README.md) [Next](splitting.md)
