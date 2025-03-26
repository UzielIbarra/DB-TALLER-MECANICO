import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import dbUsuario as db
import usuario as user
import pieza as pieza_module
import dbPieza as db_pieza
import reparacion as rep
import db_reparacion as db_rep
from datetime import datetime
import cliente
import db_cliente as db_cliente
import vehiculo
import db_vehiculo

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        
        # Crear el frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Crear el login frame
        self.create_login_frame()
        
        # Agregar créditos en la parte inferior
        credits_frame = ttk.Frame(self.root, padding="5")
        credits_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
        ttk.Label(
            credits_frame, 
            text="Creado por: Uziel Hashid Ibarra Rivas",
            font=('Arial', 8, 'italic')
        ).grid(row=0, column=0, pady=5)

    def create_login_frame(self):
        self.login_frame = ttk.Frame(self.root, padding="10")
        self.login_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.login_frame, text="Usuario:").grid(row=0, column=0, sticky=tk.W)
        self.username = ttk.Entry(self.login_frame)
        self.username.grid(row=0, column=1, sticky=(tk.W, tk.E))

        ttk.Label(self.login_frame, text="Contraseña:").grid(row=1, column=0, sticky=tk.W)
        self.password = ttk.Entry(self.login_frame, show="*")
        self.password.grid(row=1, column=1, sticky=(tk.W, tk.E))

        self.login_button = ttk.Button(self.login_frame, text="Iniciar Sesión", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2)

    def login(self):
        db_user = db.DbUsuario()
        usr = user.Usuario()
        usr.setUsername(self.username.get())
        usr.setPassword(self.password.get())
        
        authenticated_user = db_user.autenticar(usr)
        if authenticated_user:
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def create_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.main_menu = ttk.Frame(self.root, padding="10")
        self.main_menu.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        buttons = ["Usuarios", "Clientes", "Vehículos", "Piezas", "Reparaciones", "Salir"]
        for idx, text in enumerate(buttons):
            button = ttk.Button(self.main_menu, text=text, command=lambda t=text: self.menu_action(t))
            button.grid(row=0, column=idx, padx=5, pady=5)

    def menu_action(self, action):
        if action == "Usuarios":
            self.create_user_interface()
        elif action == "Clientes":
            self.create_customer_interface()
        elif action == "Vehículos":
            self.create_vehicle_interface()
        elif action == "Piezas":
            self.create_parts_interface()
        elif action == "Reparaciones":
            self.create_repairs_interface()
        elif action == "Salir":
            self.root.quit()

    def create_user_interface(self):
        self.clear_window()
        
        self.user_frame = ttk.Frame(self.root, padding="10")
        self.user_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.user_frame, text="Ingrese ID a buscar:").grid(row=0, column=0, sticky=tk.W)
        self.search_id = ttk.Entry(self.user_frame)
        self.search_id.grid(row=0, column=1, sticky=(tk.W, tk.E))

        self.search_button = ttk.Button(self.user_frame, text="Search", command=self.search_user)
        self.search_button.grid(row=0, column=2)

        ttk.Label(self.user_frame, text="USUARIO ID:").grid(row=1, column=0, sticky=tk.W)
        self.user_id = ttk.Entry(self.user_frame)
        self.user_id.grid(row=1, column=1, sticky=(tk.W, tk.E))

        ttk.Label(self.user_frame, text="Nombre:").grid(row=2, column=0, sticky=tk.W)
        self.nombre = ttk.Entry(self.user_frame)
        self.nombre.grid(row=2, column=1, sticky=(tk.W, tk.E))

        ttk.Label(self.user_frame, text="Username:").grid(row=3, column=0, sticky=tk.W)
        self.username_entry = ttk.Entry(self.user_frame)
        self.username_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

        ttk.Label(self.user_frame, text="Password:").grid(row=4, column=0, sticky=tk.W)
        self.password_entry = ttk.Entry(self.user_frame)
        self.password_entry.grid(row=4, column=1, sticky=(tk.W, tk.E))

        ttk.Label(self.user_frame, text="Perfil:").grid(row=5, column=0, sticky=tk.W)
        self.perfil = ttk.Combobox(self.user_frame, values=["Mecanico", "Admin", "Auxiliar"])
        self.perfil.grid(row=5, column=1, sticky=(tk.W, tk.E))

        self.button_frame = ttk.Frame(self.user_frame, padding="10")
        self.button_frame.grid(row=6, column=0, columnspan=2, pady=10)

        self.new_button = ttk.Button(self.button_frame, text="Nuevo", command=self.new_user)
        self.new_button.grid(row=0, column=0, padx=5)

        self.save_button = ttk.Button(self.button_frame, text="Salvar", command=self.save_user)
        self.save_button.grid(row=0, column=1, padx=5)

        self.cancel_button = ttk.Button(self.button_frame, text="Cancelar", command=self.create_main_menu)
        self.cancel_button.grid(row=0, column=2, padx=5)

        self.edit_button = ttk.Button(self.button_frame, text="Editar", command=self.edit_user)
        self.edit_button.grid(row=0, column=3, padx=5)

    def new_user(self):
        self.user_id.delete(0, tk.END)
        self.nombre.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.perfil.set("")

    def search_user(self):
        db_user = db.DbUsuario()
        usr = user.Usuario()
        usr.setUsuario_id(self.search_id.get())
        found_user = db_user.search(usr)
        if found_user:
            self.user_id.delete(0, tk.END)
            self.user_id.insert(0, found_user.getUsuario_id())
            self.nombre.delete(0, tk.END)
            self.nombre.insert(0, found_user.getNombre())
            self.username_entry.delete(0, tk.END)
            self.username_entry.insert(0, found_user.getUsername())
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, found_user.getPassword())
            self.perfil.set(found_user.getPerfil())
        else:
            messagebox.showerror("Error", "User not found")

    def save_user(self):
        db_user = db.DbUsuario()
        usr = user.Usuario()
        usr.setUsuario_id(self.user_id.get())
        usr.setNombre(self.nombre.get())
        usr.setUsername(self.username_entry.get())
        usr.setPassword(self.password_entry.get())
        usr.setPerfil(self.perfil.get())

        db_user.save(usr)
        messagebox.showinfo("Info", "User saved successfully")

    def edit_user(self):
        db_user = db.DbUsuario()
        usr = user.Usuario()
        usr.setUsuario_id(self.user_id.get())
        usr.setNombre(self.nombre.get())
        usr.setUsername(self.username_entry.get())
        usr.setPassword(self.password_entry.get())
        usr.setPerfil(self.perfil.get())

        db_user.edit(usr)
        messagebox.showinfo("Info", "User edited successfully")

    def create_parts_interface(self):
        self.clear_window()
        
        self.parts_frame = ttk.Frame(self.root, padding="10")
        self.parts_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.parts_frame, text="Ingrese ID a buscar:").grid(row=0, column=0, sticky=tk.W)
        self.search_part_id = ttk.Entry(self.parts_frame)
        self.search_part_id.grid(row=0, column=1, sticky=(tk.W, tk.E))

        self.search_part_button = ttk.Button(self.parts_frame, text="Search", command=self.search_part)
        self.search_part_button.grid(row=0, column=2)

        ttk.Label(self.parts_frame, text="ID:").grid(row=1, column=0, sticky=tk.W)
        self.part_id = ttk.Entry(self.parts_frame)
        self.part_id.grid(row=1, column=1, sticky=(tk.W, tk.E))

        ttk.Label(self.parts_frame, text="Descripcion:").grid(row=2, column=0, sticky=tk.W)
        self.description = ttk.Entry(self.parts_frame)
        self.description.grid(row=2, column=1, sticky=(tk.W, tk.E))

        ttk.Label(self.parts_frame, text="Stock:").grid(row=3, column=0, sticky=tk.W)
        self.stock = ttk.Entry(self.parts_frame)
        self.stock.grid(row=3, column=1, sticky=(tk.W, tk.E))

        self.parts_button_frame = ttk.Frame(self.parts_frame, padding="10")
        self.parts_button_frame.grid(row=4, column=0, columnspan=2, pady=10)

        self.new_part_button = ttk.Button(self.parts_button_frame, text="Nuevo", command=self.new_part)
        self.new_part_button.grid(row=0, column=0, padx=5)

        self.save_part_button = ttk.Button(self.parts_button_frame, text="Guardar", command=self.save_part)
        self.save_part_button.grid(row=0, column=1, padx=5)

        self.cancel_part_button = ttk.Button(self.parts_button_frame, text="Cancelar", command=self.create_main_menu)
        self.cancel_part_button.grid(row=0, column=2, padx=5)

        self.edit_part_button = ttk.Button(self.parts_button_frame, text="Editar", command=self.edit_part)
        self.edit_part_button.grid(row=0, column=3, padx=5)

        self.remove_part_button = ttk.Button(self.parts_button_frame, text="Remover", command=self.remove_part)
        self.remove_part_button.grid(row=0, column=4, padx=5)

    def new_part(self):
        self.part_id.delete(0, tk.END)
        self.description.delete(0, tk.END)
        self.stock.delete(0, tk.END)

    def search_part(self):
        db_part = db_pieza.DbPieza()
        part = pieza_module.Pieza()
        part.setId(self.search_part_id.get())
        found_part = db_part.search(part)
        if found_part:
            self.part_id.delete(0, tk.END)
            self.part_id.insert(0, found_part.getId())
            self.description.delete(0, tk.END)
            self.description.insert(0, found_part.getDescripcion())
            self.stock.delete(0, tk.END)
            self.stock.insert(0, found_part.getStock())
        else:
            messagebox.showerror("Error", "Part not found")

    def save_part(self):
        db_part = db_pieza.DbPieza()
        part = pieza_module.Pieza()
        part.setId(self.part_id.get())
        part.setDescripcion(self.description.get())
        part.setStock(self.stock.get())
        
        if int(part.getStock()) < 0:
            messagebox.showerror("Error", "Stock cannot be negative")
            return

        if db_part.is_duplicate(part):
            messagebox.showerror("Error", "Part already exists")
            return

        db_part.save(part)
        messagebox.showinfo("Info", "Part saved successfully")

    def edit_part(self):
        db_part = db_pieza.DbPieza()
        part = pieza_module.Pieza()
        part.setId(self.part_id.get())
        part.setDescripcion(self.description.get())
        part.setStock(self.stock.get())

        if int(part.getStock()) < 0:
            messagebox.showerror("Error", "Stock cannot be negative")
            return

        db_part.edit(part)
        messagebox.showinfo("Info", "Part edited successfully")

    def remove_part(self):
        db_part = db_pieza.DbPieza()
        part = pieza_module.Pieza()
        part.setId(self.part_id.get())

        db_part.remove(part)
        messagebox.showinfo("Info", "Part removed successfully")

    def create_repairs_interface(self):
        self.clear_window()
        
        self.repairs_frame = ttk.Frame(self.root, padding="10")
        self.repairs_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.repairs_frame, text="Ingrese Folio a buscar:").grid(row=0, column=0, sticky=tk.W)
        self.search_folio = ttk.Entry(self.repairs_frame)
        self.search_folio.grid(row=0, column=1, sticky=(tk.W, tk.E))

        self.search_repair_button = ttk.Button(self.repairs_frame, text="Search", command=self.search_repair)
        self.search_repair_button.grid(row=0, column=2)

        ttk.Label(self.repairs_frame, text="Folio:").grid(row=1, column=0, sticky=tk.W)
        self.folio = ttk.Entry(self.repairs_frame)
        self.folio.grid(row=1, column=1, sticky=(tk.W, tk.E))

        ttk.Label(self.repairs_frame, text="Matricula:").grid(row=2, column=0, sticky=tk.W)
        self.matricula = ttk.Entry(self.repairs_frame)
        self.matricula.grid(row=2, column=1, sticky=(tk.W, tk.E))

        ttk.Label(self.repairs_frame, text="Fecha Entrada:").grid(row=3, column=0, sticky=tk.W)
        self.fecha_entrada = ttk.Entry(self.repairs_frame)
        self.fecha_entrada.grid(row=3, column=1, sticky=(tk.W, tk.E))

        ttk.Label(self.repairs_frame, text="Fecha Salida:").grid(row=4, column=0, sticky=tk.W)
        self.fecha_salida = ttk.Entry(self.repairs_frame)
        self.fecha_salida.grid(row=4, column=1, sticky=(tk.W, tk.E))

        ttk.Label(self.repairs_frame, text="Pieza ID:").grid(row=5, column=0, sticky=tk.W)
        self.pieza_id = ttk.Entry(self.repairs_frame)
        self.pieza_id.grid(row=5, column=1, sticky=(tk.W, tk.E))
        
        ttk.Label(self.repairs_frame, text="Cantidad:").grid(row=6, column=0, sticky=tk.W)
        self.cantidad = ttk.Entry(self.repairs_frame)
        self.cantidad.grid(row=6, column=1, sticky=(tk.W, tk.E))

        self.repairs_button_frame = ttk.Frame(self.repairs_frame, padding="10")
        self.repairs_button_frame.grid(row=7, column=0, columnspan=2, pady=10)

        self.new_repair_button = ttk.Button(self.repairs_button_frame, text="Nuevo", command=self.new_repair)
        self.new_repair_button.grid(row=0, column=0, padx=5)

        self.save_repair_button = ttk.Button(self.repairs_button_frame, text="Guardar", command=self.save_repair)
        self.save_repair_button.grid(row=0, column=1, padx=5)

        self.cancel_repair_button = ttk.Button(self.repairs_button_frame, text="Cancelar", command=self.create_main_menu)
        self.cancel_repair_button.grid(row=0, column=2, padx=5)

        self.edit_repair_button = ttk.Button(self.repairs_button_frame, text="Editar", command=self.edit_repair)
        self.edit_repair_button.grid(row=0, column=3, padx=5)

        self.remove_repair_button = ttk.Button(self.repairs_button_frame, text="Remover", command=self.remove_repair)
        self.remove_repair_button.grid(row=0, column=4, padx=5)

    def new_repair(self):
        self.folio.delete(0, tk.END)
        self.matricula.delete(0, tk.END)
        self.fecha_entrada.delete(0, tk.END)
        self.fecha_salida.delete(0, tk.END)
        self.pieza_id.delete(0, tk.END)
        self.cantidad.delete(0, tk.END)

    def search_repair(self):
        db_repair = db_rep.DbReparacion()
        repair = rep.Reparacion()
        repair.setfolio(self.search_folio.get())
        found_repair = db_repair.search(repair.getfolio())
        if found_repair:
            self.folio.delete(0, tk.END)
            self.folio.insert(0, found_repair.getfolio())
            self.matricula.delete(0, tk.END)
            self.matricula.insert(0, found_repair.getmatricula())
            self.fecha_entrada.delete(0, tk.END)
            self.fecha_entrada.insert(0, found_repair.getfecha_entrada())
            self.fecha_salida.delete(0, tk.END)
            self.fecha_salida.insert(0, found_repair.getfecha_salida())
            self.pieza_id.delete(0, tk.END)
            self.pieza_id.insert(0, found_repair.getpieza_id())
            self.cantidad.delete(0, tk.END)
            self.cantidad.insert(0, found_repair.getcantidad())
        else:
            messagebox.showerror("Error", "Repair not found")

    def save_repair(self):
        # Validate required fields
        if not all([self.folio.get(), self.matricula.get(), self.fecha_entrada.get(), 
                    self.pieza_id.get(), self.cantidad.get()]):
            messagebox.showerror("Error", "All fields are required except Fecha Salida")
            return
        
        try:
            cantidad = int(self.cantidad.get())
            if cantidad <= 0:
                messagebox.showerror("Error", "Cantidad must be positive")
                return
        except ValueError:
            messagebox.showerror("Error", "Cantidad must be a number")
            return

        # Validate date format
        try:
            if self.fecha_entrada.get():
                datetime.strptime(self.fecha_entrada.get(), '%Y-%m-%d')
            if self.fecha_salida.get():
                datetime.strptime(self.fecha_salida.get(), '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Date format should be YYYY-MM-DD")
            return

        # Continue with existing save logic
        db_repair = db_rep.DbReparacion()
        repair = rep.Reparacion()
        repair.setfolio(self.folio.get())
        repair.setmatricula(self.matricula.get())
        repair.setfecha_entrada(self.fecha_entrada.get())
        repair.setfecha_salida(self.fecha_salida.get())
        repair.setpieza_id(self.pieza_id.get())
        repair.setcantidad(self.cantidad.get())

        # Validate if the part exists and has enough stock
        db_part = db_pieza.DbPieza()
        part = pieza_module.Pieza()
        part.setId(repair.getpieza_id())
        found_part = db_part.search(part)
        
        if not found_part:
            messagebox.showerror("Error", "Part not found")
            return
            
        if int(found_part.getStock()) < int(repair.getcantidad()):
            messagebox.showerror("Error", "Not enough stock available")
            return

        try:
            db_repair.save(repair)
            messagebox.showinfo("Info", "Repair saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save repair: {str(e)}")

    def edit_repair(self):
        db_repair = db_rep.DbReparacion()
        repair = rep.Reparacion()
        repair.setfolio(self.folio.get())
        repair.setmatricula(self.matricula.get())
        repair.setfecha_entrada(self.fecha_entrada.get())
        repair.setfecha_salida(self.fecha_salida.get())
        repair.setpieza_id(self.pieza_id.get())
        repair.setcantidad(self.cantidad.get())

        db_repair.edit(repair)
        messagebox.showinfo("Info", "Repair edited successfully")

    def remove_repair(self):
        db_repair = db_rep.DbReparacion()
        repair = rep.Reparacion()
        repair.setfolio(self.folio.get())

        db_repair.remove(repair)
        messagebox.showinfo("Info", "Repair removed successfully")

    def create_customer_interface(self):
        self.clear_window()
        
        self.customer_frame = ttk.Frame(self.root, padding="10")
        self.customer_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.customer_frame, text="Ingrese ID a buscar:").grid(row=0, column=0, sticky=tk.W)
        self.search_customer_id = ttk.Entry(self.customer_frame)
        self.search_customer_id.grid(row=0, column=1, sticky=(tk.W, tk.E))

        self.search_customer_button = ttk.Button(self.customer_frame, text="Buscar", command=self.search_customer)
        self.search_customer_button.grid(row=0, column=2)

        # Campos del cliente
        fields = [
            ("ID:", "customer_id"),
            ("Nombre:", "customer_name"),
            ("Teléfono:", "customer_phone"),
            ("RFC:", "customer_rfc"),
            ("Email:", "customer_email")
        ]

        for i, (label, attr) in enumerate(fields, start=1):
            ttk.Label(self.customer_frame, text=label).grid(row=i, column=0, sticky=tk.W)
            setattr(self, attr, ttk.Entry(self.customer_frame))
            getattr(self, attr).grid(row=i, column=1, sticky=(tk.W, tk.E))

        # Botones
        self.customer_button_frame = ttk.Frame(self.customer_frame, padding="10")
        self.customer_button_frame.grid(row=len(fields)+1, column=0, columnspan=2, pady=10)

        buttons = [
            ("Nuevo", self.new_customer),
            ("Guardar", self.save_customer),
            ("Cancelar", self.create_main_menu),
            ("Editar", self.edit_customer),
            ("Eliminar", self.remove_customer)
        ]

        for i, (text, command) in enumerate(buttons):
            ttk.Button(self.customer_button_frame, text=text, command=command).grid(row=0, column=i, padx=5)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def new_customer(self):
        self.customer_id.delete(0, tk.END)
        self.customer_name.delete(0, tk.END)
        self.customer_phone.delete(0, tk.END)
        self.customer_rfc.delete(0, tk.END)
        self.customer_email.delete(0, tk.END)

    def search_customer(self):
        db_customer = db_cliente.DbCliente()
        customer = cliente.Cliente()
        customer.setId(self.search_customer_id.get())
        found_customer = db_customer.search(customer)
        if found_customer:
            self.customer_id.delete(0, tk.END)
            self.customer_id.insert(0, found_customer.getId())
            self.customer_name.delete(0, tk.END)
            self.customer_name.insert(0, found_customer.getNombre())
            self.customer_phone.delete(0, tk.END)
            self.customer_phone.insert(0, found_customer.getTelefono())
            self.customer_rfc.delete(0, tk.END)
            self.customer_rfc.insert(0, found_customer.getRfc())
            self.customer_email.delete(0, tk.END)
            self.customer_email.insert(0, found_customer.getEmail())
        else:
            messagebox.showerror("Error", "Cliente no encontrado")

    def save_customer(self):
        db_customer = db_cliente.DbCliente()
        customer = cliente.Cliente()
        customer.setId(self.customer_id.get())
        customer.setNombre(self.customer_name.get())
        customer.setTelefono(self.customer_phone.get())
        customer.setRfc(self.customer_rfc.get())
        customer.setEmail(self.customer_email.get())
        
        db_customer.save(customer)
        messagebox.showinfo("Info", "Cliente guardado exitosamente")

    def edit_customer(self):
        db_customer = db_cliente.DbCliente()
        customer = cliente.Cliente()
        customer.setId(self.customer_id.get())
        customer.setNombre(self.customer_name.get())
        customer.setTelefono(self.customer_phone.get())
        customer.setRfc(self.customer_rfc.get())
        customer.setEmail(self.customer_email.get())
        
        db_customer.edit(customer)
        messagebox.showinfo("Info", "Cliente editado exitosamente")

    def remove_customer(self):
        db_customer = db_cliente.DbCliente()
        customer = cliente.Cliente()
        customer.setId(self.customer_id.get())
        
        db_customer.remove(customer)
        messagebox.showinfo("Info", "Cliente eliminado exitosamente")

    def create_vehicle_interface(self):
        self.clear_window()
        
        self.vehicle_frame = ttk.Frame(self.root, padding="10")
        self.vehicle_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Búsqueda
        ttk.Label(self.vehicle_frame, text="Ingrese Matrícula a buscar:").grid(row=0, column=0, sticky=tk.W)
        self.search_matricula = ttk.Entry(self.vehicle_frame)
        self.search_matricula.grid(row=0, column=1, sticky=(tk.W, tk.E))

        self.search_vehicle_button = ttk.Button(self.vehicle_frame, text="Buscar", command=self.search_vehicle)
        self.search_vehicle_button.grid(row=0, column=2)

        # Campos del vehículo
        fields = [
            ("Matrícula:", "vehicle_matricula"),
            ("Cliente ID:", "vehicle_cliente"),
            ("Marca:", "vehicle_marca"),
            ("Modelo:", "vehicle_modelo"),
            ("Color:", "vehicle_color")
        ]

        for i, (label, attr) in enumerate(fields, start=1):
            ttk.Label(self.vehicle_frame, text=label).grid(row=i, column=0, sticky=tk.W)
            setattr(self, attr, ttk.Entry(self.vehicle_frame))
            getattr(self, attr).grid(row=i, column=1, sticky=(tk.W, tk.E))

        # Botones
        self.vehicle_button_frame = ttk.Frame(self.vehicle_frame, padding="10")
        self.vehicle_button_frame.grid(row=len(fields)+1, column=0, columnspan=2, pady=10)

        buttons = [
            ("Nuevo", self.new_vehicle),
            ("Guardar", self.save_vehicle),
            ("Cancelar", self.create_main_menu),
            ("Editar", self.edit_vehicle),
            ("Eliminar", self.remove_vehicle)
        ]

        for i, (text, command) in enumerate(buttons):
            ttk.Button(self.vehicle_button_frame, text=text, command=command).grid(row=0, column=i, padx=5)

    def new_vehicle(self):
        self.vehicle_matricula.delete(0, tk.END)
        self.vehicle_cliente.delete(0, tk.END)
        self.vehicle_marca.delete(0, tk.END)
        self.vehicle_modelo.delete(0, tk.END)
        self.vehicle_color.delete(0, tk.END)

    def search_vehicle(self):
        db_vehicle = db_vehiculo.DbVehiculo()
        vehicle = vehiculo.Vehiculo()
        vehicle.setMatricula(self.search_matricula.get())
        found_vehicle = db_vehicle.search(vehicle)
        if found_vehicle:
            self.vehicle_matricula.delete(0, tk.END)
            self.vehicle_matricula.insert(0, found_vehicle.getMatricula())
            self.vehicle_cliente.delete(0, tk.END)
            self.vehicle_cliente.insert(0, found_vehicle.getCliente())
            self.vehicle_marca.delete(0, tk.END)
            self.vehicle_marca.insert(0, found_vehicle.getMarca())
            self.vehicle_modelo.delete(0, tk.END)
            self.vehicle_modelo.insert(0, found_vehicle.getModelo())
            self.vehicle_color.delete(0, tk.END)
            self.vehicle_color.insert(0, found_vehicle.getColor())
        else:
            messagebox.showerror("Error", "Vehículo no encontrado")

    def save_vehicle(self):
        db_vehicle = db_vehiculo.DbVehiculo()
        vehicle = vehiculo.Vehiculo()
        vehicle.setMatricula(self.vehicle_matricula.get())
        vehicle.setCliente(self.vehicle_cliente.get())
        vehicle.setMarca(self.vehicle_marca.get())
        vehicle.setModelo(self.vehicle_modelo.get())
        vehicle.setColor(self.vehicle_color.get())
        
        db_vehicle.save(vehicle)
        messagebox.showinfo("Info", "Vehículo guardado exitosamente")

    def edit_vehicle(self):
        db_vehicle = db_vehiculo.DbVehiculo()
        vehicle = vehiculo.Vehiculo()
        vehicle.setMatricula(self.vehicle_matricula.get())
        vehicle.setCliente(self.vehicle_cliente.get())
        vehicle.setMarca(self.vehicle_marca.get())
        vehicle.setModelo(self.vehicle_modelo.get())
        vehicle.setColor(self.vehicle_color.get())
        
        db_vehicle.edit(vehicle)
        messagebox.showinfo("Info", "Vehículo editado exitosamente")

    def remove_vehicle(self):
        db_vehicle = db_vehiculo.DbVehiculo()
        vehicle = vehiculo.Vehiculo()
        vehicle.setMatricula(self.vehicle_matricula.get())
        
        db_vehicle.remove(vehicle)
        messagebox.showinfo("Info", "Vehículo eliminado exitosamente")

# Add this at the bottom of main.py
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
