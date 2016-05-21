from random import randint

def FermatPrimalityTest(number):
    for time in range(3):
        randomNumber = randint(2, number)-1
        
        if ( pow(randomNumber, number-1, number) != 1 ):
            return False
    
    return True

        
def prime_finder(start, stop):
    
    current = randint(start, stop)
    
    if (current % 2) == 0:
        current += 1
        
    found = False
    
    while found == False:
        found = FermatPrimalityTest(current)
        if found == False:
            current += 2  
        
        
    if found == True:
        return current
    
    else:
        print('no prime found')

        
             