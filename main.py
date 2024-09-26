from tasks import TaskManager


def print_menu():
    print("\n--- Menú TaskManager ---")
    print("1. Añadir tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Ver tareas completadas")
    print("5. Eliminar tarea")
    print("6. Salir")


def main():
    manager = TaskManager()

    while True:
        print_menu()
        choice = input("Seleccione una opción: ")

        match choice:
            case "1":
                description = input("Ingrese la descripción de la tarea: ")
                try:
                    manager.add_task(description)
                    print("Tarea añadida correctamente.")
                except ValueError as e:
                    print(f"Error: {e}")

            case "2":
                tasks = manager.get_all_tasks()
                if not tasks:
                    print("No hay tareas.")
                else:
                    print("\n--- Lista de Tareas ---")
                    for task in tasks:
                        status = "Completada" if task.is_completed else "Pendiente"
                        print(
                            f"ID: {task.id}, Descripción: {task.description}, Estado: {status}")

            case "3":
                task_id = input("Ingrese el ID de la tarea a completar: ")
                try:
                    manager.mark_task_completed(task_id)
                    print(f"Tarea con ID {task_id} marcada como completada.")
                except ValueError as e:
                    print(f"Error: {e}")

            case "4":
                completed_tasks = manager.get_completed_tasks()
                if not completed_tasks:
                    print("No hay tareas completadas.")
                else:
                    print("\n--- Tareas Completadas ---")
                    for task in completed_tasks:
                        print(
                            f"ID: {task.id}, Descripción: {task.description}")

            case "5":
                task_id = input("Ingrese el ID de la tarea a eliminar: ")
                try:
                    manager.remove_task(task_id)
                    print(f"Tarea con ID {task_id} eliminada.")
                except ValueError as e:
                    print(f"Error: {e}")

            case "6":
                print("Saliendo del programa...")
                break

            case _:
                print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()
