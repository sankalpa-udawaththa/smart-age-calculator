name = input("Enter your name:    ")

print(f"Hello {name.upper()}" )

birth_year = input("Enter your Birth year:   ")

age =  int(2021) - int(birth_year)
month = age * int(12)
week = month * int(4)
day = month * int(30)
Hours = day * int(24)
minute = Hours * int(60)
sec = minute * int(60)
milsec = sec * int(1000)


print("your " + str(age) + " years old")
print("      months:-  " + str(month) + " (Approx)")
print("       Weeks:-  " + str(week) + " (Approx)")
print("        days:-  " + str(day) + " (Approx)")
print("       Hours:-  " + str(Hours) + " (Approx)")
print("      Minute:-  " + str(minute) + " (Approx)")
print("     Seconds:-  " + str(sec) + " (Approx)")
print(" Miliseconds:-  " + str(milsec) + " (Approx)")
print('''
       HHHHHHHHHHHHHHHH  H       H     HH     HH      H  H      H
              H          H       H    H  H    H H     H  H    H
              H          H       H   H    H   H  H    H  H  H 
              H          HHHHHHHHH  HHHHHHHH  H   H   H  HH
              H          H       H  H      H  H    H  H  H  H
              H          H       H  H      H  H     H H  H    H 
              H          H       H  H      H  H      HH  H      H
''')

