from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        value = v.get()
        res.set(float(eval(value)))

    except ValueError:
        pass


root = Tk()
root.title("calc")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


v = StringVar()
v_entry = ttk.Entry(mainframe, width=7, textvariable=v)
v_entry.grid(column=2, row=1, sticky=(W, E))

res = StringVar()
ttk.Label(mainframe, textvariable=res).grid(column=2, row=2, sticky=(W, E))


ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=4)


ttk.Label(mainframe, text="выражение:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="результат:").grid(column=1, row=2, sticky=W)


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)


v_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
