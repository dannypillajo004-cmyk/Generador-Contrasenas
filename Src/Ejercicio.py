import random
import string
import pyperclip

# Función para generar la contraseña
def generar_contrasena(longitud, mayusculas, minusculas, numeros, especiales):

    caracteres = ""

    if mayusculas:
        caracteres += string.ascii_uppercase

    if minusculas:
        caracteres += string.ascii_lowercase

    if numeros:
        caracteres += string.digits

    if especiales:
       caracteres += "!@#*$&.-"

    if caracteres == "":
        return None

    contrasena = ""

    for i in range(longitud):
        contrasena += random.choice(caracteres)

    return contrasena


print("================================")
print("GENERADOR SEGURO DE CONTRASEÑAS")
print("================================")

while True:

    longitud = int(input("\nIngrese la longitud de la contraseña: "))

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

        # Copiar al portapapeles
        copiar = input("\n¿Desea copiar la contraseña al portapaspeles? (s/n): ").lower()

        if copiar == "s":
            pyperclip.copy(contrasena)
            print("✔ Contraseña copiada al portapapeles")

    repetir = input(
        "\n¿Desea generar otra contraseña? (s/n): "
    ).lower()

    if repetir != "s":
        print("\nPrograma finalizado.")
        break