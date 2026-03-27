import tkinter as tk
from tkinter import messagebox

lista_compras = []
total_dia = 0

def abrir(menu):
    global total_dia
    v = tk.Toplevel()
    v.title("Ejercicio 3 - Tienda")
    v.geometry("550x450")

    def cerrar():
        v.destroy()
        menu.deiconify()

    tk.Label(v, text="Registro de compras", font=("Arial", 14)).pack(pady=10)

    tk.Label(v, text="Nombre del cliente:").pack()
    e_nombre = tk.Entry(v)
    e_nombre.pack()

    tk.Label(v, text="Mes de compra:").pack()
    e_mes = tk.Entry(v)
    e_mes.pack()

    tk.Label(v, text="Importe de compra:").pack()
    e_importe = tk.Entry(v)
    e_importe.pack()

    resultado = tk.Label(v)
    resultado.pack(pady=10)

    def validar_nombre(nombre):
        return nombre.replace(" ","").isalpha()

    def validar_mes(mes):
        meses_validos = ["enero","febrero","marzo","abril","mayo","junio",
                         "julio","agosto","septiembre","octubre","noviembre","diciembre"]
        return mes.lower() in meses_validos

    def validar_importe(importe):
        try:
            importe = float(importe)
            return 0 <= importe <= 100000
        except:
            return False

    def calcular():
        global total_dia
        nombre = e_nombre.get()
        mes = e_mes.get()
        importe = e_importe.get()

        if not validar_nombre(nombre):
            messagebox.showerror("Error", "Nombre inválido. Solo letras y espacios.")
            return
        if not validar_mes(mes):
            messagebox.showerror("Error", "Mes inválido.")
            return
        if not validar_importe(importe):
            messagebox.showerror("Error", "Importe inválido. Debe estar entre 0 y 100000.")
            return

        importe = float(importe)

        if mes.lower() == "octubre":
            descuento = 0.15
        elif mes.lower() == "diciembre":
            descuento = 0.20
        elif mes.lower() == "julio":
            descuento = 0.10
        else:
            descuento = 0

        total = importe * (1 - descuento)
        total_dia += total
        lista_compras.append((nombre, mes.capitalize(), importe, total))
        resultado.config(text=f"{nombre} - Total final: {total:.2f}")

    def mostrar_historial():
        texto = f"Total vendido: {total_dia:.2f}\nHistorial de compras:\n"
        for c in lista_compras:
            texto += f"{c[0]} | {c[1]} | Importe: {c[2]:.2f} | Total: {c[3]:.2f}\n"
        resultado.config(text=texto)

    tk.Button(v, text="Calcular total", command=calcular).pack(pady=5)
    tk.Button(v, text="Ver historial y total", command=mostrar_historial).pack(pady=5)
    tk.Button(v, text="Volver al menú", command=cerrar).pack(pady=20)