def get_windchill(temperature, speed):
    #Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
    windchill = 35.74 + 0.6215 * temperature  -35.75 * speed ** 0.16 + 0.4275 * temperature * speed ** 0.16
    return windchill

windchill = get_windchill (float(input("What is the temperature? ")))
print(windchill)
what_temperature = float(input("What is the temperature? "))
f_c = input("Fahrenheit or Celsius (F/C)? ").lower
