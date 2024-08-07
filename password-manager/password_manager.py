from tkinter import *
from tkinter import messagebox
from random import choices, shuffle
from string import punctuation, digits, ascii_lowercase, ascii_uppercase
# import pyperclip
import csv
import json

DEFAULT_EMAIL = "your_email@email.com"


def generate_password():
    # special_char = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(91, 97)] + [chr(i) for i in range(123, 127)]
    numbers = [chr(i) for i in range(48, 58)]
    big_letters = [chr(i) for i in range(65, 91)]
    small_letters = [chr(i) for i in range(97, 123)]
    # special_char = punctuation
    # numbers = digits
    # big_letters = ascii_uppercase
    # small_letters = ascii_lowercase
    pw =  choices(numbers, k=1) + choices(big_letters, k=1) + choices(small_letters, k=16)
    shuffle(pw)
    for i in range(6,14,7):
        pw.insert(i, "-")
    return ''.join(pw)


def open_json():
    try:
        with open("test.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return None
    return data


def find_password(website):
    data = open_json()
    if data is None:
        messagebox.showinfo("Empty", "There are no saved passwords in this system.")
        web_entry.delete(0, END)
        return
    if website in data:
        info = data[website]
        messagebox.showinfo("Found", f"Website:{website}\nUser Info:{info['User']}\nPassword:{info['Password']}")
        web_entry.delete(0, END)
    else:
        messagebox.showinfo("Not Found", "There is no password for this website.")
        web_entry.delete(0, END)


def show_clicked():
    info = open_json()
    if info is None:
        messagebox.showerror("Error", "The user info entered is emtpy.")
    else:
        display = []
        for key, value in info.items():
            display.append(f"Website: {key}\nUser info: {value['User']}\nPassword: {value['Password']}\n\n")
        message = ''.join(display)
        messagebox.showinfo("User Info", message)


def search_clicked():
    website = web_entry.get()
    response = False
    if website == '':
        response = messagebox.showerror("Error", "The website info entered is emtpy.")
    if response:
        web_entry.delete(0, END)
    else:
        find_password(website)


def pw_clicked():
    if pw_entry.get() != '':
        pw_entry.delete(0, END)
    password = generate_password()
    pw_entry.insert(0, password)


def add_clicked():
    response = False
    website = web_entry.get()
    if website == '':
        response = messagebox.showerror("Error", "The website info entered is emtpy.")
    user_info = user_entry.get()
    if user_info == '':
        response = messagebox.showerror("Error", "The user info entered is emtpy.")
    password = pw_entry.get()
    if password == '':
        response = messagebox.showerror("Error", "The password entered is emtpy.")

    if not response:
        data_to_csv = [website, user_info, password]
        data_to_json = {
            website: {
                "User": user_info,
                "Password": password
            }
        }
        response = messagebox.askyesnocancel(title="Saved Info", message="Are you sure you wish to proceed?")
        if response:
            with open("test.csv", "a") as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerows([data_to_csv])

            data = open_json()
            if data is None:
                data = data_to_json
            else:
                data.update(data_to_json)

            with open("test.json", "w") as file:
                json.dump(data, file, indent=2)
                web_entry.delete(0, END)
                pw_entry.delete(0, END)
                user_entry.delete(0, END)
                user_entry.insert(0, DEFAULT_EMAIL)
                web_entry.focus()
                messagebox.showinfo("Success", "Your user info and password were saved.")
                return
        elif response is None:
            messagebox.showinfo("Cancel", "Please modify your user info and password.")
            pass
        else:
            web_entry.delete(0, END)
            pw_entry.delete(0, END)
            user_entry.delete(0, END)
            user_entry.insert(0, DEFAULT_EMAIL)
            web_entry.focus()
            messagebox.showinfo("Failure", "The information was not saved.")


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:", width=12, anchor="e", bg="white", highlightthickness=0)
web_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:", width=12, anchor="e", bg="white", highlightthickness=0)
user_label.grid(column=0, row=2)

pw_label = Label(text="Password:", width=12, anchor="e", bg="white", highlightthickness=0)
pw_label.grid(column=0, row=3)

web_entry = Entry(highlightbackground="white")
# web_entry.insert(END, string="Enter site")
web_entry.focus()
web_entry.grid(column=1, row=1, sticky="ew")

user_entry = Entry(width=36, highlightbackground="white")
user_entry.insert(0, DEFAULT_EMAIL)
user_entry.grid(column=1, row=2, columnspan=2)

pw_entry = Entry(width=21, highlightbackground="white")
pw_entry.grid(column=1, row=3)

search_button = Button(text="Search", highlightbackground="white", command=search_clicked)
search_button.grid(column=2, row=1, sticky="ew")

pw_button = Button(text="Generate Password", width=11, highlightbackground="white", command=pw_clicked)
pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=34, highlightbackground="white", command=add_clicked)
add_button.grid(column=1, row=4, columnspan=2)

empty_label = Label(bg="white", highlightthickness=0)
empty_label.grid(column=1, row=6, columnspan=2)

show_all_button = Button(text="Show All", width=34, highlightbackground="white", command=show_clicked)
show_all_button.grid(column=1, row=7, columnspan=2)

window.mainloop()

if __name__ == '__main__':
    pass
