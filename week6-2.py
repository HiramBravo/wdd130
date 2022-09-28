can_ride = False
age_first = int(input("What is the age of the first rider? "))
height_first = int(input("What is the height of the first rider? "))
second_rider = (input("Is there a second rider? "))
if second_rider.lower() == "yes" :
    age_second = int(input("What is the age of the second rider? "))
    height_second = int(input("What is the height of the second rider? "))
    if height_first < 36 or height_second < 36:
        can_ride = False 
    else:
        if age_first >= 18 or age_second >= 18:
            can_ride = True
        else:
            can_ride = False
else:
    if age_first >= 18 and height_first >= 62:
        can_ride = True
    else:
        can_ride = False
if can_ride:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")