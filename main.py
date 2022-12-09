# from tkinter import *


# def add(*args):
#     a = 0
#     for n in args:
#         a += n
#     print(a)
# add(2, 5, 7, 9)

# def calculate(n, **kwargs):
#     print(kwargs)
#
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
# calculate(2, add=3, multiply=5)



def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.pack()


#Button
button = Button(text="Click Me", command=button_clicked)
button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)


# my_label = Label(text="New text", font=("Arial", 22, "bold"))
# my_label.pack()
# def button_clicked():
#     my_label.config(text=input.get())
#
# my_button = Button(text="Click here", command=button_clicked)
# my_button.pack()
#





mainloop()

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {key: (value*9/5)+32 for (key, value) in weather_c.items()}
#
# print(weather_f)
