import pytest
from tasks import TaskManager


@pytest.fixture
def empty_task_manager():
    """Crea y retorna una instancia de TaskManager vacía."""
    return TaskManager()


@pytest.fixture
def manager_with_tasks(mocker):
    """Crea una instancia de TaskManager con algunas tareas predefinidas."""
    mock_random = mocker.patch("tasks.random.sample")
    mock_random.side_effect = ["1", "2", "3"]

    manager_with_tasks = TaskManager()
    for i in range(1, 4):
        manager_with_tasks.add_task(f"Task {i}")
    return manager_with_tasks


def test_add_task(empty_task_manager):
    empty_task_manager.add_task("Task 1")
    tasks_list = empty_task_manager._tasks
    assert len(tasks_list) == 1
    assert tasks_list[0].description == "Task 1"


@pytest.mark.parametrize(
    "tasks",
    [
        ([]),
        (["task 1",]),
        (["task 1", "task 2", "task 3", "task 4",]),
    ]
)
def test_get_all_tasks(empty_task_manager, tasks):
    for task in tasks:
        empty_task_manager.add_task(task)

    list_tasks = empty_task_manager.get_all_tasks()

    assert len(list_tasks) == len(tasks)

    for index, task in enumerate(list_tasks):
        assert task.description == tasks[index]
        assert not task.is_completed


@pytest.mark.parametrize(
    "id_to_remove",
    [
        ("1"),
        ("2"),
        ("3"),
    ]
)
def test_remove_task_by_id(manager_with_tasks, id_to_remove):
    manager_with_tasks.remove_task(id_to_remove)

    list_tasks = manager_with_tasks.get_all_tasks()
    list_ids = [task.id for task in list_tasks]

    assert id_to_remove not in list_ids
    assert len(list_tasks) == 2


@pytest.mark.parametrize("task_id_to_complete", [
    ("1"),
    ("2"),
    ("3"),
])
def test_mark_task_completed(
        manager_with_tasks, task_id_to_complete, mocker):

    mock_send_notification = mocker.patch(
        'tasks.TaskManager.send_notification', return_value="Mock Notification")

    response = manager_with_tasks.mark_task_completed(task_id_to_complete)

    tasks = manager_with_tasks.get_all_tasks()
    task = next(task for task in tasks
                if task.id == task_id_to_complete)

    assert task.is_completed
    assert response == "Mock Notification"
    mock_send_notification.assert_called_once_with(task_id_to_complete)


def test_add_task_empty_description(manager_with_tasks):
    with pytest.raises(
            ValueError, match="La descripción no puede estar vacía"):
        manager_with_tasks.add_task("")


def test_mark_task_completed_invalid_id(manager_with_tasks):
    with pytest.raises(ValueError, match="Tarea con ID 999 no encontrada"):
        manager_with_tasks.mark_task_completed("999")


def test_remove_task_invalid_id(manager_with_tasks):
    with pytest.raises(ValueError, match="Tarea con ID 999 no encontrada"):
        manager_with_tasks.remove_task("999")
