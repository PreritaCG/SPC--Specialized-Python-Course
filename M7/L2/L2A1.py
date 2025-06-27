from tkinter import *

root = Tk()
root.title('Number Pad')
root.geometry('250x300')

nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ['#', 0, '*']]

for i in range(4):
    root.rowconfigure(i, weight=1)
    for j in range(3):
        root.columnconfigure(j, weight=1)
        btn = Button(
            root,
            text=str(nums[i][j]),
            font=('Arial', 18),
            bg='#d0efff'
        )
        btn.grid(row=i, column=j, sticky='nsew', padx=0.5, pady=)

root.mainloop()