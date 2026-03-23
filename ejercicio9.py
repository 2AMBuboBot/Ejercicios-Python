import tkinter as tk
from tkinter import messagebox

lista_numeros = []
suma = 0

def abrir(menu):
    v = tk.Toplevel()
    v.title("Ejercicio 9 - Suma hasta pasar 100")
    v.geometry("500x400")

    def cerrar():
        v.destroy()
        menu.deiconify()

    tk.Label(v, text="Ingrese números enteros", font=("Arial", 14)).pack(pady=10)
    e_num = tk.Entry(v)
    e_num.pack()

    resultado = tk.Label(v)
    resultado.pack(pady=10)

    def agregar():
        global suma
        try:
            num = int(e_num.get())
        except:
            messagebox.showerror("Error", "Debe ingresar un número entero")
            return

        lista_numeros.append(num)
        suma += num

        if suma > 100:
            resultado.config(text=f"Lista: {lista_numeros}\nCantidad: {len(lista_numeros)}\nSuma final: {suma}")
        else:
            resultado.config(text=f"Suma parcial: {suma}")

    tk.Button(v, text="Agregar número", command=agregar).pack(pady=5)
    tk.Button(v, text="Volver al menú", command=cerrar).pack(pady=20)