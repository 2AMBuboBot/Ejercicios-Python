import tkinter as tk
from tkinter import messagebox

def abrir(menu):
    v = tk.Toplevel()
    v.title("Ejercicio 4 - Número menor que 10")
    v.geometry("500x400")

    def cerrar():
        v.destroy()
        menu.deiconify()

    intentos = 0

    tk.Label(v, text="Ingrese un número menor que 10", font=("Arial", 14)).pack(pady=10)
    e_num = tk.Entry(v)
    e_num.pack()

    resultado = tk.Label(v)
    resultado.pack(pady=10)

    def validar():
        nonlocal intentos
        try:
            num = int(e_num.get())
        except:
            messagebox.showerror("Error", "Debe ingresar un número entero")
            return

        intentos += 1
        if num < 10:
            resultado.config(text=f"Número correcto: {num}\nIntentos: {intentos}")
        else:
            messagebox.showerror("Error", "Número debe ser menor que 10")

    tk.Button(v, text="Validar", command=validar).pack(pady=5)
    tk.Button(v, text="Volver al menú", command=cerrar).pack(pady=20)