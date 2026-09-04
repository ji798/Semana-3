#Almacenar las edades de 6 estudiantes
edades = []

def AlmacenarEdades(edad):
    edades.append(edad)

def mostrarEdades():
    return edades

for i in range(10):
    while True:
        try:
            edad = int(input(f"Estudiante #{i + 1} dime tu edad: "))
            if edad < 0:
                print("La edad no puede ser negativa. Intente nuevamente.")
                continue
            AlmacenarEdades(edad)
            break
        except ValueError:
            print("Se debe ingresar un numero entero.")
