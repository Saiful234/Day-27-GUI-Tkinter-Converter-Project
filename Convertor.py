from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)

def convertor():
    result_int = int(user_input.get())
    result = round(result_int * 1.609)
    result_label.config(text=str(result))
    return

user_input = Entry()
user_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

button = Button(text="Calculate", command= convertor)
button.grid(column=1, row=2)


window.mainloop()