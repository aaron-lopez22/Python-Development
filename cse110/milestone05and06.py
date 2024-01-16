'''
Aaron Lopez
Milestone 05 06
CSE 110
Adventure Game
'''

print()
print("Today we are going to play and adventure game where you can make the choices. The choices will be shown in caps lock to choose from.\n ")
print("You wake up in your tent and notice that the person you were with is missing. You decide you can either LEAVE or STAY.")
choice1 = input("(LEAVE/STAY)? ")
print()



if choice1.lower() == "leave":
    print("You decide to leave and look for the person you were with. You take a flashlight and start walking away from camp. As you begin walking you hear a scream up ahead.")
    print("You can RUN for the scream because it could be the person you were with, you can HIDE, or go BACK to camp.")
    choice1_1 = input("(RUN/HIDE/STAY)?")
    if choice1_1.lower() == "run":
        print("As you run towards the scream you trip and fall. You end up rolling off a cliff and dying.")
    elif choice1_1.lower() == "hide":
        print("As you hide the scream stops and you start hearing laughter and realize it is just another campout having a party. So you turn to leave and get attacked by a bear.")
    elif choice1_1.lower() == "stay":
        print("You go back to camp when you hear the person you were with yelling your name. When you arrive you find out they just went to the bathroom.")
    else:
        print("wrong answer has been chosen the game has ended.")
elif choice1.lower() == "stay":
    print("As you stay in camp you start to get paranoid and think that someone may have attacked the person you were with. You get up to think if maybe you run to the CAR you can grab a gun you have or just go back to SLEEP and forget about the whole thing.")
    choice2_1 = input("(SLEEP/CAR)? ")
    if choice2_1.lower() == "sleep":
        print("You wake up to find the person you were with had just gone to the bathroom and came back a little after you fell asleep.")
    elif choice2_1 == "car":
        print("As you begin to run to the car you hear some noises next to you and turn to then get attacked by a bear. You manage to slip out and see a CAVE nearby or can still grab the GUN.") 
        choice2_2 = input("(CAVE/GUN)? ") 
        if choice2_2.lower() == "cave":
            print("You run to the cave and there happnens to be a small space to crawl into and the bear can't get to you. Eventually the bear leaves you alone. You are then able to go back to camp to find the person and let them know what happened")
        elif choice2_2.lower() == "gun":
            print("You run to the car to grab the gun to only find that the gun is not loaded and get eaten by the bear.")
        else:
            print("wrong answer has been chosen the game has ended.")
    else:
         print("Wrong answer has been chosen the game is over.")         
else:
    print("Wrong answer has been chosen the game is over.")
