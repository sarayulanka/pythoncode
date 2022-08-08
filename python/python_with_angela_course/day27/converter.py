from tkinter import *

window = Tk()
window.title('Converter program')
window.config(padx=20, pady=20)

def miles_to_kilos():
    x = int(input.get())*1.609344
    km_number = round(x, 2)
    km_amount['text']= km_number


km_number = 0

input = Entry(width=7)
input.grid(column=0, row=0)

miles = Label(text='Miles', font=('Arial', 10, 'bold'))
miles.grid(column=1, row=0)

is_equal_to = Label(text='is equal to ', font=('Arial', 10, 'bold'))
is_equal_to.grid(column=0, row=1)


km_amount = Label(text= f'{km_number}', font=('Arial', 10, 'bold'))
km_amount.grid(column=1, row=1)

km = Label(text= 'km.', font=('Arial', 10, 'bold'))
km.grid(column=2, row=1)



button = Button(text='Calculate!', command=miles_to_kilos)
button.grid(column=1, row=2)

window.mainloop()