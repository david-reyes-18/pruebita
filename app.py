import tkinter as tk

def saludar():
    label.config(text="¡Hola desde Tkinter y GitHub Actions!")

# Crear ventana
ventana = tk.Tk()
ventana.title("App de Prueba")
ventana.geometry("300x150")

# Widgets
label = tk.Label(ventana, text="Presiona el botón")
label.pack(pady=10)

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack(pady=5)

# Ejecutar bucle principal
if __name__ == "__main__":
    ventana.mainloop()
