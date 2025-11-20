import tempfile
from pathlib import Path
from todo_cli import store

def test_add_and_list(tmp_path: Path):
    p = tmp_path / "todos.json"
    assert store.list_todos(p) == []
    store.add_todo("task1", p)
    store.add_todo("task2", p)
    todos = store.list_todos(p)
    assert len(todos) == 2
    assert todos[0]["text"] == "task1"
    assert todos[1]["text"] == "task2"

def test_remove(tmp_path: Path):
    p = tmp_path / "todos.json"
    store.add_todo("a", p)
    store.add_todo("b", p)
    assert store.remove_todo(0, p) is True
    todos = store.list_todos(p)
    assert len(todos) == 1
    assert todos[0]["text"] == "b"
    # invalid index
    assert store.remove_todo(10, p) is False
