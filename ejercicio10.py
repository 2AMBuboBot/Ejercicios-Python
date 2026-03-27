import tkinter as tk
from tkinter import messagebox

lista_trabajadores = []

def abrir(menu):
    v = tk.Toplevel()
    v.title("Ejercicio 10 - Pago de trabajadores")
    v.geometry("550x450")

    def cerrar():
        v.destroy()
        menu.deiconify()

    tk.Label(v, text="Registro de trabajadores", font=("Arial", 14)).pack(pady=10)

    tk.Label(v, text="Nombre:").pack()
    e_nombre = tk.Entry(v)
    e_nombre.pack()

    tk.Label(v, text="Horas normales:").pack()
    e_horas = tk.Entry(v)
    e_horas.pack()

    tk.Label(v, text="Pago por hora normal:").pack()
    e_pago = tk.Entry(v)
    e_pago.pack()

    tk.Label(v, text="Horas extras:").pack()
    e_extra = tk.Entry(v)
    e_extra.pack()

    tk.Label(v, text="Número de hijos:").pack()
    e_hijos = tk.Entry(v)
    e_hijos.pack()

    resultado = tk.Label(v)
    resultado.pack(pady=10)

    def validar_nombre(nombre):
        return nombre.replace(" ", "").isalpha()

    def validar_numero(valor, entero=True, positivo=True):
        try:
            if entero:
                valor = int(valor)
            else:
                valor = float(valor)
            if positivo and valor < 0:
                return False
            return True
        except:
            return False

    def calcular_pago():
        nombre = e_nombre.get()
        horas = e_horas.get()
        pago = e_pago.get()
        extra = e_extra.get()
        hijos = e_hijos.get()

        if not validar_nombre(nombre):
            messagebox.showerror("Error", "Nombre inválido, solo letras y espacios")
            return
        if not validar_numero(horas):
            messagebox.showerror("Error", "Horas normales inválidas")
            return
        if not validar_numero(pago, entero=False):
            messagebox.showerror("Error", "Pago por hora inválido")
            return
        if not validar_numero(extra):
            messagebox.showerror("Error", "Horas extras inválidas")
            return
        if not validar_numero(hijos):
            messagebox.showerror("Error", "Número de hijos inválido")
            return

        horas = int(horas)
        pago = float(pago)
        extra = int(extra)
        hijos = int(hijos)

        # 🔥 VALIDACIONES NUEVAS
        if horas > 100:
            messagebox.showerror("Error", "Horas normales no pueden ser mayores a 100")
            return
        if extra > 100:
            messagebox.showerror("Error", "Horas extras no pueden ser mayores a 100")
            return
        if pago > 100000:
            messagebox.showerror("Error", "Pago por hora no puede ser mayor a 100000")
            return
        if hijos > 10:
            messagebox.showerror("Error", "Número de hijos no puede ser mayor a 10")
            return

        pago_normal = horas * pago
        pago_extra = extra * (pago * 1.5)
        bono = hijos * 0.5
        total = pago_normal + pago_extra + bono

        lista_trabajadores.append((nombre, pago_normal, pago_extra, bono, total))
        resultado.config(text=f"Total a pagar: {total:.2f}")

    def mostrar_reporte():
        texto = "Reporte de pagos:\n"
        for t in lista_trabajadores:
            texto += f"{t[0]} | Normal: {t[1]:.2f} | Extra: {t[2]:.2f} | Bono hijos: {t[3]:.2f} | Total: {t[4]:.2f}\n"
        resultado.config(text=texto)

    tk.Button(v, text="Calcular pago", command=calcular_pago).pack(pady=5)
    tk.Button(v, text="Mostrar reporte", command=mostrar_reporte).pack(pady=5)
    tk.Button(v, text="Volver al menú", command=cerrar).pack(pady=20)