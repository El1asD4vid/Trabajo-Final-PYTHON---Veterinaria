import os

# --- INICIO DE LA CONFIGURACIÓN DE RUTAS ---
# Detecta la carpeta donde se encuentra este archivo de Python
ruta_del_script = os.path.dirname(os.path.abspath(__file__))

# Establece esa carpeta como directorio de trabajo
os.chdir(ruta_del_script)
# --- FIN DE LA CONFIGURACIÓN ---


def mostrar_menu():
    print("\n====================================")
    print("   VETERINARIA 'PATAS Y BIGOTES'")
    print("====================================")
    print("1. Registrar mascota")
    print("2. Registrar turno")
    print("3. Registrar atención médica")
    print("4. Mostrar mascotas")
    print("5. Mostrar turnos")
    print("6. Mostrar atenciones")
    print("7. Estadísticas")
    print("0. Salir")
    print("====================================")


def registrar_mascota():
    print("\n--- Registrar mascota ---")

    id_mascota = input("Ingrese el ID de la mascota: ")
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie: ")
    edad = input("Ingrese la edad: ")
    duenio = input("Ingrese el nombre del dueño: ")

    archivo = open("mascotas.txt", "a")

    archivo.write(id_mascota + ";" +
                  nombre + ";" +
                  especie + ";" +
                  edad + ";" +
                  duenio + "\n")

    archivo.close()

    print("\n¡Mascota registrada correctamente!")


def mostrar_mascotas():
    print("\n--- Lista de mascotas ---")

    try:
        archivo = open("mascotas.txt", "r")

        for linea in archivo:
            print(linea.strip())

        archivo.close()

    except FileNotFoundError:
        print("No hay mascotas registradas.")


def mostrar_atenciones():
    print("\n--- Lista de atenciones médicas ---")
    try:
        archivo = open("atenciones.txt", "r")
        for linea in archivo:
            print(linea.strip())
        archivo.close()
    except FileNotFoundError:
        print("No hay atenciones médicas registradas.")


def registrar_turno():
    print("\n--- Registrar turno ---")

    id_mascota = input("Ingrese el ID de la mascota: ")
    fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
    hora = input("Ingrese la hora: ")
    motivo = input("Ingrese el motivo de la consulta: ")

    archivo = open("turnos.txt", "a")

    archivo.write(id_mascota + ";" +
                  fecha + ";" +
                  hora + ";" +
                  motivo + "\n")

    archivo.close()

    print("\n¡Turno registrado correctamente!")

def mostrar_turnos():
    print("\n--- Lista de turnos ---")

    try:
        archivo = open("turnos.txt", "r")

        for linea in archivo:
            print(linea.strip())

        archivo.close()

    except FileNotFoundError:
        print("No hay turnos registrados.")


def registrar_atencion():
    print("\n--- Registrar atención médica ---")

    id_mascota = input("Ingrese el ID de la mascota: ")
    tipo_atencion = input("Ingrese el tipo de atención: ")
    observaciones = input("Ingrese las observaciones: ")

    archivo = open("atenciones.txt", "a")

    archivo.write(id_mascota + ";" +
                  tipo_atencion + ";" +
                  observaciones + "\n")

    archivo.close()

    print("\n¡Atención médica registrada correctamente!")


def estadisticas():
    print("\n========== ESTADÍSTICAS ==========\n")

    # CONTADOR DE MASCOTAS
    cantidad_mascotas = 0
    try:
        archivo = open("mascotas.txt", "r")

        for linea in archivo:
            cantidad_mascotas += 1

        archivo.close()

    except FileNotFoundError:
        cantidad_mascotas = 0

    # CONTADOR DE TURNOS
    cantidad_turnos = 0
    try:
        archivo = open("turnos.txt", "r")

        for linea in archivo:
            cantidad_turnos += 1

        archivo.close()

    except FileNotFoundError:
        cantidad_turnos = 0

    # CONTADOR DE ATENCIONES
    cantidad_atenciones = 0
    try:
        archivo = open("atenciones.txt", "r")

        for linea in archivo:
            cantidad_atenciones += 1

        archivo.close()

    except FileNotFoundError:
        cantidad_atenciones = 0

    print("Cantidad de mascotas registradas:", cantidad_mascotas)
    print("Cantidad de turnos registrados:", cantidad_turnos)
    print("Cantidad de atenciones realizadas:", cantidad_atenciones)


def main():
    opcion = -1

    while opcion != 0:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                registrar_mascota()
            
            elif opcion == 2:
                registrar_turno()
            
            elif opcion == 3:
                registrar_atencion()
            
            elif opcion == 4:
                mostrar_mascotas()
            
            elif opcion == 5:
                mostrar_turnos()

            elif opcion == 6:
                mostrar_atenciones()

            elif opcion == 7:
                estadisticas()

            elif opcion == 0:
                print("\nGracias por utilizar el sistema.")

            else:
                print("\nOpción invalida.")

        except ValueError:
            print("\nDebe ingresar un número.")

    input("\nPresiona Enter para cerrar la ventana...")


main()