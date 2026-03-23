import tkinter as tk
from tkinter import messagebox

lista_trabajadores = []

def abrir(menu):
    v = tk.Toplevel()
    v.title("Ejercicio 1 - Aumento de sueldos")
    v.geometry("550x450")

    def cerrar():
        v.destroy()
        menu.deiconify()

    tk.Label(v, text="Registro de trabajadores", font=("Arial", 14)).pack(pady=10)
    
    tk.Label(v, text="Nombre:").pack()
    e_nombre = tk.Entry(v)
    e_nombre.pack()

    tk.Label(v, text="Sueldo básico:").pack()
    e_sueldo = tk.Entry(v)
    e_sueldo.pack()

    resultado = tk.Label(v)
    resultado.pack(pady=10)

    def validar_nombre(nombre):
        return nombre.replace(" ","").isalpha()

    def validar_sueldo(sueldo):
        try:
            sueldo = float(sueldo)
            return sueldo >= 0
        except:
            return False

    def calcular_aumento(sueldo):
        if sueldo < 4000:
            return sueldo * 0.15
        elif sueldo <= 7000:
            return sueldo * 0.10
        else:
            return sueldo * 0.08

    def guardar():
        nombre = e_nombre.get()
        sueldo = e_sueldo.get()

        if not validar_nombre(nombre):
            messagebox.showerror("Error", "Nombre inválido. Solo letras y espacios.")
            return

        if not validar_sueldo(sueldo):
            messagebox.showerror("Error", "Sueldo inválido. Debe ser número positivo.")
            return

        sueldo = float(sueldo)
        aumento = calcular_aumento(sueldo)
        nuevo_sueldo = sueldo + aumento

        lista_trabajadores.append((nombre, sueldo, aumento, nuevo_sueldo))
        resultado.config(text=f"{nombre} - Nuevo sueldo: {nuevo_sueldo:.2f}")

    def mostrar_historial():
        texto = ""
        for t in lista_trabajadores:
            texto += f"{t[0]} | Sueldo: {t[1]:.2f} | Aumento: {t[2]:.2f} | Nuevo: {t[3]:.2f}\n"
        resultado.config(text=texto)

    tk.Button(v, text="Calcular aumento", command=guardar).pack(pady=5)
    tk.Button(v, text="Ver historial", command=mostrar_historial).pack(pady=5)
    tk.Button(v, text="Volver al menú", command=cerrar).pack(pady=20)