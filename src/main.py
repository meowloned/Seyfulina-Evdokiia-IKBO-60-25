from parser import parse_command
import tkinter as tk
import argparse
from pathlib import Path
from logger import log_command


arg_parser = argparse.ArgumentParser(
    description="Эмулятор UNIX Shell"
)

arg_parser.add_argument("--vfs", help="Путь к VFS")
arg_parser.add_argument("--log", help="Путь к CSV-логу")
arg_parser.add_argument("--script", help="Путь к стартовому скрипту")

config = arg_parser.parse_args()

print(f"vfs: {config.vfs}")
print(f"log: {config.log}")
print(f"script: {config.script}")

root = tk.Tk()
vfs_name = Path(config.vfs).name if config.vfs else "default"
root.title(f"Эмулятор VFS: {vfs_name}")
root.geometry("800x500")

output = tk.Text(root, state="disabled")
output.pack(fill="both", expand=True, padx=10, pady=10)

command_entry = tk.Entry(root)
command_entry.pack(fill="x", padx=10, pady=10)


def execute_command(command_line):
    parts = parse_command(command_line)
    command = parts[0]
    args = parts[1:]

    if command in ("ls", "cd"):
        if len(args) > 1:
            return "слишком много аргументов", False

        output.insert(tk.END, f"Команда: {command}\n")
        output.insert(tk.END, f"Аргументы: {args}\n")
        return "", False

    if command == "exit":
        if args:
            return "exit не принимает аргументы", False
        return "", True

    return f"неизвестная команда {command}", False


def handle_command(event=None, command_line=None):
    if command_line is None:
        command_line = command_entry.get()
        command_entry.delete(0, tk.END)

    if not command_line.strip():
        return

    output.config(state="normal")
    output.insert(tk.END, f"VFS> {command_line}\n")
    error_message = ""
    should_exit = False

    try:
        error_message, should_exit = execute_command(command_line)

    except ValueError as error:
        error_message = str(error)
        should_exit = False

    if error_message:
        output.insert(tk.END, f"Ошибка: {error_message}\n")

    log_command(config.log, command_line, error_message)

    if should_exit:
        root.destroy()
        return

    output.config(state="disabled")
    output.see(tk.END)


def run_startup_script():
    if not config.script:
        return

    try:
        commands = Path(config.script).read_text(
            encoding="utf-8"
        ).splitlines()
    except (OSError, UnicodeError) as error:
        output.config(state="normal")
        output.insert(tk.END, f"Ошибка скрипта: {error}\n")
        output.config(state="disabled")
        return

    for command_line in commands:
        command_line = command_line.strip()

        if not command_line or command_line.startswith("#"):
            continue

        handle_command(command_line=command_line)

        if command_line == "exit":
            return


command_entry.bind("<Return>", handle_command)

root.after(0, run_startup_script)

root.mainloop()
