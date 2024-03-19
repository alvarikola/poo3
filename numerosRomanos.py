class NumerosRomanos:
    def __init__(self, numero:int, romano:str) -> None:
        self.numero = numero
        self.romano = romano



    def convertirDecimales(self):
        listaRomanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        listaNumeros = [1000, 900, 500, 400,  100,  90,  50,  40,    10,  9,    5,   4,     1]
        numeroRomano = ''
        i = 0
        while self.numero > 0:
            if self.numero == listaNumeros[0]:
                self.numero = listaRomanos[0]
                return self.numero
            
            if self.numero - listaNumeros[i] >= 0:
                numeroRomano += listaRomanos[i]
                self.numero -= listaNumeros[i]
            else:
                i += 1
        return numeroRomano
    

    def convertirRomanos(self):
        listaRomanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        listaNumeros = [1000, 900, 500, 400,  100,  90,  50,  40,    10,  9,    5,   4,     1]
        numeroDecimal = 0
        i = ""
        while self.romano:
            if self.romano == listaRomanos[0]:
                self.romano = listaNumeros[0]
                return self.romano
            
            if self.romano - listaRomanos[i] >= 0:
                numeroDecimal += listaNumeros[i]
                self.romano -= listaRomanos[i]
            else:
                i += 1
        return numeroDecimal



def main():
    numero1 = NumerosRomanos(134, "I")

    print(numero1.convertirDecimales())
    print(numero1.convertirRomanos())


main()

        