"""
Simple JSON-backed todo store.
Functions are written to be testable (accept a path).
"""
from __future__ import annotations
import json
from pathlib import Path
from typing import List, Dict, Any

def _default_path(path: Path | str | None) -> Path:
    if path is None:
        return Path("data/todos.json")
    return Path(path)

def load_todos(path: Path | str | None = None) -> List[Dict[str, Any]]:
    p = _default_path(path)
    if not p.exists():
        return []
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return []

def save_todos(todos: List[Dict[str, Any]], path: Path | str | None = None) -> None:
    p = _default_path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(todos, indent=2), encoding="utf-8")

def add_todo(text: str, path: Path | str | None = None) -> Dict[str, Any]:
    todos = load_todos(path)
    item = {"text": text, "done": False}
    todos.append(item)
    save_todos(todos, path)
    return item

def list_todos(path: Path | str | None = None) -> List[Dict[str, Any]]:
    return load_todos(path)

def remove_todo(index: int, path: Path | str | None = None) -> bool:
    todos = load_todos(path)
    if index < 0 or index >= len(todos):
        return False
    todos.pop(index)
    save_todos(todos, path)
    return True
