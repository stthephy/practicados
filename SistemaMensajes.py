import os

class Employee:
    def __init__(self, cedula, nombre, fecha_nacimiento, ciudad_nacimiento, telefono, correo, direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

class Message:
    def __init__(self, fecha, remitente, titulo, mensaje):
        self.fecha = fecha
        self.remitente = remitente
        self.titulo = titulo
        self.mensaje = mensaje

# Función para cargar los empleados desde el archivo "Empleados.txt"
def cargar_empleados():
    archivo_empleados = "Empleados.txt"

    if not os.path.isfile(archivo_empleados):
        # El archivo no existe, así que lo creamos con datos de ejemplo
        datos_empleados = [
            "Juan Perez,123456789,1990-01-15,Bogotá,1234567,jperez@email.com,Calle 123,Barrio A,Ciudad A,Urb A,101",
            "Maria Gomez,987654321,1985-05-20,Medellín,9876543,mgomez@email.com,Calle 456,Barrio B,Ciudad B,Urb B,202",
            # Agrega más datos de empleados si es necesario
        ]

        with open(archivo_empleados, "w") as file:
            for datos in datos_empleados:
                file.write(datos + "\n")

        print(f"Archivo '{archivo_empleados}' creado con datos de ejemplo.")

    empleados = []
    with open(archivo_empleados, "r") as file:
        for line in file:
            data = line.strip().split(',')
            empleado = Employee(data[1], data[0], data[2], data[3], data[4], data[5], data[6])
            empleados.append(empleado)

    return empleados

# Función para cargar las contraseñas desde el archivo "Password.txt"
def cargar_contrasenas():
    archivo_contrasenas = "Password.txt"

    if not os.path.isfile(archivo_contrasenas):
        # El archivo no existe, así que lo creamos con datos de ejemplo
        datos_contrasenas = [
            "123456789,contrasena_empleado,empleado",
            "987654321,contrasena_admin,administrador",
            # Agrega más datos de contraseñas si es necesario
        ]

        with open(archivo_contrasenas, "w") as file:
            for datos in datos_contrasenas:
                file.write(datos + "\n")

        print(f"Archivo '{archivo_contrasenas}' creado con datos de ejemplo.")

    contrasenas = {}
    with open(archivo_contrasenas, "r") as file:
        for line in file:
            cedula, contrasena, tipo = line.strip().split(',')
            contrasenas[cedula] = (contrasena, tipo)
    return contrasenas

def admin_main(empleados, contrasenas):
    while True:
        print("\nFuncionalidades para administradores:")
        print("1. Registrar Nuevo Usuario")
        print("2. Cambiar Contraseña de Usuario")
        print("3. Eliminar Usuario")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_usuario(empleados, contrasenas)
        elif opcion == "2":
            cambiar_contrasena(contrasenas)
        elif opcion == "3":
            eliminar_usuario(empleados, contrasenas)
        elif opcion == "4":
            # Implementa la lógica para guardar los cambios en los archivos antes de salir
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
def registrar_usuario(empleados, contrasenas):
    cedula = input("Cédula del nuevo usuario: ")
    if cedula in contrasenas:
        print("El usuario ya existe.")
    else:
        nombre = input("Nombre: ")
        fecha_nacimiento = input("Fecha de Nacimiento: ")
        ciudad_nacimiento = input("Ciudad de Nacimiento: ")
        telefono = input("Teléfono: ")
        correo = input("Correo Electrónico: ")
        direccion = input("Dirección: ")
        tipo = input("Tipo de usuario (empleado o administrador): ")

        empleado = Employee(cedula, nombre, fecha_nacimiento, ciudad_nacimiento, telefono, correo, direccion)
        contrasena = input("Contraseña: ")

        empleados[cedula] = empleado
        contrasenas[cedula] = (contrasena, tipo)
        print(f"Nuevo usuario registrado como {tipo}.")

# Función para cambiar la contraseña de un usuario
def cambiar_contrasena(contrasenas):
    cedula = input("Cédula del usuario al que deseas cambiar la contraseña: ")
    if cedula in contrasenas:
        nueva_contrasena = input("Nueva contraseña: ")
        contrasenas[cedula] = (nueva_contrasena, contrasenas[cedula][1])
        print("Contraseña cambiada con éxito.")
    else:
        print("El usuario no existe.")

# Función para eliminar un usuario del sistema
def eliminar_usuario(empleados, contrasenas):
    cedula = input("Cédula del usuario que deseas eliminar: ")
    if cedula in contrasenas:
        del contrasenas[cedula]
        del empleados[cedula]
        print("Usuario eliminado del sistema.")
    else:
        print("El usuario no existe.")
# Función para autenticar al usuario
# Función para autenticar al usuario
def autenticar(contrasenas):
    cedula = input("Cédula de identidad: ")
    contrasena = input("Contraseña: ")
    if cedula in contrasenas and contrasenas[cedula][0] == contrasena:
        tipo = contrasenas[cedula][1]
        return tipo
    else:
        return None

# Función principal
if __name__ == "__main__":
    empleados = cargar_empleados()
    contrasenas = cargar_contrasenas()
    while True:
        print("Bienvenido al sistema de mensajería electrónica interna.")
        tipo = autenticar(contrasenas)
        if tipo is not None:
            if tipo == "empleado":
                print(f"Autenticado como empleado")
                # Aquí puedes continuar con las funcionalidades para empleados
            elif tipo == "administrador":
                print(f"Autenticado como administrador")
                admin_main(empleados, contrasenas)
            break
        else:
            print("Cédula o contraseña incorrecta. Inténtalo de nuevo.")



    while True:
        print("Bienvenido al sistema de mensajería electrónica interna.")
        cedula, tipo = autenticar(contrasenas)
        if cedula is not None:
            print(f"Autenticado como {tipo}")
            # Aquí puedes continuar con las funcionalidades para empleados y administradores
class Inbox:
    def __init__(self):
        self.messages = []  # Lista de mensajes en la bandeja de entrada

    def agregar_mensaje(self, mensaje):
        self.messages.append(mensaje)

    def mostrar_bandeja_entrada(self):
        print("Bandeja de Entrada:")
        for i, mensaje in enumerate(self.messages):
            print(f"{i + 1}. Fecha: {mensaje.fecha}, Remitente: {mensaje.remitente}, Título: {mensaje.titulo}")

class ReadMessagesQueue:
    def __init__(self):
        self.messages = []  # Cola simple de mensajes leídos

    def agregar_mensaje(self, mensaje):
        self.messages.append(mensaje)

    def leer_mensaje(self):
        if not self.esta_vacia():
            return self.messages.pop(0)
        else:
            return None

    def esta_vacia(self):
        return len(self.messages) == 0

class DraftsStack:
    def __init(self):
        self.messages = []  # Pila simple de mensajes en borradores

    def agregar_borrador(self, mensaje):
        self.messages.append(mensaje)

    def obtener_ultimo_borrador(self):
        if not self.esta_vacia():
            return self.messages[-1]
        else:
            return None

    def eliminar_ultimo_borrador(self):
        if not self.esta_vacia():
            self.messages.pop()

    def esta_vacia(self):
        return len(self.messages) == 0




# Función principal para administradores
# Función principal para administradores