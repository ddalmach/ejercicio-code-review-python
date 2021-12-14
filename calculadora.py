#Respetar la nomenclatura
class calculadora:

    def menu(self):
        print("**Ha elegido calculadora**")
        print("Que transaccion desea realizar:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Divicion")
        valor1= int(input("valor:"))
        return valor1


    def __init__(self):
        self.valor1=int(input("Ingrese primer valor:"))
        self.valor2=int(input("Ingrese segundo valor:"))
        self.valor=int(self.menu())

        if self.valor==1:
            self.add()
        if self.valor == 2:
            self.substract()
        if self.valor == 3:
            self.multiply()
        if self.valor == 4:
            self.divide()

    def add(self):
        suma=self.valor1+self.valor2
        print("La suma es",suma)

    def substract(self):
        resta=self.valor1-self.valor2
        print("La rersta es",resta)

    def multiply(self):
        multi=self.valor1*self.valor2
        print("El producto es",multi)
# no se esta controlando la división para 0
    def divide(self):
        divi=self.valor1/self.valor2
        print("La division es",divi)
