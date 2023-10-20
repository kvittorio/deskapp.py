import csv
import tkinter as tk
from tkinter import filedialog

def convert_text_to_csv():
    input_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not input_file:
        return

    output_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

    with open(input_file, 'r') as text_file, open(output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=selected_option.get())
        
        for line in text_file:
            parts = line.strip().split()
            country = ' '.join(parts[:-12])
            numbers = parts[-12:]
            csv_writer.writerow([country] + numbers)

    result_label.config(text=f'Data has been successfully converted to {output_file}')

# Create a Tkinter window
window = tk.Tk()
window.title("Конвертер")

button_label = tk.Label(window, text="Select delimiter:")

selected_option = tk.StringVar()
# newvar = {"|": "pipe", ", ": "commma", ";": "semicolon", "\t": "tab"}
readable_to_value = {
    "Pipe": "|",
    "Tab": "\t",
    "Comma": ",",
    "Semicolon": ";"
}
options = list(readable_to_value.keys())
selected_option.set(options[0])
option_menu = tk.OptionMenu(window, selected_option, *options)

# Create a Button widget with a label (name) and associate it with a function
convert_button = tk.Button(window, text="Convert", command=convert_text_to_csv)

# Create a Label widget to add a name or description to the button
result_label = tk.Label(window, text="")

button_label.pack()  # Add the label for the dropdown button
option_menu.pack()
convert_button.pack()
result_label.pack()

window.mainloop()