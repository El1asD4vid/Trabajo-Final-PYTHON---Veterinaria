def mostrar_menu():
    print("\n====================================")
    print("   VETERINARIA 'PATAS Y BIGOTES'")
    print("====================================")
    print("1. Registrar mascota")
    print("2. Registrar turno")
    print("3. Registrar atención médica")
    print("4. Mostrar mascotas")
    print("5. Mostrar turnos")
    print("6. Estadísticas")
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


def main():
    opcion = -1

    while opcion != 0:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                registrar_mascota()
            
            elif opcion == 4:
                mostrar_mascotas()

            elif opcion == 0:
                print("\nGracias por utilizar el sistema.")

            else:
                print("\nFuncionalidad en desarrollo...")

        except ValueError:
            print("\nDebe ingresar un número.")

    input("\nPresiona Enter para cerrar la ventana...")


main()