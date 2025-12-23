"""
Gestión de tareas
"""
from itertools import count


class Task:
    def __init__(self, id, description):
        self.id = id
        self.is_completed = False
        if description is None or description.strip() == "":
            raise ValueError("Description cannot be empty")
        self.description = description


class TaskManager:
    def __init__(self):
        self._tasks = []
        self._id_counter = count(1)

    def generate_id(self):
        return str(next(self._id_counter))

    def add_task(self, task):
        self._tasks.append(Task(self.generate_id(), task))

    def get_all_tasks(self):
        return self._tasks

    def get_task_by_id(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id, new_description):
        for task in self._tasks:
            if task.id == task_id:
                task.description = new_description
                return

    def remove_task(self, task_id):
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                self._tasks.pop(i)
                self.send_removed_notification(task_id)
                return

    def mark_task_as_completed(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                task.is_completed = True
                return

    def send_removed_notification(self, task_id):
        pass
