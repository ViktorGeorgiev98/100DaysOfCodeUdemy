# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json


# ---------------------------- SAVE PASSWORD ------------------------------- #
# generate password function
def generate_strong_password(length=15):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(characters, k=length))
    return password


# insert generated password to the input field function
def insert_generated_password():
    new_password = generate_strong_password()
    password_entry.delete(0, END)
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)


# add password to file function


def add_password():
    website = website_input.get()
    email = email_input.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}
    if not website or not email or not password:
        messagebox.showerror(
            title="All fields are mandatory!",
            message="Please fill website, email and password",
        )
        return
    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?",
    )
    if is_ok:
        new_entry = f"{website} | {email} | {password}"
        # write to json file
        # json.dump(new_data, password_manager, indent=4)
        # read json file
        # data = json.load(password_manager)
        # print(data)
        # update json file
        # first read old data, then update old data with new data, save updated data with the normal json write method
        # data.update(new_data)
        # json.dump(data, password_manager, indent=4)
        try:
            with open(
                "./day_29_build_password_manager_app/data.json", mode="r"
            ) as password_manager:
                data = json.load(password_manager)
        except FileNotFoundError:
            with open(
                "./day_29_build_password_manager_app/data.json", mode="w"
            ) as password_manager:
                json.dump(new_data, password_manager, indent=4)
        else:
            data.update(new_data)
            with open(
                "./day_29_build_password_manager_app/data.json", mode="w"
            ) as password_manager:
                json.dump(data, password_manager, indent=4)
        finally:
            website_input.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(height=200, width=200)
lock_img = PhotoImage(file="./day_29_build_password_manager_app/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "test@abv.bg")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(
    text="Generate Password", command=insert_generated_password
)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
