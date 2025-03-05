import tkinter

# create new tkinter window
# window = tkinter.Tk()
# # add title
# window.title("My first GUI Program")
# # hardcode min size
# window.minsize(width=600, height=500)
#
# # Label
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "italic"))
# # you need to have the line below, otherwise the label will not show - geometry management system
# # expand true will try to fill the whole window
# # my_label.pack(expand=True)
# # my_label.pack(side="left")
# my_label.pack()

# how to put default values to functions
# you write a default value and then can execute the function without arguments
# def my_function(a=1, b=2, c=3):
#     print(a, b, c)
# my_function()

# you can also provide arguments to overwrite the old ones
# my_function(5, 10, 15)

# you do need to provide mandatory arguments
# def other_function(c, a=1, b=2,):
#     print(a, b, c)
# other_function(5)
# other_function(c=5)

# how to create functions with unlimited arguments
# def add(*args):
#     for n in args:
#         print(n)
# add(3, 5, 7, 10)
# basically the unlimited arguments logic is a tuple
# def add(*args):
# you can take argument from any position
# print(args[0])
#     sum = 0
#     for n in args:
#         sum += n
#     print(sum)
# add(1, 32, 531, 132, 12, 21, 32)

# how to create function with names keywords arguments. Now we can use named arguments.
# we can add other specific arguments as well
# def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # we can use all of the dictionary logic (object)
    # n += kwargs["add"]
    # print(n)
    # n *= kwargs["multiply"]
    # print(n)

# calculate(2, add=3, multiply=5)
# we can use keyword arguments in creating classes
# class Car:
#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw["model"]

# will print whatever we stated
# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.make)
# !!! it will fail if we use a keyword argument in the class creation but we do not add in the initialization
# use get instead !!!
# now it will work
# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#
# my_car = Car()


# continue with tkinter training

window = tkinter.Tk()
# add title
window.title("My first GUI Program")
# hardcode min size
window.minsize(width=600, height=500)

# Label
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "italic"))
# you need to have the line below, otherwise the label will not show - geometry management system
# my_label.pack()
# expand true will try to fill the whole window
# my_label.pack(expand=True)
# my_label.pack(side="left")
# change label text
# both lines below work the same way
# my_label["text"] = "New Text"
# my_label.config(text="New Text")


# function for button
# def button_clicked():
#     my_label.config(text=input.get())
# # Button - we do not need brackets for commands (click events)
# button = tkinter.Button(text="Click Me", command=button_clicked)
# # need to also use pack
# button.pack()
#
#
# # Entry - input
# input = tkinter.Entry(width=15)
# # need to also pack it
# input.pack()
# # to get value use 'get'
# # print(input.get())
#
# # Spinbox
# def spinbox_used():
#     # gets the current value in spinbox
#     print(spinbox.get())
# spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# # Scale
# # Called with current scale value
# def scale_used(value):
#     print(value)
# scale = tkinter.Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# # Check button
# def check_button_used():
# #     prints 1 if on and 0 if not on
#     print(checked_state.get())
# # variable to hold to checked state, 0 is of, 1 is on
# checked_state = tkinter.IntVar()
# checkbutton1 = tkinter.Checkbutton(text="Option 1", variable=checked_state, command=check_button_used)
# checkbutton2 = tkinter.Checkbutton(text="Option 1", variable=checked_state, command=check_button_used)
# checked_state.get()
# checkbutton1.pack()
# checkbutton2.pack()
#
# # Radio button
# def radio_used():
# #     prints 1 if on and 0 if not on
#     print(radio_state.get())
# # variable to hold to checked state, 0 is of, 1 is on
# radio_state = tkinter.IntVar()
# radiobutton1 = tkinter.Radiobutton(text="Option 1",value=1, variable=radio_state, command=radio_used)
# radiobutton2 = tkinter.Radiobutton(text="Option 1",value=2, variable=radio_state, command=radio_used)
# radio_state.get()
# radiobutton1.pack()
# radiobutton2.pack()
#
# # Listbox
# def listbox_used(event):
# #     gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
# listbox = tkinter.Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

# Layouts and positioning of widgets
# pack, place, grid

# PACK
# - packs widgets one below the other per default starting from the top
# you can use 'side' to put them somewhere, but you cannot use specific position

# PLACE - good if you have a small amount of widgets
# below line will place it in the top-left corner
# my_label.place(x=0, y=0)
# my_label.place(x=100, y=200)

# GRID - imagines our programme is a grid and can be divided into columns and rows (simillar to css grid)
# !!! important - children must be with grid as well, if you try with pack, you will get error
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "italic"))
my_label.grid(column=0, row=0)
button = tkinter.Button(text="Test1")
button.grid(column=2, row=0)
entry = tkinter.Entry()
entry.grid(column=3, row=2)

# How to add padding - directly use components like in css
window.config(padx=20, pady=20)



window.mainloop()