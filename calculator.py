import tkinter as tk

current_expression = ""

def clear_button_clicked():
    global current_expression
    current_expression = ""
    expression_label.config(text=current_expression)

def button_clicked(button_text):
    global current_expression
    if button_text == "=":
        try:
            
            result = eval(current_expression)
            current_expression = str(result)
            expression_label.config(text=current_expression)
        except Exception:
            
            current_expression = "Error"
            expression_label.config(text=current_expression)
    else:
       
        current_expression += button_text
        expression_label.config(text=current_expression)


window = tk.Tk()
window.title("Simple Calculator")

expression_label = tk.Label(window, text="", font=("Arial", 24))
expression_label.pack(pady=20)


for digit in range(10):
    button = tk.Button(window, text=str(digit), command=lambda digit=digit: button_clicked(str(digit)))
    button.grid(row=int(digit / 3), column=digit % 3, padx=5, pady=5)


operator_buttons = ["+", "-", "*", "/", "="]
for i, operator in enumerate(operator_buttons):
    button = tk.Button(window, text=operator, command=lambda operator=operator: button_clicked(operator))
    button.grid(row=int(i / 3 + 1), column=i % 3, padx=5, pady=5)

clear_button = tk.Button(window, text="C", command=clear_button_clicked)
clear_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
window.mainloop()
