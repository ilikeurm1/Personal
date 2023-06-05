# Code only supports 2 numbers for now :) if the calc has a variable amount of usable numbers

# ---> imports <---

import math

# ---> Variables <---

Number1 = float()
Number2 = float()
Answer = None


Calculations = ["Multiply", "Divide", "Add", "Subtract", "Powers", "Sqrt", "Cbrt", "Pytha", "HDI", "BMI"]
NCalculation = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
ChosenCalc = None


Rounder = None
Power1 = None
Power2 = None
PythaAdd = None
inM = None


# ---> Calculator :) <---

while True:
       print('1. Multiply / 2. Divide / 3. Add / 4. Subtract / 5. Powers / 6. Sqrt / 7. Cbrt / 8. Pytha / 9. HDI / 10. BMI')
       Calculation = input(f'What kind of calculation do u want to do? 1. Multiply / 2. Divide / 3. Add / 4. Subtract / 5. Powers / 6. Sqrt / 7. Cbrt / 8. Pytha / 9. HDI / 10. BMI (USE THE NUMBERS!): ')
       if Calculation in Calculations or Calculation in NCalculation:
              print('WORKED!')
              print(f'Calculation {Calculation} chosen!')
              if 'Multiply' in Calculation or '1' in  Calculation:  # Multiplication 

                     # ---> Inputs <---
              
                     Number1 = float(input('What is the first number you want to multiply: '))
                     Number2 = float(input('What is the second number you want to multiply: '))

                     # ---> Calculations <---

                     Answer = Number1 * Number2

                     # ---> Output <---

                     print(f'{Number1} times {Number2} is {Number1 * Number2}')

              elif 'Divide' in Calculation or '2' in Calculation: # Division
                            
                     # ---> Inputs <---
                            
                     Number1 = float(input('What is the number you want to divide: '))
                     Number2 = float(input('What number do you want to divide by: '))
                     Rounder = int(input('To how many decimals do you want to round: '))
                            
                     # ---> Calculations <---
                            
                     if Number1 == 0 or Number2 == 0:
                            print(f'Very funny!')
                     else: 
                            Answer = round(Number1 / Number2, Rounder)

                     # ---> Output <---

                     print(f'{Number1} divided by {Number2} is {Answer}')

              elif 'Add' in Calculation or '3' in Calculation: # Addition
                            
                     # ---> Inputs <---
                            
                     Number1 = float(input('What is the first number you want to add: '))
                     Number2 = float(input('What is the second number you want to add: '))

                     # ---> Calculations <---

                     Answer = Number1 + Number2

                     # ---> Output <---

                     print(f'{Number1} plus {Number2} is {Answer}')

              elif 'Subtract' in Calculation or '4' in Calculation: # Subtraction
                            
                     # ---> Inputs <---
                            
                     Number1 = float(input('What is the first number you want to subtract: '))
                     Number2 = float(input('What is the second number you want to subtract: '))

                     # ---> Calculations <---

                     Answer = Number1 - Number2

                     # ---> Output <---

                     print(f'{Number1} minus {Number2} is {Answer}')

              elif 'Powers' in Calculation or '5' in Calculation: # Powers
                     
                     # ---> Inputs <---
                     
                     Number1 = float(input('What is the base number that you want to use: '))
                     Number2 = float(input('What is the power: '))

                     # ---> Calculations <---

                     Answer = Number1 ** Number2

                     # ---> Output <---

                     print(f'{Number1} to the power {Number2} is {Answer}')

              elif 'Sqrt' in Calculation or '6' in Calculation: # Squarroot

                     # ---> Inputs <---

                     Number1 = float(input('What is the base number that you want to use: '))
                     
                     # ---> Calculations <---
                     
                     Answer = math.sqrt(Number1)

                     # ---> Output <---

                     print(f'The squarroot of {Number1} is {Answer}')
                     
              elif 'Cbrt' in Calculation or '7' in Calculation: # Cuberoot

                     # ---> Inputs <---

                     Number1 = float(input('What is the base number that you want to use: '))
                     Rounder = int(input('To how many decimals do you want to round: '))

                     # ---> Calculations <---

                     Answer = math.pow(Number1, (1 / 3))

                     # ---> Output <---

                     print(f'The cuberoot of {Number1} is {round(Answer, Rounder)}')



              elif 'Pytha' in Calculation or '8' in Calculation: # Pythagoras

                     # ---> Inputs <---

                     Number1 = float(input('What is the length of side 1 (in cm): '))
                     Number2 = float(input('What is the length of side 2 (in cm): '))
                     Rounder = int(input('To how many decimals do you want to round: '))

                     # ---> Calculations <---

                     Power1 = math.pow(Number1, 2)
                     Power2 = math.pow(Number2, 2)
                     PythaAdd = Power1 + Power2
                     Answer = round(math.sqrt(PythaAdd), Rounder)

                     # ---> Output <---

                     print(f'The diagonal is {Answer} cm long')
                     inM = input('Do you want the length in meters? (y/n): ')
                     if 'y' in inM:
                            print(f'The diagonal in meters is {Answer / 100} m long')
                     elif 'n' in inM:
                            print(f'Ok!')
                     else:
                            print(f'Invalid input!')



              elif 'HDI' in Calculation or '9' in Calculation: # HDI
                     print(f'Calculation {Calculation} chosen!')

                     # ---> Inputs <---

                     Country = input('Country: ')
                     LE = float(input('LE: '))
                     MYS = float(input('MYS: '))
                     EYS = float(input('EYS: '))
                     GNIpc = float(input('GNIpc: '))

                     # ---> Calculations <---

                     LEI = (LE - 20) / (82.3 - 20)
                     MYSI = MYS / 13.2
                     EYSI = EYS / 20.6
                     EI = math.sqrt(MYSI * EYSI) / 0.951
                     II = (math.log(GNIpc) - math.log(100)) / (math.log(107721) - math.log(100))
                     HDI = math.pow(LEI * EI * II, 1/3)

                     # ---> Output <---

                     print(f"The HDI of {Country} is {HDI:.3f}.")



              elif 'BMI' in Calculation or '10' in Calculation: # BMI
                     # ---> Inputs <---

                     Weight = float(input('Weight in kg: '))
                     Length = float(input('Lengte in cm: '))

                     # ---> Calculations <---

                     LengthM = Length / 100
                     RBMI = Weight / (LengthM ** 2)
                     BMI = round(RBMI, 1)

                     # ---> Output <---

                     print('Je hebt een BMI van', BMI)
                     if BMI < 18.5: # ondergewicht
                            print('Je hebt ondergewicht')
                     elif BMI <= 25: # Normaal
                            print('Je hebt een normaal gewicht')
                     elif BMI <= 30: # Je hebt overgewicht
                            print('Je hebt overgewicht')
                     elif BMI <= 35: #- obesitas
                            print('Je hebt obesitas')
                     else: # ernstige obesitas
                            print('Je hebt ernstige obesitas')



       else:
              print('Can not do that type of calculation (yet).')


       # ---> Run again <---
       again = input("Run again? (y/n): ")
       if 'y' in again:
              continue
       elif 'n' in again:
              print("Good bye!")
              print("")
              print("Thank you for using this calculator!")
              print("")
              print("Credits:")
              print("")
              print("Programming: Matthijs Duhoux")
              print("")
              print("Formulas: The internet / Matthijs Duhoux")
              break
       else:
              print("Invalid Input")
              break