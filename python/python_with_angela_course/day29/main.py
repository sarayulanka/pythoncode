from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    letter_list = [choice(letters) for character in range(1, randint(8, 10) + 1)]
    number_list = [choice(numbers) for character in range(1, randint(2, 4) + 1)]
    symbol_list = [choice(symbols) for character in range(1, randint(2, 4) + 1)]

    password_list = []

    password_list.extend(letter_list)
    password_list.extend(number_list)
    password_list.extend(symbol_list)

    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)








# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any empty fields.")
    else:

        is_true = messagebox.askokcancel(title=website, message=f'This is the data you have given:\n Website: {website} \n Email: {email} \n Password: {password} \n Is This information ok?')

        if is_true == True:
            with open('data.txt', mode='a') as data_file:
                data_file.write(f'{website} | {email} | {password}\n')

                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showinfo(message='The data transaction was successful!')
        else:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(message='Enter your new info and then click add.')

    
    

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('My Password Program')
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels:

website_label = Label(text='Website:', font=('Courier', 10, BOLD))
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:', font=('Courier', 10, BOLD))
email_label.grid(row=2, column=0)

password_label = Label(text='Password:', font=('Courier', 10, BOLD))
password_label.grid(row=3, column=0)



# Entries:

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, sticky=W, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, sticky=W,columnspan=2)

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, sticky=W)



# Buttons:

password_button = Button(text='Generate Password', command=generate_password)
password_button.grid(row=3, column=2)


final_button = Button(text='Add', width=36, command=save)
final_button.grid(row=4, column=1, sticky=W, columnspan=2)



window.mainloop()