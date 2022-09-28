choose_year = input("Enter the year of interest: ")
with open("life-expectancy.csv") as life_file:
    next(life_file)

    max = 0
    min = 100

    for line in life_file:
        data = line.strip().split(",")

        country = data[0].strip()
        code = data[1].strip()
        year = int(data[2])
        life = float(data[3])

        if life > max:
            max = life 
        
        if life < min:
            min =life

    if choose_year.strip() == choose_year.strip():
        print(f"The overall max life expectancy is: {max} from {country} in {year}")
        print(f"The overall min life expectancy is: {min} from {country} in {year}")
        print(f"")
