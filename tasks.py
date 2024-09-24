"""
Gestión de tareas
"""


class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.is_completed = False


class TaskManager:
    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        pass

    def get_all_tasks(self):
        pass
