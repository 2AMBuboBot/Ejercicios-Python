import tkinter as tk
from tkinter import messagebox

def abrir(menu):
    v = tk.Toplevel()
    v.title("Ejercicio 7 - Suma hasta N")
    v.geometry("500x400")

    def cerrar():
        v.destroy()
        menu.deiconify()

    tk.Label(v, text="Ingrese un número positivo N", font=("Arial", 14)).pack(pady=10)
    e_n = tk.Entry(v)
    e_n.pack()

    resultado = tk.Label(v)
    resultado.pack(pady=10)

    def calcular_suma():
        try:
            n = int(e_n.get())
        except:
            messagebox.showerror("Error", "Debe ingresar un número entero")
            return

        if n <= 0:
            messagebox.showerror("Error", "Número debe ser positivo")
            return

        suma = 0
        secuencia = ""
        for i in range(1, n+1):
            suma += i
            secuencia += str(i) + " "

        resultado.config(text=f"Secuencia: {secuencia}\nSuma total: {suma}")

    tk.Button(v, text="Calcular suma", command=calcular_suma).pack(pady=5)
    tk.Button(v, text="Volver al menú", command=cerrar).pack(pady=20)