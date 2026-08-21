#Hector Malaga Rodriguez, 951, 21 de Agosto del 2026
#Ejercicio 2. Historial de una hoja de calculo super basico
from tkinter import simpledialog, messagebox


pila_inicial = [("A1","Hola"),("B1","Adios"),("C1","Salud"),("D1", "Zapato")]
ultimo_eliminado = 0

def cambios_nuevos():
    celda = simpledialog.askstring("Cambio","Celda a modificar: ")
    cambio = simpledialog.askstring("Cambio","Modificacion: ")
    afectacion = (celda, cambio)
    pila_inicial.append(afectacion)

def deshacer_ultimo():
    ultimo_eliminado = pila_inicial.pop(-1)
    messagebox.showinfo("Deshacer",f"Valor eliminado {ultimo_eliminado}")

def historial_completo():
    messagebox.showinfo("historial",f"Lista del historial actual\n\n {pila_inicial}")

while True:
    opcion = 0
    opcion = simpledialog.askinteger("Menu",f"1. Hacer cambios\n"
                       "2. Deshacer último cambios\n"
                       "3. Ver historial completo\n"
                       "4. salir")
    if opcion == 1:
        cambios_nuevos()
    elif opcion == 2:
        deshacer_ultimo()
    elif opcion == 3:
        historial_completo()
    elif opcion == 4:
        messagebox.showinfo("Adios","Programa terminado")
        break
    else:
        messagebox.showerror("ERROR2","Opcion invalida")