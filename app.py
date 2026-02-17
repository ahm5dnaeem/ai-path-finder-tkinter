import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Search Visualizer")

# ---------- USER INPUT ----------
# rows = int(input("Enter rows: "))
# cols = int(input("Enter cols: "))
rows = 5
cols = 5

# ---------- TOP CONTROL FRAME ----------
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

# Dropdown variable
algorithm_var = tk.StringVar()
algorithm_var.set("BFS")   # default

dropdown = ttk.Combobox(control_frame,
                        textvariable=algorithm_var,
                        values=["BFS", "DFS","UCS","DLS","IDDFS","Bidirectional"],
                        state="readonly")
dropdown.pack(side=tk.LEFT, padx=10)

# Select Button
def select_algorithm():
    selected = algorithm_var.get()
    print("Selected Algorithm:", selected)
    # Later you will call BFS or DFS here

select_btn = tk.Button(control_frame,
                       text="Select",
                       command=select_algorithm)
select_btn.pack(side=tk.LEFT)

# ---------- GRID FRAME ----------
grid_frame = tk.Frame(root)
grid_frame.pack()

grid_cells = []

for i in range(rows):
    row_list = []
    for j in range(cols):
        cell = tk.Label(grid_frame,
                        width=6,
                        height=3,
                        bg="white",
                        borderwidth=1,
                        relief="solid")
        cell.grid(row=i, column=j)

        row_list.append(cell)
    grid_cells.append(row_list)

# Example: manually change a cell
grid_cells[0][0].config(bg="green")

root.mainloop()
