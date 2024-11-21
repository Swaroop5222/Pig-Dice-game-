
import random

def user_turn(user_total):
   print("Now it's your turn")
   while(True):
      user=input("Enter \'e\' to roll the dice: ").lower()
      if user=='e':
         user_choice=random.randint(1,6)
         print("Your dice value is: ",user_choice)
         if user_choice!=1:
           user_total+=user_choice
         print("Your Score: ",user_total)
         if user_choice==1:
          print("Dice value is 1. So it's now computer's turn")
          break
      else:
         print("Enter \'e\' only to roll dice")
   return user_total,user_choice

def computer_turn(computer_total):
   while(True):
      computer_choice=random.randint(1,6)
      print("Computer's dice value is: ",computer_choice)
      if computer_choice!=1:
       computer_total+=computer_choice
      print("Computer Score: ",computer_total)
      if computer_choice==1:
        print("Dice value is 1. So it's now user's turn")
        break
   return computer_total,computer_choice

while(True):
 user_total,computer_total,user_choice=0,0,0
 ask=input("Do you want to play the game?(y/n): ").lower()
 if ask=='y':
   while(True):
          if user_total>=100:
            print("You won the game!")
            print("Your score is: ",user_total)
            print("Computer score is: ",computer_total)
            break
          elif computer_total>=100:
            print("You lost the game!")
            print("Your score is: ",user_total)
            print("Computer score is: ",computer_total)
            break
          elif user_choice==1:
            computer_total,computer_choice= computer_turn(computer_total)
            user_choice=0
          else:
             user_total,user_choice=user_turn(user_total) 

 elif ask=='n':
    print("Game completed")
    break
 else:
    print("Enter either y or n only: ")
