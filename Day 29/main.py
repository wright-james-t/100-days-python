from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #

FONT_NAME = "Comic Sans"
DEFAULT_UNAME = "fake-email@hotmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def genpass():
    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = ''.join(password_list)
    pyperclip.copy(password)
    entry_password.insert(0, password)


# ---------------------------- CONSTANTS ------------------------------- #

def search():
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="File not found", message="No data file found!")
    try:
        searched_user = data[entry_website.get()]["Username"]
        searched_pass = data[entry_website.get()]["Password"]
        messagebox.showinfo(title="Search", message=f"Username: {searched_user}\nPassword: {searched_pass}\n")
    except KeyError:
        messagebox.showwarning(title="Search", message="No results found!")
    except UnboundLocalError:
        pass

# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear_fields():
    entry_website.delete(0, 'end')
    entry_website.focus()
    entry_password.delete(0, 'end')
    if entry_uname != DEFAULT_UNAME:
        entry_uname.delete(0, 'end')
        entry_uname.insert(0, DEFAULT_UNAME)


def save():
    username = entry_uname.get()
    password = entry_password.get()
    website = entry_website.get()
    new_data = {
        website: {
            "Username": username,
            "Password": password
        }
    }

    if len(username) == 0 or len(password) == 0 or len(website) == 0:
        messagebox.showwarning(title="Oops", message=f"Please don't leave any fields blank.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details you entered\nEmail: {username}\nPassword:{password}")
        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            clear_fields()

# ---------------------------- UI SETUP ------------------------------- #


# Window
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website:")
label_website.grid(column=0, row=1, sticky="E")

label_uname = Label(text="Email/Username:")
label_uname.grid(column=0, row=2, sticky="E")

label_password = Label(text="Password:")
label_password.grid(column=0, row=3, sticky="E")


# Entries
entry_website = Entry()
entry_website.focus()
entry_website.grid(column=1, row=1, sticky="EW")

entry_uname = Entry()
entry_uname.insert(0, DEFAULT_UNAME)
entry_uname.grid(column=1, row=2, columnspan=2, sticky="EW")

entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")


# Buttons
button_generate = Button(text="Generate Password", command=genpass)
button_generate.grid(column=2, row=3, sticky="EW")

button_add = Button(text="Add", width=35, command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")

button_search = Button(text="Search", command=search)
button_search.grid(column=2, row=1, sticky="EW")

window.mainloop()

