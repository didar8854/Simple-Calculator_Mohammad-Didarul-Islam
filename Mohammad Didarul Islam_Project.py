import tkinter as tk


# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        result = str(eval(expression))
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")


# Function to update the expression in the entry box
def update_expression(value):
    current = entry_var.get()
    entry_var.set(current + str(value))


# Function to clear the entry box
def clear_expression():
    entry_var.set("")


# Function to handle backspace
def backspace():
    current = entry_var.get()
    entry_var.set(current[:-1])


# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a variable to hold the entry value
entry_var = tk.StringVar()

# Create the entry box
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 24), bd=10, relief="sunken", width=15, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('<', 5, 1)
]

# Create buttons and place them on the grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=('Arial', 18), command=lambda: evaluate_expression(entry_var.get()))
    elif text == "C":
        button = tk.Button(root, text=text, font=('Arial', 18), command=clear_expression)
    elif text == "<":
        button = tk.Button(root, text=text, font=('Arial', 18), command=backspace)
    else:
        button = tk.Button(root, text=text, font=('Arial', 18), command=lambda value=text: update_expression(value))

    button.grid(row=row, column=col, sticky="nsew", ipadx=20, ipady=20)

# Make the grid expandable
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Run the main loop
root.mainloop()
