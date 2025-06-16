import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyodbc

# 🔧 CONEXIÓN A SQL SERVER
conexion = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=26.95.196.200;'
    'DATABASE=CASTILLONV2;'
    'UID=sa;'
    'PWD=Castillon1234+'
)

def login():
    usuario = entry_usuario.get().strip()
    clave = entry_clave.get().strip()

    cursor = conexion.cursor()
    query = """
        SELECT COUNT(*) 
        FROM USUARIO 
        WHERE LOGEO COLLATE Latin1_General_CI_AI = ? 
          AND CLAVE = ? 
          AND ESTADO = 1
    """
    cursor.execute(query, (usuario, clave))
    resultado = cursor.fetchone()[0]

    if resultado == 1:
        ventana.withdraw()  # Oculta login

        nueva_ventana = tk.Toplevel()
        nueva_ventana.title("Productos disponibles")

        tk.Label(nueva_ventana, text="Listado de productos", font=("Arial", 12, "bold")).pack(pady=5)

        # Tabla tipo Treeview
        tree = ttk.Treeview(nueva_ventana, columns=("nombre", "descripcion", "precio", "marca"), show="headings", height=15)
        tree.pack(padx=10, pady=10)

        tree.heading("nombre", text="Nombre")
        tree.heading("descripcion", text="Descripción")
        tree.heading("precio", text="Precio")
        tree.heading("marca", text="Marca")

        tree.column("nombre", width=200)
        tree.column("descripcion", width=300)
        tree.column("precio", width=80, anchor=tk.CENTER)
        tree.column("marca", width=100, anchor=tk.CENTER)

        try:
            cursor.execute("SELECT NOMPRODUCTO, DESCRIPCION, PRECIO, MARCA FROM PRODUCTO WHERE ESTADO = 1")
            for fila in cursor.fetchall():
                tree.insert("", tk.END, values=(fila[0], fila[1], f"${fila[2]:.2f}", fila[3]))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los productos: {str(e)}")

        # Botón cerrar sesión
        def cerrar_sesion():
            nueva_ventana.destroy()
            ventana.deiconify()

        tk.Button(nueva_ventana, text="Cerrar sesión", command=cerrar_sesion).pack(pady=10)

    else:
        messagebox.showerror("Error", "Credenciales incorrectas o usuario inactivo.")

# 🎨 INTERFAZ PRINCIPAL
ventana = tk.Tk()
ventana.title("Login - CASTILLONV2")

tk.Label(ventana, text="Usuario:").grid(row=0, column=0, padx=10, pady=10)
entry_usuario = tk.Entry(ventana)
entry_usuario.grid(row=0, column=1)

tk.Label(ventana, text="Clave:").grid(row=1, column=0, padx=10, pady=10)
entry_clave = tk.Entry(ventana, show="*")
entry_clave.grid(row=1, column=1)

tk.Button(ventana, text="Iniciar sesión", command=login).grid(row=2, columnspan=2, pady=10)

ventana.mainloop()
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyodbc

# 🔧 CONEXIÓN A SQL SERVER
conexion = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=26.95.196.200;'
    'DATABASE=CASTILLONV2;'
    'UID=sa;'
    'PWD=Castillon1234+'
)

def login():
    usuario = entry_usuario.get().strip()
    clave = entry_clave.get().strip()

    cursor = conexion.cursor()
    query = """
        SELECT COUNT(*) 
        FROM USUARIO 
        WHERE LOGEO COLLATE Latin1_General_CI_AI = ? 
          AND CLAVE = ? 
          AND ESTADO = 1
    """
    cursor.execute(query, (usuario, clave))
    resultado = cursor.fetchone()[0]

    if resultado == 1:
        ventana.withdraw()  # Oculta login

        nueva_ventana = tk.Toplevel()
        nueva_ventana.title("Productos disponibles")

        tk.Label(nueva_ventana, text="Listado de productos", font=("Arial", 12, "bold")).pack(pady=5)

        # Tabla tipo Treeview
        tree = ttk.Treeview(nueva_ventana, columns=("nombre", "descripcion", "precio", "marca"), show="headings", height=15)
        tree.pack(padx=10, pady=10)

        tree.heading("nombre", text="Nombre")
        tree.heading("descripcion", text="Descripción")
        tree.heading("precio", text="Precio")
        tree.heading("marca", text="Marca")

        tree.column("nombre", width=200)
        tree.column("descripcion", width=300)
        tree.column("precio", width=80, anchor=tk.CENTER)
        tree.column("marca", width=100, anchor=tk.CENTER)

        try:
            cursor.execute("SELECT NOMPRODUCTO, DESCRIPCION, PRECIO, MARCA FROM PRODUCTO WHERE ESTADO = 1")
            for fila in cursor.fetchall():
                tree.insert("", tk.END, values=(fila[0], fila[1], f"${fila[2]:.2f}", fila[3]))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los productos: {str(e)}")

        # Botón cerrar sesión
        def cerrar_sesion():
            nueva_ventana.destroy()
            ventana.deiconify()

        tk.Button(nueva_ventana, text="Cerrar sesión", command=cerrar_sesion).pack(pady=10)

    else:
        messagebox.showerror("Error", "Credenciales incorrectas o usuario inactivo.")

# 🎨 INTERFAZ PRINCIPAL
ventana = tk.Tk()
ventana.title("Login - CASTILLONV2")

tk.Label(ventana, text="Usuario:").grid(row=0, column=0, padx=10, pady=10)
entry_usuario = tk.Entry(ventana)
entry_usuario.grid(row=0, column=1)

tk.Label(ventana, text="Clave:").grid(row=1, column=0, padx=10, pady=10)
entry_clave = tk.Entry(ventana, show="*")
entry_clave.grid(row=1, column=1)

tk.Button(ventana, text="Iniciar sesión", command=login).grid(row=2, columnspan=2, pady=10)

ventana.mainloop()
