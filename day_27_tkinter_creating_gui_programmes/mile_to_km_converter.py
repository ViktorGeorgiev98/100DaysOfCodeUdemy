from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=10, pady=10)
# window.minsize(width=300, height=200)

def calculate():
    value = int(entry_for_miles.get())
    label_km_value.config(text=value * 1.7)

entry_for_miles = Entry()
entry_for_miles.grid(column=1, row=0)
label_for_miles = Label(text="Miles")
label_for_miles.grid(column=2, row=0)
label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)
label_km_value = Label(text="0")
label_km_value.grid(column=1, row=1)
label_km = Label(text="km")
label_km.grid(column=2, row=1)
button_calculate = Button(text="Calculate", command=calculate)
button_calculate.grid(column=1, row=2)

window.mainloop()