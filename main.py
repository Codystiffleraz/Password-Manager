from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_entry.grid(row=1, column=1, columnspan=2)

username = Label(text="Email/Username: ")
username.grid(row=2, column=0)
username_entry = Entry(width=53)
username_entry.grid(row=2, column=1, columnspan=2)

password = Label(text="Password: ")
password.grid(row=3, column=0)
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=45)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()