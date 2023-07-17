from tkinter import *


def miles_to_km():
    miles = float(input_box.get())
    km = miles * 1.609
    change_km_label.config(text=f"{km}")


window = Tk()
window.title("Mile to km Converter")
window.config(padx=20, pady=20)


input_box = Entry(width=10)
input_box.grid(column=1, row=1)

miles_label = Label(text="Miles", font=("Arial", 10))
miles_label.grid(column=2, row=1)

equal_label = Label(text="is equal to", font=("Arial", 10))
equal_label.grid(column=0, row=2)

change_km_label = Label(text="0", font=("Arial", 10))
change_km_label.grid(column=1, row=2)

km_label = Label(text="km", font=("Arial", 10))
km_label.grid(column=2, row=2)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=3)


window.mainloop()

