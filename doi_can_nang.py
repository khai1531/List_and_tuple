import tkinter as tk

def convert_weight():
    try:
        # Get the weight value from the entry field
        weight_kg = float(weight_entry.get())

        # Convert weight to grams
        weight_grams = weight_kg * 1000
        grams_label.config(text=f"Grams: {weight_grams:.2f}")

        # Convert weight to pounds
        weight_pounds = weight_kg * 2.20462
        pounds_label.config(text=f"Pounds: {weight_pounds:.2f}")

        # Convert weight to ounces
        weight_ounces = weight_kg * 35.274
        ounces_label.config(text=f"Ounces: {weight_ounces:.2f}")

    except ValueError:
        # Handle invalid input (non-numeric)
        error_label.config(text="Invalid input. Please enter a numeric value.")

# Create the main window
window = tk.Tk()
window.title("Weight Converter")

# Create labels and entry fields for Kg input and weight conversion results
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

# Run the main event loop
window.mainloop()
