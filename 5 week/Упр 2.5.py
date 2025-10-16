from tkinter import *
from tkinter import ttk


def imt(*args):
    try:
        weight = float(w.get())
        height = float(h.get())
        res.set(int(weight / (height * height)))
        r = weight / (height * height)
        if r < 18.5:
            i.set("Недостаточная (дефицит) масса тела")
        elif r < 25:
            i.set("Норма")
        elif r < 30:
            i.set("Избыточная масса тела (предожирение)")
        else:
            i.set("Ожирение")

    except ValueError:
        pass


root = Tk()
root.title("IMT")

mainframe = ttk.Frame(root, padding="4 4 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=2)
mainframe.columnconfigure(3, weight=2)
mainframe.columnconfigure(4, weight=1)

w = StringVar()
w_entry = ttk.Entry(mainframe, width=7, textvariable=w)
w_entry.grid(column=2, row=1, sticky=(W, E))

h = StringVar()
h_entry = ttk.Entry(mainframe, width=7, textvariable=h)
h_entry.grid(column=2, row=2, sticky=(W, E))

res = StringVar()
ttk.Label(mainframe, textvariable=res).grid(column=2, row=3, sticky=(W, E))

i = StringVar()
ttk.Label(mainframe, textvariable=i).grid(column=3, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=imt).grid(column=3, row=4, sticky=W)

ttk.Label(mainframe, text="weight (kg)").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="height (m)").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="imt:").grid(column=1, row=3, sticky=W)


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

w_entry.focus()

root.bind("<Return>", imt)

root.mainloop()
