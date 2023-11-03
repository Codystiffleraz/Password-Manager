from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data ={
        website:{
            "email": email,
            "password": password
        }
    }
    
    # No empty fields
    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
            
        except FileNotFoundError:
            # Checks if the file has been created already or not 
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                
        else:
            # Updating old data with new data
            data.update(new_data)
            
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:   
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            
            
# ---------------------------- FIND PASSWORD ------------------------------- #     
            
def find_password():
    website = website_entry.get()
        
    try:
        with open('data.json', "r") as json_file:
            data = json.load(json_file)
        
    except FileNotFoundError:
        messagebox.showinfo("Error", "no data found")
    else:
        if website in data:
            messagebox.showinfo(website, f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No detail for {website} exists.")
    

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
website_entry = Entry(width=34)
website_entry.focus()
website_entry.grid(row=1, column=1)

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
generate_password_button = Button(text="Generate Password", command=generate_password, width=14)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()