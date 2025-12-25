import pytest

from itertools import count
from tasks import TaskManager


def test_example():
    assert 1 == 1


@pytest.fixture
def task_manager():
    task_manager = TaskManager()
    yield task_manager


def test_add_task(task_manager):
    task_manager.add_task("Tarea 1")
    
    assert len(task_manager.get_all_tasks()) == 1, "TEST FAILED: Task was not added"
    
    assert task_manager.get_all_tasks()[0].description == "Tarea 1", "TEST FAILED: Task description does not match"
    
    assert not task_manager.get_all_tasks()[0].is_completed, "TEST FAILED: Task is completed"


def test_get_all_task(task_manager):
    list_tasks = task_manager.get_all_tasks()
    assert isinstance(list_tasks, list), "TEST FAILED: Tasks list is not a list"


def test_get_all_tasks_empty(task_manager):
    assert len(task_manager.get_all_tasks()) == 0, "TEST FAILED: Task was not added"


def test_get_all_tasks_one_task(task_manager):
    task_manager.add_task("Tarea 1")
    
    assert len(task_manager.get_all_tasks()) == 1, "TEST FAILED: Task was not added"


def test_get_all_tasks_many_tasks(task_manager):
    task_manager.add_task("Tarea 1")
    task_manager.add_task("Tarea 2")
    task_manager.add_task("Tarea 3")
    list_tasks = task_manager.get_all_tasks()

    assert len(list_tasks) == 3, "TEST FAILED: Task was not added"
    
    assert list_tasks[0].description == "Tarea 1", "TEST FAILED: Task description does not match"
    assert not list_tasks[0].is_completed, "TEST FAILED: Task is completed"
    
    assert list_tasks[1].description == "Tarea 2", "TEST FAILED: Task description does not match"
    assert not list_tasks[1].is_completed, "TEST FAILED: Task is completed"
    
    assert list_tasks[2].description == "Tarea 3", "TEST FAILED: Task description does not match"
    assert not list_tasks[2].is_completed, "TEST FAILED: Task is completed"


@pytest.mark.parametrize(
    "tasks",
    [
        ([]),
        (["Tarea 1"]),
        (["Tarea 1", "Tarea 2"]),
        (["Tarea 1", "Tarea 2", "Tarea 3"]),
    ]
)
def test_add_task_parametrized(task_manager, tasks):
    for task in tasks:
        task_manager.add_task(task)
    
    list_task = task_manager.get_all_tasks()

    assert len(list_task) == len(tasks), "TEST FAILED: Task was not added"
    
    for i, task in enumerate(list_task):
        assert task.description == tasks[i], "TEST FAILED: Task description does not match"
        assert not task.is_completed, "TEST FAILED: Task is completed"


def test_add_task_empty_description(task_manager):
    with pytest.raises(
            ValueError, match="Description cannot be empty"):
        task_manager.add_task("")
    
    assert len(task_manager.get_all_tasks()) == 0, "TEST FAILED: Task was added"


@pytest.mark.parametrize(
    "id_task",
    [ (1), (2), (3) ]
)
def test_get_task_by_id(task_manager, id_task, mocker):

    mock_generate_id = mocker.patch("tasks.TaskManager.generate_id")
    mock_generate_id.side_effect = count(1) # Genera un contador infinito

    task_manager.add_task("Tarea 1")
    task_manager.add_task("Tarea 2")
    task_manager.add_task("Tarea 3")
    
    task_selected = task_manager.get_task_by_id(id_task)
    assert task_selected is not None, "TEST FAILED: Task was not found"
    assert task_selected.id == id_task, "TEST FAILED: Task ID does not match"


@pytest.mark.parametrize(
    "id_to_remove",
    [ (1), (2), (3) ]
)
def test_remove_task_parametrized(task_manager, id_to_remove, mocker):

    mock_generate_id = mocker.patch("tasks.TaskManager.generate_id")
    mock_generate_id.side_effect = count(1) # Genera un contador infinito

    task_manager.add_task("Tarea 1")
    task_manager.add_task("Tarea 2")
    task_manager.add_task("Tarea 3")
    
    task_manager.remove_task(id_to_remove)
    
    list_task = task_manager.get_all_tasks()
    list_ids = [task.id for task in list_task]
    
    assert len(list_task) == 2, "TEST FAILED: Task was not removed"
    assert id_to_remove not in list_ids, "TEST FAILED: Task was not removed"


def test_send_notification(task_manager, mocker):
    mock_send_notification = mocker.patch("tasks.TaskManager.send_removed_notification")

    mock_generate_id = mocker.patch("tasks.TaskManager.generate_id")
    mock_generate_id.side_effect = count(1) # Genera un contador infinito

    task_manager.add_task("Tarea 1")
    task_manager.remove_task(1)
    
    mock_generate_id.assert_called_once()
    mock_send_notification.assert_called_once_with(1)


def test_mark_task_completed(task_manager):
    task_manager.add_task("Tarea 1")

    unique_task = task_manager.get_all_tasks()[0]
    task_manager.mark_task_as_completed(unique_task.id)
    
    list_task = task_manager.get_all_tasks()
    
    assert list_task[0].is_completed, "TEST FAILED: Task was not completed"


@pytest.mark.parametrize(
    "id_to_complete",
    [ (1), (2), (3) ]
)
def test_mark_task_completed_parametrized(task_manager, id_to_complete, mocker):

    mock_generate_id = mocker.patch("tasks.TaskManager.generate_id")
    mock_generate_id.side_effect = count(1) # Genera un contador infinito

    task_manager.add_task("Tarea 1")
    task_manager.add_task("Tarea 2")
    task_manager.add_task("Tarea 3")
    
    task_manager.mark_task_as_completed(id_to_complete)
    
    list_task = task_manager.get_all_tasks()
    
    assert task_manager.get_task_by_id(id_to_complete).is_completed, "TEST FAILED: Task was not completed"
    
    assert not any(t.is_completed for t in list_task if t.id != id_to_complete), "TEST FAILED: An invalid task was marked as completed"
