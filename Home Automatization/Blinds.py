# ---> Imports <---

import math

# ---> Variables <---

T = float(input('Temp outside? '))
T_Stewie = float(input('Temp Stewies room? '))
T_Kamiel = float(input('Temp Kamiels room? '))
T_Parents = float(input('Temp parents room? '))
Rooms = [T_Stewie, T_Kamiel, T_Parents]

# ---> Calculations <--- 

if min(Rooms) >=T:
    # Close all blinds here
    print("All blinds closed")
elif max(Rooms) >=T:
    # Open all blinds here
    print('All blinds opened')
elif T > T_Stewie:
    # Close Stewies blind here
    print("Stewie's blind closed")
elif T > T:
    print('This is here to stop errors lmaooooooooooooooooooooooooooooooooo')