import random

def guess_number():
  
  number = random.randint(1, 10)
  attempts = 0
  guess = None
  while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1
    if guess < number:
      print("Your guess is too low.")
    elif guess > number:
      print("Your guess is too high.")
    if attempts==3:
      break 
    
  else:
    print(f"Congratulations! You guessed the number in {attempts} attempts.")


def main():
   
   guess_number()
 
main()
