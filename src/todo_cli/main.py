"""
CLI entrypoint for the todo app.
Usage examples:
  python -m todo_cli.main add "Buy milk"
  python -m todo_cli.main list
"""
from __future__ import annotations
import argparse
from pathlib import Path
from todo_cli import store

def main(argv=None):
    parser = argparse.ArgumentParser(prog="todo")
    sub = parser.add_subparsers(dest="cmd")
    a_add = sub.add_parser("add")
    a_add.add_argument("text", nargs="+")
    sub.add_parser("list")
    a_remove = sub.add_parser("remove")
    a_remove.add_argument("index", type=int)

    args = parser.parse_args(argv)
    if args.cmd == "add":
        text = " ".join(args.text)
        item = store.add_todo(text)
        print(f'Added: "{item["text"]}"')
    elif args.cmd == "list":
        todos = store.list_todos()
        if not todos:
            print("No todos.")
            return
        for i, t in enumerate(todos):
            mark = "x" if t.get("done") else " "
            print(f"{i}. [{mark}] {t.get('text')}")
    elif args.cmd == "remove":
        ok = store.remove_todo(args.index)
        print("Removed." if ok else "Index out of range.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
