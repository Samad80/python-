import random

def rps(rock,paper,scissors,):
    user_choice = input("Enter Your Choice ")
    if (user_choice == rock):
        print("you chose rock ")
        computer=random.randint(1,3)
        if 2==computer:
            print ('computer chose paper')
            print ("computer wins")
        elif 3==computer:
            print('computer chose scissors ')
            print('You win ')
        else :
            print ("computer chose same")
            print ("tie")
    elif (user_choice == paper ):
        print ('you chose paper')
        computer=random.randint(1,3)
        if 3 == computer:
            print ('computer chose scissors ' )
            print ("computer wins ")
        elif 1==computer:
            print ('computer chose rock ')
            print ('you win')
        else :
            print ("computer chose same")
            print ('tie ')
    elif(user_choice ==scissors):
        print ('you chose scissor')
        computer=random.randint(1,3)
        if  (1==computer):
            print ('computer chose rock ')
            print ("computer wins ")
        elif (2==computer ):
            print ("computer chose paper ")
            print('you win')
        else :
            print ("computer chose same")
            print ('tie ')
    else :
        print ('invaid entry')


def main():
    rps('rock','paper','scissors',)
           
main ()



