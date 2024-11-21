# Uzraksti programmu, kurā  dators izvēlas 100 skaitļus robežās no 101 līdz 500. Izvēlētie skaitļi tiek izvadīti terminālī.

import random       # Aizmirsa uzrakstīt random 

for i in range (101,501,1):
    random_skaitlis=random.randint(101,501)    # Nepareizs mainīgais
    print(random_skaitlis)
