import tkinter.messagebox
from tkinter import *
import random
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)
def generate_password():
    global letters
    global numbers
    global symbols
    l = [random.choice(letters) for _ in range(nr_letters) ]
    s = [random.choice(symbols) for _ in range(nr_symbols)]
    n = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = l + s + n
    random.shuffle(password_list)
    # merge array into one string
    password = ''.join(password_list)
    password_textbox.insert(0, password)

def save_password():
    website = website_textbox.get()
    username = username_textbox.get()
    password = password_textbox.get()

    if len(website) <= 0 or len(username) <= 0 or len(password) <= 0:
        messagebox.showerror(title="Missing Fields", message="there are some missing fields")
    else:
        is_ok =  messagebox.askokcancel(title=f"{website}", message=f"there are the details entered: \nEmail:- {username}  \nPassword :- {password} \n "f"Is it ok to save ?")
        if is_ok:
            if len(website) > 0 and len(username) > 0 and len(password) > 0 :
                with open('password.txt', mode='a') as file:
                    file.write(f"Website : {website} | Username : {username} | password : {password}\n")

                # to clear fields after saving data into txt
                    website_textbox.delete(0, END)
                    password_textbox.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website')
website_label.grid(column=0, row=1)

website_textbox = Entry(width=35 )
website_textbox.grid(column=1, row=1, columnspan=2)
website_textbox.focus()


username_label = Label(text='Email/Username')
username_label.grid(column=0, row=3)

username_textbox = Entry(width=35)

'''
insert used to prepopulate data into text box, insert method 2 paramerter 1 index , 2 data/ string
index : 0 means start of texzt box
END :- constant, which means it add string at end of text box value
'''
username_textbox.insert(END, 'abhishek.paliwal@gmail.com')
username_textbox.grid(column=1, row=3, columnspan=2)


password_label = Label(text='Password')
password_label.grid(column=0, row=4)

password_textbox = Entry(width=21)
password_textbox.grid(column=1, row=4)

gen_pass_button = Button(text='Generate Password', command=generate_password)
gen_pass_button.grid(column=2, row=4)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(column=1, row=5, columnspan=2)









window.mainloop()