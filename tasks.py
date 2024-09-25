"""
Gestión de tareas
"""
import random


class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.is_completed = False


class TaskManager:
    def __init__(self):
        self._tasks = []

    def add_task(self, description):
        if not description:
            raise ValueError("La descripción no puede estar vacía")
        task = Task(random.sample("1234567890", 4),  description)
        self._tasks.append(task)

    def get_all_tasks(self):
        return self._tasks

    def remove_task(self, task_id):
        initial_count = len(self._tasks)
        self._tasks = [task for task in self._tasks if task.id != task_id]
        
        if len(self._tasks) == initial_count:
            raise ValueError(f"Tarea con ID {task_id} no encontrada")

    def mark_task_completed(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                task.is_completed = True
                response = self.send_notification(task_id)
                return response
        raise ValueError(f"Tarea con ID {task_id} no encontrada")

    def send_notification(self, task_id):
        return "Notificación enviada"
