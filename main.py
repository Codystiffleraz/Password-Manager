from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    
    # No empty fields
    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # Message box
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        
        # Adds data to the data.txt file
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)

logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website = Label(text="Website: ")
website.grid(row=1, column=0)
website_entry = Entry(width=53)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

username = Label(text="Email/Username: ")
username.grid(row=2, column=0)
username_entry = Entry(width=53)
username_entry.insert(0, "cody@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)

password = Label(text="Password: ")
password.grid(row=3, column=0)
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()