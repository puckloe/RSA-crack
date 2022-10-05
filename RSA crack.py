#imports needed modules
import math
import sys

#this function finds the factors of a number and only returns if it has two factors for if n is small
#not including the number and 1
def shortNumberFactors(number):
    numberList = []
    for i in range(2, (number-1)):
            if number % i == 0:
                   numberList.append(i)
    if len(numberList) == 2:
        p = numberList[0]
        q = numberList[1]
        return p, q
                
    else:
        return 1, number


#this function also gets the factors of n, but only if n is a large number
def bigNumberFactors(n):
    a = float(int(math.sqrt(n)))
    while True:
        bSquared = ((a**2) - n)
        if bSquared > 1:
            b = math.sqrt(bSquared)
        else:
            b = 0.1 #b is not actually equal to 0.1 but it has been set this way as you can't squre root negative numbers and making a float just makes it iterate again
        if b.is_integer():
            p = a+b
            q = a - b
            return p, q
            break
        else:
            a = a+1
    
#this function gets the Euiler totient of a function
def getEulerTotient(p, q):
    phi = (p - 1) * (q - 1)
    return phi


#this essencially just does the rest of the RSA normally to find d
def findKey(e, phi):
    d = 1
    while True:
        if ((e * d) % phi) == 0:
            return d
        else:
            d = d + 1

#main program
try:
    e = int(input("what is the value of e? "))
    n = int(input("what is the value of n? "))
    
except ValueError:
    print("that is not a valid input")
    sys.exit()
    
except KeyboardInterrupt:
    print("that is not a valid input")
    sys.exit()

#if the value of n is small you can quite easily just find the factors of n
if n < 1000:
    p, q = shortNumberFactors(n)


        

else:
    p, q = bigNumberFactors(n)

#verify if n is a valid input
if p == 1:
    print("that is not a valid value for n as it is not a multiple of two primes")

#from here you can essencially just do RSA normally as you have p and q so you can find the value for d quite simply
else:
    phi = getEulerTotient(p, q)
    d = findKey(e, phi)
    print("the decryption key is " + str(d) + " or any value of " + str(d) + " added with a multiple of " + str(e)) 
