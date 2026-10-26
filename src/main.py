from parser import parse_command
import tkinter as tk

root = tk.Tk()
root.title("Эмулятор VFS: default")
root.geometry("800x500")

output = tk.Text(root, state="disabled")
output.pack(fill="both", expand=True, padx=10, pady=10)

command_entry = tk.Entry(root)
command_entry.pack(fill="x", padx=10, pady=10)


def handle_command(event):
    command_line = command_entry.get()
    command_entry.delete(0, tk.END)

    output.config(state="normal")
    output.insert(tk.END, f"VFS> {command_line}\n")

    try:
        parts = parse_command(command_line)

        if parts:
            command = parts[0]
            args = parts[1:]

            if command in ("ls", "cd"):
                if len(args) > 1:
                    output.insert(tk.END, "Ошибка: слишком много аргументов\n")
                else:
                    output.insert(tk.END, f"Команда: {command}\n")
                    output.insert(tk.END, f"Аргументы: {args}\n")

            elif command == "exit":
                if args:
                    output.insert(tk.END, "Ошибка: exit не принимает аргументы\n")
                else:
                    root.destroy()
                    return

            else:
                output.insert(tk.END, f"Ошибка: неизвестная команда {command}\n")

    except ValueError as error:
        output.insert(tk.END, f"Ошибка: {error}\n")

    output.config(state="disabled")
    output.see(tk.END)


command_entry.bind("<Return>", handle_command)

root.mainloop()
