# 📝 To-Do List Application (Console + GUI)

This project is a simple and persistent **To-Do List Manager** implemented in Python with both **Console** and **GUI** interfaces. It allows users to **add, remove, view, and prioritize tasks with due dates**, while storing all data persistently in a text file (`tasks.txt`).

---

## 🚀 Features

### ✅ Console Version
- Add new tasks with priority and due date
- Remove tasks by number
- View all tasks in a list
- Persistent storage using `tasks.txt`

### 🎨 GUI Version (Tkinter-based)
- Visually appealing, user-friendly interface
- Add/remove/view tasks with priority and due date
- Scrollable task list
- Responsive and colorful UI design
- Uses the same backend as the console version (shared data)

---

## 📁 File Structure

.
├── todo.py # Main script for GUI and console logic
├── tasks.txt # Stores tasks persistently
├── .gitignore # Ignores all files except todo.py and tasks.txt
└── README.md # Project documentation

---

## 💻 How to Run

### ▶️ Console Version
python todo.py console
### 🖥️ GUI Version
python todo.py gui

## 📦 Requirements
 Python 3.x
 No external libraries needed (only tkinter which comes with Python)

---

## ✨ Sample Task Format
 Each task includes:
   Title
   Due Date (optional)
   Priority (Low / Medium / High)

 Example (in GUI or console):
    Buy groceries | Due: 2025-07-20 | Priority: High
    
## 🧠 Learning Goals
  File handling with Python (open, read, write)
  List and string operations
  Tkinter GUI basics
  Modular and reusable code structure
  
---

## 🤝 Contributions
  This project was developed as part of an internship task by Asmi Dagar.
  Feel free to fork and enhance it with features like:
    Task editing
    Date validation
    Sorting by due date or priority
    Notifications

## 📸 Screenshot
  <img width="1920" height="1020" alt="Screenshot 2025-07-18 113507" src="https://github.com/user-attachments/assets/0445d157-1898-4aae-90eb-0a63048fd64d" />


📃 License
This project is open-source and free to use under the MIT License.

