# This is my first actual Python script that i made on my own (no exercise) so its very bad code :)


# Code only supports 2 numbers for now :)

# ---> imports <---

import math

# ---> Variables <---

Number1 = float()
Number2 = float()
Calculations = ["Multiply", "Divide", "Add", "Subtract", "Powers", "Sqrt", "Cbrt"]
NCalculation = ["1", "2", "3", "4", "5", "6", "7"]
Rounder = None
Squarroot = None
Cuberoot = None

# ---> Calculator :) <---

while True:
       Calculation = input('What kind of calculation do u want to do? 1. Multiply / 2. Divide / 3. Add / 4. Subtract / 5. Powers / 6. Sqrt (You can use the numbers aswell!): ')
       if Calculation in Calculations or Calculation in NCalculation:
              print('WORKED!')
              if 'Multiply' in Calculation or '1' in  Calculation:  # Multiplication 
                     print(f'Calculation {Calculation} chosen!')
                     Number1 = float(input('What is the first number you want to multiply: '))
                     Number2 = float(input('What is the second number you want to multiply: '))
                     print(f'{Number1} times {Number2} is {Number1 * Number2}')
              elif 'Divide' in Calculation or '2' in Calculation: # Division
                     print(f'Calculation {Calculation} chosen!')
                     Number1 = float(input('What is the number you want to divide: '))
                     Number2 = float(input('What number do you want to divide by: '))
                     Rounder = int(input('To how many decimals do you want to round: '))
                     if Number2 == 0 or Number1 == 0:
                            print(f'Very funny!')
                     else: 
                            print(f'{Number1} divided by {Number2} is {round(Number1 / Number2, Rounder)}')
              elif 'Add' in Calculation or '3' in Calculation: # Addition
                     print(f'Calculation {Calculation} chosen!')
                     Number1 = float(input('What is the first number you want to add: '))
                     Number2 = float(input('What is the second number you want to add: '))
                     print(f'{Number1} plus {Number2} is {Number1 + Number2}')
              elif 'Subtract' in Calculation or '4' in Calculation: # Subtraction
                     print(f'Calculation {Calculation} chosen!')
                     Number1 = float(input('What is the first number you want to subtract: '))
                     Number2 = float(input('What is the second number you want to subtract: '))
                     print(f'{Number1} minus {Number2} is {Number1 - Number2}')
              elif 'Powers' in Calculation or '5' in Calculation: # Powers
                     print(f'Calculation {Calculation} chosen!')
                     Number1 = float(input('What is the base number that you want to use: '))
                     Number2 = float(input('What is the power: '))
                     print(f'{Number1} to the power {Number2} is {Number1 ** Number2}')
              elif 'Sqrt' in Calculation or '6' in Calculation: # Squarroot
                     print(f'Calculation{Calculation} chosen!') 
                     Number1 = float(input('What is the base number that you want to use: '))
                     Squarroot = math.sqrt(Number1)
                     print(f'The squarroot of {Number1} is {Squarroot}')
       else:
              print('Can not do that type of calculation (yet).')
       again = input("Run again? (y/n): ")
       if 'y' in again:
              continue
       elif 'n' in again:
              print("Good bye!")
              break
       else:
              print("Invalid Input")
              break