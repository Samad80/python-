import random

def dice():
    return random.randint(1,6)

def main():
    print("press enter to roll a dice")
    input ()
    for i in range (2):
    print("you rolled a", dice())

main()
