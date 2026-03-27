import tkinter as tk
from tkinter import messagebox

lista_visitantes = []
total_recaudado = 0

def abrir(menu):
    global total_recaudado
    v = tk.Toplevel()
    v.title("Ejercicio 2 - Parque")
    v.geometry("550x450")

    def cerrar():
        v.destroy()
        menu.deiconify()

    tk.Label(v, text="Registro de visitantes", font=("Arial", 14)).pack(pady=10)

    tk.Label(v, text="Nombre:").pack()
    e_nombre = tk.Entry(v)
    e_nombre.pack()

    tk.Label(v, text="Edad:").pack()
    e_edad = tk.Entry(v)
    e_edad.pack()

    tk.Label(v, text="Cantidad de juegos:").pack()
    e_juegos = tk.Entry(v)
    e_juegos.pack()

    resultado = tk.Label(v)
    resultado.pack(pady=10)

    def validar_nombre(nombre):
        return nombre.replace(" ", "").isalpha()

    def validar_edad(edad):
        try:
            edad = int(edad)
            return 0 <= edad <= 100
        except:
            return False

    def validar_juegos(juegos):
        try:
            juegos = int(juegos)
            return 0 <= juegos <= 100000
        except:
            return False

    def calcular_pago():
        global total_recaudado
        nombre = e_nombre.get()
        edad = e_edad.get()
        juegos = e_juegos.get()

        if not validar_nombre(nombre):
            messagebox.showerror("Error", "Nombre inválido. Solo letras y espacios.")
            return
        if not validar_edad(edad):
            messagebox.showerror("Error", "Edad inválida. Debe estar entre 0 y 100.")
            return
        if not validar_juegos(juegos):
            messagebox.showerror("Error", "Juegos inválido. Debe estar entre 0 y 100000.")
            return

        edad = int(edad)
        juegos = int(juegos)
        precio = juegos * 50

        if edad < 10:
            descuento = 0.25
        elif edad <= 17:
            descuento = 0.10
        else:
            descuento = 0

        total = precio * (1 - descuento)
        total_recaudado += total
        lista_visitantes.append((nombre, edad, juegos, total))
        resultado.config(text=f"{nombre} - Total a pagar: {total:.2f}")

    def mostrar_total():
        texto = f"Total recaudado: {total_recaudado:.2f}\nHistorial:\n"
        for vst in lista_visitantes:
            texto += f"{vst[0]} | Edad: {vst[1]} | Juegos: {vst[2]} | Pagar: {vst[3]:.2f}\n"
        resultado.config(text=texto)

    tk.Button(v, text="Calcular pago", command=calcular_pago).pack(pady=5)
    tk.Button(v, text="Ver total e historial", command=mostrar_total).pack(pady=5)
    tk.Button(v, text="Volver al menú", command=cerrar).pack(pady=20)