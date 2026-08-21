#Hector Malaga Rodriguez, 951, 21 de Agosto del 2026
#Ejercicio 1. La clase estadistica que calcula frecuencias, moda y hace histogramas

class Estadistica:
    def __init__(self, lista):
        self.lista = lista

    def frec_numero(self):
        frecuencia = []
        revisados = []

        for numero in self.lista:
            if numero not in revisados:
                total = self.lista.count(numero)
                frecuencia.append((numero, total))
                revisados.append(numero)

        return "lista de frecuencias", frecuencia

    def moda(self):
        moda_final = 0
        mod = 0
        revisados = []

        for moda in self.lista:
            if moda not in revisados:
                total = self.lista.count(moda)
                if total > moda_final:
                    moda_final = total
                    mod = moda
                revisados.append(moda)

        return "La moda es de", mod, "repitiendose", moda_final

    def histograma(self):
        revisados = []

        print("Histograma")
        for numero in self.lista:
            if numero not in revisados:
                total = self.lista.count(numero)
                print(numero, total*"*")
                revisados.append(numero)


lista_ejemplo = [1,1,1,2,2,3,5,5,6,7,8,9,9,9,10,10,2,8,7,9,9,6,1,6,7]
lista = Estadistica(lista_ejemplo)
print(lista.frec_numero())
print(lista.moda())
lista.histograma()

