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

    def generate_id(self):
        raise NotImplementedError("Subclasses must implement this method")

    def add_task(self, task):
        raise NotImplementedError("Subclasses must implement this method")

    def get_all_tasks(self):
        raise NotImplementedError("Subclasses must implement this method")

    def get_task_by_id(self, task_id):
        raise NotImplementedError("Subclasses must implement this method")

    def update_task(self, task_id, new_description):
        raise NotImplementedError("Subclasses must implement this method")

    def remove_task(self, task_id):
        raise NotImplementedError("Subclasses must implement this method")

    def mark_task_as_completed(self, task_id):
        raise NotImplementedError("Subclasses must implement this method")

    def send_removed_notification(self, task_id):
        raise NotImplementedError("Subclasses must implement this method")
