#Calcular la edad de una persona y decir si es mayor o menor de edad
from datetime import date
from colorama import Fore, Style

try:
    año_nac = int(input("Dime el año en que naciste: "))

    edad = date.today().year - año_nac

    if edad >= 18:
        print(Fore.GREEN + "Usted es mayor de edad" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Eres menor de edad" + Style.RESET_ALL)

except ValueError:
    print(Fore.RED + "Por favor, ingrese un año válido." + Style.RESET_ALL)
