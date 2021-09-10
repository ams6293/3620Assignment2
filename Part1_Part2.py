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

def Divide():
    #loop for asking for valid input
    while True:
        try:
            number1 = float(input("Enter your first number "))
            number2 = float(input("Enter your second number "))
        except ValueError:
         #error if valid number isn't entered
            print("Sorry enter a valid number, remember you can't divide by zero")
            continue
        else:
            break
    try:
        print(f'{number1}/{number2}={number1/number2}')
    except ZeroDivisionError:
        print
        "You can't divide by zero!"


Divide()

