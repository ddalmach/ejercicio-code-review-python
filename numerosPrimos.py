
class numerosPrimo:

    def menu(self):
        print("**Ha elegido NumerosPrimos**")
        print("Ingrese un numero:")
        valor1= int(input("valor:"))
        return valor1


    def __init__(self):
        self.n=int(self.menu())
        self.obtener_primo()
        self.sumar_primos()

 
# Call variables with complete names
    def obtener_primo(self):
        array_primos = []
        if self.n > 0:
            for i in range(2, self.n):
                crec = 2
                es_primo = True
                while es_primo and crec < i:
                    if i % crec == 0:
                        es_primo = False
                    else:
                        crec += 1
                if es_primo:
                    array_primos.append(i)
                    # print(i)
        return print("Numeros Primos"+str(array_primos))

    def sumar_primos(self):
        suma_primos = 0
        if self.n > 0:
            for i in range(2, self.n):
                crec = 2
                es_primo = True
                while es_primo and crec < i:
                    if i % crec == 0:
                        es_primo = False
                    else:
                        crec += 1
                if es_primo:
                    suma_primos += i
                    # print(i)
        return print("Suma: "+str(suma_primos))
