import random 

def numguess():

    n = int(input ("enter a number from one to ten "))
    comp =random.randint(1,10)
    print("computer guessed" , comp)
    if (n==comp ):
        print("you guessed it right")
    elif  ((n>comp)):
        print('too high')
    else:
        print ('too low ')
        return None

def main ():

    while True :
        numguess ()
        again = input("do you want another guess? ")
    
main()
