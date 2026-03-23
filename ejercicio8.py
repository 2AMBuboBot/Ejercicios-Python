import tkinter as tk
from tkinter import messagebox

lista_numeros = []

def abrir(menu):
    v = tk.Toplevel()
    v.title("Ejercicio 8 - Suma acumulativa")
    v.geometry("500x400")

    def cerrar():
        v.destroy()
        menu.deiconify()

    suma = 0

    tk.Label(v, text="Ingrese números (0 para detener)", font=("Arial", 14)).pack(pady=10)
    e_num = tk.Entry(v)
    e_num.pack()

    resultado = tk.Label(v)
    resultado.pack(pady=10)

    def agregar_numero():
        nonlocal suma
        try:
            num = int(e_num.get())
        except:
            messagebox.showerror("Error", "Debe ingresar un número entero")
            return

        if num != 0:
            lista_numeros.append(num)
            suma += num
            resultado.config(text=f"Suma acumulada: {suma}")
        else:
            resultado.config(text=f"Números ingresados: {lista_numeros}\nCantidad: {len(lista_numeros)}\nSuma total: {suma}")

    tk.Button(v, text="Agregar número", command=agregar_numero).pack(pady=5)
    tk.Button(v, text="Volver al menú", command=cerrar).pack(pady=20)