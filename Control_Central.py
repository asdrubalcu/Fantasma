# main.py
import time
from colorama import init, Fore, Style
from Tabla_secreta import Tabla_Secreta
from intercept import Interceptar

# Personalización

import pyfiglet

init(autoreset=True)  # Para que los colores no se queden activos

tabla = Tabla_Secreta()
interceptor = Interceptar()

def control_central():
    while True:
        print(Fore.YELLOW + pyfiglet.figlet_format("OSTA INTERCEPT", font="slant"))

        print(Fore.GREEN + "1. Generar Tablas Secretas")
        print(Fore.GREEN + "2. Intercepción de Señales")
        print(Fore.GREEN + "3. Validación de predicción")
        print(Fore.GREEN + "4. Reiniciar misión")
        print(Fore.GREEN + "5. Salir")

        opcion = input(Fore.RED + "\nSeleccione una opción: ")

        if opcion == '1':
            tabla.generar_tablas()
            interceptor.configurar_listas(tabla.tabla1, tabla.tabla2)

        elif opcion == '2':
            interceptor.generar_senal()

        elif opcion == '3':
            interceptor.ver_coincidencias()

        elif opcion == '4':
            tabla.reiniciar()
            interceptor.reiniciar()
            interceptor.configurar_listas(tabla.tabla1, tabla.tabla2)

        elif opcion == '5':
            print(Fore.MAGENTA + "\nAbandonando programa. Hasta pronto, agente.")
            time.sleep(3)
            break

        else:
            print(Fore.RED + "Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    control_central()