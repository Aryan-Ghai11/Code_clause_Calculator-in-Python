from tkinter import *

# Function to perform calculations
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_list.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Invalid input")

# Creating a window
window = Tk()
window.title("Calculator")

# Creating labels and entries for input
label1 = Label(window, text="Enter first number:")
label1.grid(row=0, column=0)

entry1 = Entry(window)
entry1.grid(row=0, column=1)

label2 = Label(window, text="Enter second number:")
label2.grid(row=1, column=0)

entry2 = Entry(window)
entry2.grid(row=1, column=1)

# Creating a dropdown list for selecting operator
operator_list = StringVar(window)
operator_list.set("+") # Default value

operator_label = Label(window, text="Select an operator:")
operator_label.grid(row=2, column=0)

operator_dropdown = OptionMenu(window, operator_list, "+", "-", "*", "/")
operator_dropdown.grid(row=2, column=1)

# Creating a button to calculate the result
calculate_button = Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0)

# Creating a label to display the result
result_label = Label(window, text="Result:")
result_label.grid(row=3, column=1)

# Run the window
window.mainloop()
