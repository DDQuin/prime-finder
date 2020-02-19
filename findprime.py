import math

#This function keeps finding prime numbers and printing them out until n is entered

def startPrimeSearch():
    primenum = 1
    while(True):
        primenum = primenum + 1
        print("Enter n to stop finding primes.")
        response = input()
        if not response == 'n':
            primenum = findNextPrime(primenum)
            print("The prime number is: " + str(primenum))
        else:
            print("Program finished")
            return

# Function starts from a given number and increments the number to check if it is a prime
# number, it keeps on going until a prime number is found and returns the prime number
def findNextPrime(startnumber): 
    n = startnumber
    while(True):
        prime = isPrime(n)
        if not prime == False:
            return prime
        else:
            n = n + 1
    

#Function takes in a number and checks if it is prime or not, returns False if not and the number if it is prime
def isPrime(possibleprime):
    n = possibleprime
    endnumber = math.floor(n / 2)  # the number / 2 rounded down is the last number that has a chance of being a factor
    for i in range(2, endnumber + 1): # Now start looping through every number i that could be a possible factor from 2 to the endnumber (1 added as without, range would go to endnumber - 1)
            if n % i == 0:  #If the number n divided by i is zero then i is a factor so the number n is not prime so return false
                return False
    return n    # No factor found for the number so it must be prime 
    
        
# Main
startPrimeSearch()
