import tkinter as tk
from tkinter import messagebox

usuario_correcto = "admin"
clave_correcta = "1234"


def verificar_login():
    user = entrada_usuario.get()
    clave = entrada_clave.get()

    if user == usuario_correcto and clave == clave_correcta:
        ventana_login.destroy()
        menu_principal()
    else:
        messagebox.showerror("Error", "Datos incorrectos")


def menu_principal():
    global menu
    menu = tk.Tk()
    menu.title("MENÚ PRINCIPAL")
    menu.geometry("500x500")

    tk.Label(menu, text="MENÚ DE EJERCICIOS", font=("Arial", 16)).pack(pady=10)

    for i in range(1, 11):
        tk.Button(menu, text=f"Ejercicio {i}", width=25,
                  command=lambda i=i: abrir_ejercicio(i)).pack(pady=5)

    tk.Button(menu, text="Salir", bg="red", fg="white",
              command=menu.destroy).pack(pady=20)

    menu.mainloop()


def abrir_ejercicio(num):
    menu.withdraw()  

    if num == 1:
        import ejercicio1
        ejercicio1.abrir(menu)

    elif num == 2:
        import ejercicio2
        ejercicio2.abrir(menu)

    elif num == 3:
        import ejercicio3
        ejercicio3.abrir(menu)

    elif num == 4:
        import ejercicio4
        ejercicio4.abrir(menu)

    elif num == 5:
        import ejercicio5
        ejercicio5.abrir(menu)

    elif num == 6:
        import ejercicio6
        ejercicio6.abrir(menu)

    elif num == 7:
        import ejercicio7
        ejercicio7.abrir(menu)

    elif num == 8:
        import ejercicio8
        ejercicio8.abrir(menu)

    elif num == 9:
        import ejercicio9
        ejercicio9.abrir(menu)

    elif num == 10:
        import ejercicio10
        ejercicio10.abrir(menu)


ventana_login = tk.Tk()
ventana_login.title("Login")
ventana_login.geometry("300x200")

tk.Label(ventana_login, text="Usuario").pack()
entrada_usuario = tk.Entry(ventana_login)
entrada_usuario.pack()

tk.Label(ventana_login, text="Contraseña").pack()
entrada_clave = tk.Entry(ventana_login, show="*")
entrada_clave.pack()

tk.Button(ventana_login, text="Iniciar sesión", command=verificar_login).pack(pady=10)

ventana_login.mainloop()