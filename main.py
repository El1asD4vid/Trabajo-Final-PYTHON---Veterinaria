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


def main():
    opcion = -1

    while opcion != 0:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 0:
                print("\nGracias por utilizar el sistema.")
            else:
                print("\nFuncionalidad en desarrollo...")

        except ValueError:
            print("\nDebe ingresar un número.")

    input("\nPresiona Enter para cerrar la ventana...")


main()