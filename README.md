# Todo CLI (tiny)

A small Python CLI todo app to practice GitHub + Copilot workflows.

How to run locally:
1. git clone https://github.com/rajraomv/todo-cli.git
2. cd todo-cli
3. python -m venv .venv
4. source .venv/bin/activate   # Windows: .venv\Scripts\activate
5. pip install -U pytest
6. python -m todo_cli.main add "Buy milk"
7. python -m todo_cli.main list
8. pytest -q

Files:
- src/todo_cli/main.py — CLI entry
- src/todo_cli/store.py — simple JSON-backed storage and helper functions
- tests/test_store.py — pytest tests for store functions

Notes:
- Do not commit secrets here.
- Review Copilot suggestions before accepting them.
