from tkinter import *

# def button_clicked():
#     print("I got clicked")
#     user_text = user_input.get()
#     my_label.config(text=user_text)
#
window = Tk()
window.title("My First GUI")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)
#
# my_label = Label(text="I am a label", font=("Arial", 24))
# my_label.config(text="New Text")
# # my_label.pack()
# # my_label.place(x=100, y=200)
# my_label.grid(column=1, row=1)
# my_label.config(padx=20, pady=20)
#
#
# button = Button(text="Click me", command=button_clicked)
# button.grid(column=2, row=2)
#
# new_button = Button(text="New button", command=print("New button clicked"))
# new_button.grid(column=3, row=1)
#
# user_input = Entry(width=10)
# user_input.grid(column=4, row=3)

# entry at 2-1, label (miles) at 3-1
# label (is equal to) at 2-1, entry at 2-2 (0 as starting text), label (km) at 3-2
# button (calculate) at 2-3


def convert_calculation():
    km = float(miles_input.get()) * 1.609
    converted_label.config(text=km)


miles_input = Entry(width=10)
miles_input.grid(column=2, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)

eq_label = Label(text="is equal to")
eq_label.grid(column=1, row=2)

converted_label = Label(text="0")
converted_label.grid(column=2, row=2)

km_label = Label(text="Km")
km_label.grid(column=3, row=2)

calc_button = Button(text="Calculate", command=convert_calculation)
calc_button.grid(column=2, row=3)

window.mainloop()