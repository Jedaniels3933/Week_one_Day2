# Buggy Code 

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")   
if action == ("climb a tree"):
    print("You found a bird's nest!")
elif action == ("cross a river"):
    print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")


    #Based on the corrected code from Task 1, expand the game. If the user chooses "cave", instead of printing "You find a hidden treasure!" ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

    place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")   
if action == ("climb a tree"):
    print("You found a bird's nest!")
elif action == ("cross a river"):
    print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

    #Based on the corrected code from Task 1, expand the game. If the user chooses "cave", instead of printing "You find a hidden treasure!" ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")   
    if action == ("climb a tree"):
        print("You found a bird's nest!")
    if action == ("cross a river"):
        print("You found a boat!")
if place == "cave":
    action = print("light a torch or proceed in the dark?")
decision = input("What do you do? ")
if decision == "light a torch":
        print("Let there be light!")
        print("You find a hidden treasure!")
if decision == ("proceed in the dark"):
        print("You stumble and fall into a pit full of rabid hamsters!")
        print("You can not tell after 5 seconds what is worse, the pain or the cringe....never mind...it is the pain!")
        print("Game Over!")

        #Task 3 

        place = input("Choose a place: forest or cave? ")

if place == "forest":
    pass
else:
    
    
    action = input("climb a tree or cross a river?")   
    if action == ("climb a tree"):
        print("You found a bird's nest!")
    if action == ("cross a river"):
        print("You found a boat!")
if place == "cave":
  
    action = print("light a torch or proceed in the dark?")
    
decision = input("What do you do? ")
if decision == "light a torch":
         
    print("Let there be light!")
    print("You find a hidden treasure!")
if decision == ("proceed in the dark"):
        print("You stumble and fall into a pit full of rabid hamsters!")
        print("You can not tell after 5 seconds what is worse, the pain or the cringe....never mind...it is the pain!")
        print("Game Over!")

    #You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

#Buggy Code:

#attendees = input("Enter number of attendees: ")
#venue = "large hall" if attendees > 100 elif "conference room"
#print(venue)

attendees = input("Enter number of attendees: ")

if attendees > 100: 
    venue = ("large hall") 
elif "conference room":
    print("venue") 

   #Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".


attendees = input("Enter number of attendees: ")
user_input = input("Do you want vegetarian food? (yes/no): ")
if yes == ("Veggie Delight Caterers"):
    print("Venue: Veggie Delight Caterers")
else no == ("Gourmet Meals Caterers"):
    print("Venue: Gourmet Meals Caterers")
if attendees > 100: 
    venue = ("large hall") 
elif "conference room":
    print("venue")    


