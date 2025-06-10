# intercept.py

import random
import time
from colorama import init, Fore, Style
from alive_progress import alive_bar  # Importamos barra animada

class Interceptar:
    def __init__(self):
        self.tabla1 = []
        self.tabla2 = []
        self.senales_enviadas = []
        self.coincidencias = []
        self.coincidencias_t1 = []
        self.coincidencias_t2 = []

    def configurar_listas(self, l1, l2):
        self.tabla1 = l1
        self.tabla2 = l2
        self.coincidencias_t1 = []
        self.coincidencias_t2 = []

    def generar_senal(self):
        if not self.tabla1 or not self.tabla2:
            print(Fore.RED + "Error: No se han generado las tablas secretas. Use la opción 1 primero.")
            time.sleep(2)
            return

        print(Fore.YELLOW + "\n--- Iniciando interceptación automática de señales ---")

        total_restantes = 20 - len(self.senales_enviadas)
        with alive_bar(total_restantes, title= Fore.BLUE + "Intercepción en progreso") as bar:
            while True:
                if len(self.senales_enviadas) >= 20:
                    print(Fore.YELLOW + "Ya se interceptaron todas las señales posibles.")
                    break

                # Genero señal única
                while True:
                    senal = random.randint(1, 20)
                    if senal not in self.senales_enviadas:
                        self.senales_enviadas.append(senal)
                        break

                time.sleep(2)  # Simulo espescucha real
                print(Fore.YELLOW + "\nSeñal interceptada: " + str(senal))

                resultado = ""
                if senal in self.tabla1:
                    resultado = Fore.GREEN + "Coincidencia en Tabla 1."
                elif senal in self.tabla2:
                    resultado = Fore.GREEN + "Coincidencia en Tabla 2."
                else:
                    resultado = Fore.RED + "No hay coincidencia."

                print(resultado)
                self.coincidencias.append((senal, resultado))

                # Registrar coincidencias por tabla
                if senal in self.tabla1 and senal not in self.coincidencias_t1:
                    self.coincidencias_t1.append(senal)
                if senal in self.tabla2 and senal not in self.coincidencias_t2:
                    self.coincidencias_t2.append(senal)

                bar()  # Avanza la barra de progreso

                # Verificar si se descifró alguna tabla
                if set(self.tabla1) == set(self.coincidencias_t1):
                    print(Fore.GREEN + "\nMensaje interceptado. El algoritmo ha descifrado la Tabla de Predicción 1.")
                    print(Fore.GREEN + "Código secreto: " + str(self.tabla1))
                    time.sleep(5)
                    break
                elif set(self.tabla2) == set(self.coincidencias_t2):
                    print(Fore.GREEN + "\nMensaje interceptado. El algoritmo ha descifrado la Tabla de Predicción 2.")
                    print(Fore.GREEN + "Código secreto: " + str(self.tabla2))
                    time.sleep(5)
                    break

    def ver_coincidencias(self):
        if not self.coincidencias:
            print(Fore.YELLOW + "No hay señales interceptadas aún.")
            time.sleep(3)
            return

        print(Fore.YELLOW + "\nValidación de predicción paso a paso:")
        for senal, resultado in self.coincidencias:
            print(Fore.YELLOW + "- Señal interceptada: " + str(senal))
            print(Fore.YELLOW + "  Resultado: " + resultado)
            print(Fore.YELLOW + "------------------------------")

        # Mostrar si ya se completó alguna tabla
        if set(self.tabla1) == set(self.coincidencias_t1):
            print(Fore.GREEN + "\nPredicción completada: El algoritmo de la Tabla 1 ha logrado descifrar el código.")
            print(Fore.GREEN + "Código Secreto: ",self.tabla1)

        elif set(self.tabla2) == set(self.coincidencias_t2):
            print(Fore.GREEN + "\nPredicción completada: El algoritmo de la Tabla 1 ha logrado descifrar el código.")
            print(Fore.GREEN + "Código Secreto: ",self.tabla2)

        else:
            print(Fore.YELLOW + "\nAún no se ha descifrado completamente ninguna tabla.")
        time.sleep(5)

    def reiniciar(self):
        self.senales_enviadas = []
        self.coincidencias = []
        self.coincidencias_t1 = []
        self.coincidencias_t2 = []
        self.tabla1 = []
        self.tabla2 = []
        print(Fore.RED + "\nMisión reiniciada automáticamente.")
