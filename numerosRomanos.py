class NumerosRomanos:
    def __init__(self, numero:int) -> None:
        self.numero = numero



    def convertir(self):
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



def main():
    numero1 = NumerosRomanos(134)

    print(numero1.convertir())


main()

        