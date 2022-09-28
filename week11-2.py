with open("hr_system.txt") as system_title:
    for line in system_title:
        system = line.strip()
        parts = system.split(" ")
        name = parts[0]
        id_number = parts[1]
        title = parts[2]
        salary = float(parts[3])
        pay_amount = salary / 24
        if title.lower() == "engineer":
            pay_amount += 1000
        print(f"{name} (ID: {id_number}), {title} - ${pay_amount:.2f}")