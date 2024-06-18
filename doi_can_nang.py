import tkinter as tk

def convert_weight():
    try:

        weight_kg = float(weight_entry.get())

 
        weight_grams = weight_kg * 1000
        grams_label.config(text=f"Grams: {weight_grams:.2f}")

        weight_pounds = weight_kg * 2.20462
        pounds_label.config(text=f"Pounds: {weight_pounds:.2f}")

   
        weight_ounces = weight_kg * 35.274
        ounces_label.config(text=f"Ounces: {weight_ounces:.2f}")

    except ValueError:
        error_label.config(text="Invalid input. Please enter a numeric value.")

window = tk.Tk()
window.title("Weight Converter")

weight_label = tk.Label(window, text="Enter weight in Kg:")
weight_label.pack()

weight_entry = tk.Entry(window)
weight_entry.pack()

convert_button = tk.Button(window, text="Convert", command=convert_weight)
convert_button.pack()

grams_label = tk.Label(window, text="Grams:")
grams_label.pack()

pounds_label = tk.Label(window, text="Pounds:")
pounds_label.pack()

ounces_label = tk.Label(window, text="Ounces:")
ounces_label.pack()

error_label = tk.Label(window, text="")
error_label.pack()

window.mainloop()
