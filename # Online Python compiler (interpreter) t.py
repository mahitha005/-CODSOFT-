# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this on
import tkinter as tk

# Function to update the input field
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to handle special operations
def special_operation(operation):
    try:
        value = float(entry.get())
        if operation == 'sqrt':
            result = (value)**(0.5)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Initialize the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display input and output
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('%', 4, 3)
]

# Add buttons to the window
for (text, row, col) in buttons:
    tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: button_click(t)).grid(row=row, column=col)

# Add special buttons
tk.Button(root, text='C', padx=20, pady=20, command=clear).grid(row=5, column=0)
tk.Button(root, text='sqrt', padx=20, pady=20, command=lambda: special_operation('sqrt')).grid(row=5, column=1)
tk.Button(root, text='^', padx=20, pady=20, command=lambda: button_click('**')).grid(row=5, column=2)

# '=' button will calculate the result
tk.Button(root, text='=', padx=20, pady=20, command=calculate).grid(row=5, column=3)

# Run the main loop
root.mainloop()
