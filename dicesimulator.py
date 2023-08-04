import random

def dice():
    return random.randint(1,6)

def main():
   for i in range (2):
    print("you rolled a", dice())

main()
