
def mostrar_menu():
    print("\n--- Lista de Tareas ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Salir")


def ver_tareas():
    try:
        with open("tareas.txt", "r") as archivo:
            tareas = archivo.readlines()
            if not tareas:
                print("No hay tareas pendientes.")
            else:
                print("\nTareas:")
                for i, tarea in enumerate(tareas):
                    print(f"{i + 1}. {tarea.strip()}")
    except FileNotFoundError:
        print("No hay tareas pendientes.")


def agregar_tarea():
    tarea = input("Escribe la nueva tarea: ")
    with open("tareas.txt", "a") as archivo:
        archivo.write(tarea + "\n")
    print(f"Tarea '{tarea}' agregada.")


def marcar_completada():
    ver_tareas()
    try:
        numero = int(input("Ingresa el número de la tarea completada: ")) - 1
        with open("tareas.txt", "r") as archivo:
            tareas = archivo.readlines()
        if 0 <= numero < len(tareas):
            tarea_eliminada = tareas.pop(numero)
            with open("tareas.txt", "w") as archivo:
                archivo.writelines(tareas)
            print(f"Tarea '{tarea_eliminada.strip()}' marcada como completada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            ver_tareas()
        elif opcion == "2":
            agregar_tarea()
        elif opcion == "3":
            marcar_completada()
        elif opcion == "4":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
