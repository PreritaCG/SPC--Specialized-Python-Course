#Inch to Cms Converter
import tkinter as tk

def convert():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{cm:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

root = tk.Tk()
root.title("Inch to Centimeter Converter")

entry_label = tk.Label(root, text="Enter inches:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

#completed lesson3