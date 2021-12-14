import numpy as np

class gasolinera:

    def __init__(self):
        self.principal()

    def principal(self):
        # Decoración: Nombre del Algoritmo
        # Constantes
        # Call the variables with significant names
        LITXG = 3.785
        PRECIOXL = 4.50
        
        # Entradas
        # Call the variables with complete names
        consu = float(input("Ingresar consumo: "))
        
        # Proceso
        total = consu * LITXG * PRECIOXL
        
        # Salida
        print("\nSALIDA: ")
        print("-------------------------------------------------------")
        print("Total:", total)
