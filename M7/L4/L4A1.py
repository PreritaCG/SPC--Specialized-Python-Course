# Import necessary packages 
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Setup Root Window
window = Tk()
window.title("Codingal's Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Function to Open a file
def open_file():
	"""Open a file for editing."""
	filepath = askopenfilename(
		filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
	)
	if not filepath:
		return
	txt_edit.delete(1.0, END)
	# if a file is opened then display the contents of the file
	with open(filepath, "r") as input_file:
		# Read contents of the input file
		text = input_file.read()
		# Insert contents of the file in the editor box
		txt_edit.insert(END, text)
		input_file.close()
	window.title(f"Codingal's Text Editor - {filepath}")

# Function to Save a file
def save_file():
    # Save the current file as a new file
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
		# Read the edited content and update in the output file
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"Codingal's Text Editor - {filepath}")

# Add widgets in the application
txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()

'''
# impoert necessary libraries
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# setup root window
window=Tk()
window.title("codingals text editor")
window.geometry("600x600")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=500, weight=1)

# function to open a file
def open_file():
    # open a flie for editing
    filepath= askopenfilename(filetypes=[("Text files", "*.txt"),("all files", "*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0,END)
    # if a flie is opened then display the contents of the file
    with open(filepath, 'r') as input_file:
        # read the contents of the input file
        text=input_file.read()
        # insert contents of the file in the editior box
        txt_edit.insert(END, text)
        input_file.close()
    window.title(f'Codingals text editor-{filepath}')

# function to save a file
def save_file():
    # save current file
    filepath= asksaveasfilename(defaultextension='txt', filetypes=[("text file", "*.txt"),("all files", "*.*") ])

    if not filepath:
        return
    with open(filepath, 'w') as output_file:
        text= txt_edit.get(1.0,END)
        output_file.write(text)
    window.title(f'Codingals text editor-{filepath}')

# add widgets
txt_edit=Text(window)
fr_buttons=Frame(window, relief=RAISED, bd=2)
btn_open= Button(fr_buttons, text='open', command=open_file)
btn_save= Button(fr_buttons, text='save as...', command=save_file)

btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
btn_save.grid(row=0, column=0, sticky='ew',padx=5)

fr_buttons.grid(row=0, column=0, sticky='ns')
txt_edit.grid(row=0, column=1, sticky='nsew')

window.mainloop()'''