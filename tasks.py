"""
Gestión de tareas
"""
import random
import logging


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
            logging.error("La descripción no puede estar vacía")
            raise ValueError("La descripción no puede estar vacía")
        task = Task("".join(random.sample("1234567890", 4)),  description)
        self._tasks.append(task)

    def get_all_tasks(self):
        return self._tasks

    def remove_task(self, task_id):
        initial_count = len(self._tasks)
        self._tasks = [task for task in self._tasks if task.id != task_id]

        if len(self._tasks) == initial_count:
            logging.error(f"Tarea con ID {task_id} no encontrada")
            raise ValueError(f"Tarea con ID {task_id} no encontrada")
        self.send_notification(task_id)

    def mark_task_completed(self, task_id):
        task = self.get_task(task_id)
        task.is_completed = True
        self.send_notification(task_id)

    def get_completed_tasks(self):
        completed_tasks = []
        for task in self._tasks:
            if task.is_completed:
                completed_tasks.append(task)
        return completed_tasks

    def send_notification(self, task_id):
        logging.info(f"Notificación enviada sobre {task_id}")
        return "Notification sent"

    def get_task(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"Tarea con ID {task_id} no encontrada")
