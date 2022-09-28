with open("life-expectancy.csv") as life_expectancy:
    interest = input("Enter the year of interest: ")
    my_list = []
    for line in life_expectancy:
        line = line.strip()
        line = line.split(",")
        entity = line[0]
        code = line[1]
        year = line[2]
        life = line[3]
        my_list.append(life)
        minimum = min(my_list)
        maximum = max(my_list)
    print(f"{minimum}")
    print(f"{maximum}")

        
    

