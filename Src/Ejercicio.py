import random
import string
import pyperclip

# Genera una contraseña según las opciones seleccionadas por el usuario
def generar_contrasena(longitud, mayusculas, minusculas, numeros, especiales):

    caracteres = ""

    # Construcción del conjunto de caracteres disponibles
    if mayusculas:
        caracteres += string.ascii_uppercase

    if minusculas:
        caracteres += string.ascii_lowercase

    if numeros:
        caracteres += string.digits

    if especiales:
        caracteres += "!@#*$&.-"

    # Validación: debe existir al menos un tipo de carácter
    if caracteres == "":
        return None

    contrasena = ""

    # Generación aleatoria de la contraseña
    for i in range(longitud):
        contrasena += random.choice(caracteres)

    return contrasena


print("================================")
print("GENERADOR SEGURO DE CONTRASEÑAS")
print("================================")

while True:

    # Validación de longitud
    while True:
        try:
            longitud = int(input("\nIngrese la longitud de la contraseña: "))

            if longitud >= 8:
                break

            print("La longitud debe ser mayor o igual que 8.")

        except ValueError:
            print("Ingrese un número válido.")

    mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == "s"
    minusculas = input("¿Incluir minúsculas? (s/n): ").lower() == "s"
    numeros = input("¿Incluir números? (s/n): ").lower() == "s"
    especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == "s"

    contrasena = generar_contrasena(
        longitud,
        mayusculas,
        minusculas,
        numeros,
        especiales
    )

    if contrasena is None:
        print("\nDebe seleccionar al menos un tipo de carácter.")
    else:
        print("\nContraseña generada:")
        print(contrasena)

        # Permite copiar la contraseña generada al portapapeles
        copiar = input(
            "\n¿Desea copiar la contraseña al portapapeles? (s/n): "
        ).lower()

        if copiar == "s":
            pyperclip.copy(contrasena)
            print("Contraseña copiada al portapapeles.")

    repetir = input(
        "\n¿Desea generar otra contraseña? (s/n): "
    ).lower()
    
    if repetir != "s":
        print("\nPrograma finalizado.")
        break
