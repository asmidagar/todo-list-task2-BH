import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

TASKS_FILE = "tasks.txt"

# --------------------- SHARED LOGIC ----------------------

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 3:
                    task, due, priority = parts
                    tasks.append({"task": task[6:], "due": due[5:], "priority": priority[10:]})
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for t in tasks:
            file.write(f"Task: {t['task']} | Due: {t['due']} | Priority: {t['priority']}\n")

# --------------------- CONSOLE INTERFACE ----------------------

def add_task_cli(tasks):
    task = input("Enter task description: ").strip()
    due = input("Enter due date (YYYY-MM-DD): ").strip()
    priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()

    try:
        datetime.strptime(due, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return

    if priority not in ["High", "Medium", "Low"]:
        print("Priority must be High, Medium, or Low.")
        return

    tasks.append({"task": task, "due": due, "priority": priority})
    save_tasks(tasks)
    print("Task added successfully.")

def remove_task_cli(tasks):
    view_tasks_cli(tasks)
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Removed: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def view_tasks_cli(tasks):
    if not tasks:
        print("No tasks.")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t['task']} | Due: {t['due']} | Priority: {t['priority']}")
        print()

def run_console_mode():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            view_tasks_cli(tasks)
        elif choice == "2":
            add_task_cli(tasks)
        elif choice == "3":
            remove_task_cli(tasks)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

# --------------------- GUI INTERFACE ----------------------

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Manager")
        self.root.geometry("600x400")
        self.root.resizable(True, True)

        self.tasks = load_tasks()

        # Styling
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"))
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=28)
        style.map("Treeview", background=[("selected", "#ADD8E6")])

        # Main Frame
        self.frame = tk.Frame(root, bg="#f0f4f7")
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.tree = ttk.Treeview(self.frame, columns=("Task", "Due", "Priority"), show='headings', selectmode="browse")
        self.tree.heading("Task", text="Task")
        self.tree.heading("Due", text="Due Date")
        self.tree.heading("Priority", text="Priority")
        self.tree.column("Task", width=240)
        self.tree.column("Due", width=100, anchor="center")
        self.tree.column("Priority", width=100, anchor="center")
        self.tree.pack(fill="both", expand=True, pady=10)

        self.load_tree()

        # Buttons
        button_frame = tk.Frame(self.frame, bg="#f0f4f7")
        button_frame.pack(pady=10)

        self.make_button(button_frame, "Add Task", self.add_task, "#4CAF50").pack(side=tk.LEFT, padx=10)
        self.make_button(button_frame, "Remove Task", self.remove_task, "#F44336").pack(side=tk.LEFT, padx=10)
        self.make_button(button_frame, "Exit", root.quit, "#607D8B").pack(side=tk.LEFT, padx=10)

    def make_button(self, parent, text, command, bg_color):
        return tk.Button(
            parent, text=text, command=command,
            font=("Segoe UI", 10, "bold"), bg=bg_color, fg="white",
            activebackground="#333", padx=12, pady=6, borderwidth=0
        )

    def load_tree(self):
        self.tree.delete(*self.tree.get_children())
        for task in self.tasks:
            tag = task["priority"].lower()
            self.tree.insert('', tk.END, values=(task["task"], task["due"], task["priority"]), tags=(tag,))

        self.tree.tag_configure("high", background="#FFCDD2")
        self.tree.tag_configure("medium", background="#FFF9C4")
        self.tree.tag_configure("low", background="#C8E6C9")

    def add_task(self):
        task = simpledialog.askstring("Task", "Enter task description:")
        due = simpledialog.askstring("Due Date", "Enter due date (YYYY-MM-DD):")
        priority = simpledialog.askstring("Priority", "Enter priority (High/Medium/Low):")

        if not task or not due or not priority:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            datetime.strptime(due, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format.")
            return

        if priority.capitalize() not in ["High", "Medium", "Low"]:
            messagebox.showerror("Error", "Priority must be High, Medium, or Low.")
            return

        self.tasks.append({"task": task, "due": due, "priority": priority.capitalize()})
        save_tasks(self.tasks)
        self.load_tree()

    def remove_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a task to remove.")
            return
        index = self.tree.index(selected[0])
        self.tasks.pop(index)
        save_tasks(self.tasks)
        self.load_tree()

def run_gui_mode():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

# --------------------- MODE SELECTION ----------------------

if __name__ == "__main__":
    print("Choose mode:")
    print("1. Console")
    print("2. GUI")
    mode = input("Enter 1 or 2: ").strip()

    if mode == "1":
        run_console_mode()
    elif mode == "2":
        run_gui_mode()
    else:
        print("Invalid choice.")
