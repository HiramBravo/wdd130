print("You wake up to the alarm of a falling plane and you are the only person on board")
print("What do you do first?")
print("You try to find the pilot or try to fly the plane?")
first_choice = input("What do you choose, FIND or FLY? ")
if first_choice.upper() == "FIND" :
    find = input("You wasted precious seconds looking for the pilot and you couldn't find him")
    print("Do you want to keep looking for the pilot or try to fly the plane? ")
    first_choice_2 = input("What do you choose, FIND or FLY? ")
    if first_choice_2.upper() == "FIND" :
        find_2 = input("By continuing to look for the pilot, you didn't realize that the plane was losing altitude very quickly and crashed into a mountain, so you died")
    else:
        if first_choice_2.upper() == "FLY" :
         fly = input("You try to fly the plane you realize the controls work but you have no idea how to fly the plane")
        print("Are you still trying to fly the plane or are you trying to find a parachute? ")
        first_choice_3 = input("What do you choose, PARACHUTE or FLY? ")
        if first_choice_3.upper() == "PARACHUTE" :
            parachute = input ("You find the parachute, now you must decide to jump or wait until the plane is closer to the ground to jump? ")
else:
    if first_choice.upper() == "FLY" :
        fly = input("You try to fly the plane you realize the controls work but you have no idea how to fly the plane")
        print("Are you still trying to fly the plane or are you trying to find a parachute? ")
        first_choice_3 = input("What do you choose, PARACHUTE or FLY? ")
        if first_choice_3.upper() == "FLY" :
            fly_2 = input("By continuing to look for the pilot, you didn't realize that the plane was losing altitude very quickly and crashed into a mountain, so you died")
        if first_choice_3.upper() == "PARACHUTE" :
            parachute = input ("You find the parachute, now you must decide to jump or wait until the plane is closer to the ground to jump? ")
            first_choice_4 = input("Jump KNOW or WAIT? ")
            if first_choice_4.upper() == "KNOW" :
                know = input("You jump immediately so you manage to open your parachute and managed to land safe and sound.")
                print("You made it!")
            else:
                if first_choice_4.upper() == "WAIT" :
                    wait = input("You waited until the last minute to jump so there wasn't enough pressure to open the parachute so you didn't land very well.")
                    print("Don't worry is a game try again!")