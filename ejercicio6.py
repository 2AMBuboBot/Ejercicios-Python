import tkinter as tk
from tkinter import messagebox

lista_intentos = []

def abrir(menu):
    v = tk.Toplevel()
    v.title("Ejercicio 6 - Registro de intentos")
    v.geometry("500x400")

    def cerrar():
        v.destroy()
        menu.deiconify()

    tk.Label(v, text="Ingrese número entre 0 y 20", font=("Arial", 14)).pack(pady=10)
    e_num = tk.Entry(v)
    e_num.pack()

    resultado = tk.Label(v)
    resultado.pack(pady=10)

    def validar():
        try:
            num = int(e_num.get())
        except:
            messagebox.showerror("Error", "Debe ingresar un número entero")
            return

        lista_intentos.append(num)
        if 0 < num < 20:
            resultado.config(text=f"Número correcto: {num}\nIntentos: {len(lista_intentos)}")
        else:
            messagebox.showerror("Error", "Número incorrecto")

    def mostrar_historial():
        texto = f"Intentos: {lista_intentos}"
        resultado.config(text=texto)

    tk.Button(v, text="Validar", command=validar).pack(pady=5)
    tk.Button(v, text="Ver historial", command=mostrar_historial).pack(pady=5)
    tk.Button(v, text="Volver al menú", command=cerrar).pack(pady=20)