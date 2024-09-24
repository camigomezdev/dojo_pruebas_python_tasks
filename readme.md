# Gestión de Tareas

## Descripción del Proyecto
Este proyecto consiste en construir una **API de gestión de tareas (To-Do List)**, siguiendo las prácticas de desarrollo dirigido por pruebas (TDD) y el uso de mocks para simular dependencias externas.

### Funcionalidades principales:
1. **Crear tareas.**
2. **Actualizar el estado de una tarea (completa/incompleta).**
3. **Borrar tareas.**
4. **Obtener la lista de tareas.**

## Estructura del Proyecto

### 1. Modelo `Task`

- **Clase `Task`:** Representa una tarea con atributos básicos.
  - Atributos:
    - `id`: Identificador único de la tarea.
    - `description`: Descripción de la tarea.
    - `is_completed`: Estado de la tarea (completada o no).

### 2. Clase `TaskManager`

- **Clase `TaskManager`:** Se encargará de gestionar las tareas (añadir, eliminar, completar).
  - Métodos:
    - `add_task(description)`: Agrega una nueva tarea a la lista.
    - `remove_task(id)`: Elimina una tarea existente.
    - `get_all_tasks()`: Devuelve la lista de tareas.
    - `mark_task_completed(id)`: Marca una tarea como completada.


## Lista de Pruebas para el Proyecto de Gestión de Tareas

### Pruebas de la funcionalidad básica

- `test_add_task`: Verifica que se puede añadir una tarea a la lista.
- `test_get_all_tasks`: Verifica que se puede obtener la lista completa de tareas.
- `test_mark_task_completed`: Verifica que se puede marcar una tarea como completada.
- `test_remove_task`: Verifica que se puede eliminar una tarea de la lista.

### Pruebas con `pytest.parametrize`

- `test_add_task_parametrized`: Verifica que se pueden añadir varias tareas con diferentes descripciones.
- `test_mark_task_completed_parametrized`: Verifica que se pueden marcar como completadas varias tareas con diferentes IDs.
- `test_remove_task_parametrized`: Verifica que se pueden eliminar varias tareas con diferentes IDs.

### Pruebas de comportamiento de borde

- `test_add_task_empty_description`: Verifica el comportamiento cuando se intenta añadir una tarea sin descripción.
- `test_mark_task_completed_invalid_id`: Verifica el comportamiento al intentar marcar como completada una tarea con un ID inexistente.
- `test_remove_task_invalid_id`: Verifica el comportamiento al intentar eliminar una tarea con un ID inexistente.

### Pruebas con Mocks

- `test_add_task_with_mock`: Verifica que se llama correctamente a la función de guardar en la base de datos al añadir una tarea.
- `test_remove_task_with_mock`: Verifica que se llama correctamente a la función de eliminar de la base de datos al eliminar una tarea.
- `test_send_notification_mock`: Verifica si se enevió una notificación
