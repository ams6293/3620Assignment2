def BMICalc():
    #loop for asking for valid input
  while True:  
     try:
         height = float(input("Enter your height in meters "))
         weight = float(input("Enter your weight in kg "))

     except InputValueError:
         #error if valid number isn't entered
         print("Sorry enter a valid number")
         continue
     else:
        break

  print("Your BMI is.. ")
  print('{:.2f}'.format(weight/ height ** 2))

BMICalc()

