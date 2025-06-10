# Tabla_secreta.py

import random
import time
from colorama import init, Fore, Style

class Tabla_Secreta:
    def __init__(self):
        self.tabla1 = []
        self.tabla2 = []
        self.usados = []

    def generar_tablas(self):
        self.tabla1 = []
        self.tabla2 = []
        self.usados = []

        # Generar 5 números únicos para la primera tabla
        while len(self.tabla1) < 5:
            num = random.randint(1, 20)
            if num not in self.usados:
                self.tabla1.append(num)
                self.usados.append(num)

        # Generar 5 números únicos para la segunda tabla, sin repetir con la primera
        while len(self.tabla2) < 5:
            num = random.randint(1, 20)
            if num not in self.usados:
                self.tabla2.append(num)
                self.usados.append(num)

        print(Fore.GREEN + "\nAlgoritmos empleados. Tablas generadas:")
        print(Fore.GREEN + "Tabla 1: " + str(self.tabla1))
        print(Fore.GREEN + "Tabla 2: " + str(self.tabla2))
        time.sleep(5)

    def reiniciar(self):
        self.tabla1 = []
        self.tabla2 = []
        self.usados = []
        print("Misión reiniciada. Tablas borradas.")
        time.sleep(2)