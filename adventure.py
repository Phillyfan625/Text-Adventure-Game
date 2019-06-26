import random
import sys
import time

def script():
     restart = input("Would you like to restart this program?")
     if restart == "yes" or restart == "y" or restart == "Yes":
         playGame()
     if restart == "n" or restart == "no" or restart == "No":
        exit()


def playGame():
                print("Our Journey Begins")

                name = input("What is your name? \n")

                print("Lets go forth our adventure " + name)
                answer = input("You see a pathway in the distance, (left or right)\n")
                # LEFT
                if answer == ("left"):
                    
                    answer = input("Now you see a 100 foot monster, do you run or attack?\n")
                    if answer == ("run"):
                        print("ouch that sucker killed you") 
                        script()     
                        
                    else:
                        print("Well there are good and bad news")
                        print("Good news: the monster is gone")
                        print("bad news: your fingers are gone")
                    
                        # continues the path of attack
                        answer = input("You start to walk the path, as you see a bag full of items. Do you want the item?\n")
                    
                # RIGHT
                else:
                    answer = input("You embark on a house in the woods, do you enter?\n")
                    if answer == ("yes"):
                        print("The house is very big, you continue to walk into the house as you hear a loud sound in the attic.")
                        answer = input( "Do you want to investigate the sound? (yes/no)\n")
                        if answer == ("yes"):
                            print("OOHH Okay you freakky")
                            print("You start to run upstairs")
                            print("You begin to hear a faint laugh as you approach the attic")
                            answer = input("Do you still want to go in the attic?(yes/no)\n")
                            if answer == ("yes"):
                                print("take a deep breath bud, you're in for a treat!")
                            else:
                                print("It's okay to be a wimp sometimes")
                        else:
                            print("You're smarter than you look")
                    else:
                        print("You now realize you are in a game, so you start to fly!\n")
                        script()
 
 
def startGame():
     playerAnswer = input("Would you like to embark on an adventure? (Yes/No)\n")
     if playerAnswer == ("Yes") or playerAnswer == ("yes"):
         playGame()
     else:
         exit()
         
         
startGame()

                            


