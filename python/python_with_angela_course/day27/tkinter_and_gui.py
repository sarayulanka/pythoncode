# In this file, we are going to learn about tkinter module that will help us create
# graphic user interfaces(GUI)

from tkinter import *

# The line of code below creates a window using the Tk class()
window = Tk()
window.title('1st GUI program')

# minsize lets you specify what you want the default value to be
window.minsize(500, 300)

# Let's try creating a label on our window using the Label class:
label = Label(text='This is a label', font=('Arial', 18, 'bold'))

# The line above creates a label but the label won't show up on the screen without the line below
# the pack method ensures that the label actually is visible
label.pack()

# An input class called Entry in the tkinter module:

input = Entry(width=10)
input.pack()
print(input.get())


# Now let's try creating a button using the button class:

def button_clicked():
    # This function will determine what should happen when the button is clicked
    new_text = input.get()
    label['text'] = new_text

button = Button(text='Click Me!', command=button_clicked)
button.pack()


# Now, pack is a label manager and it basically just packs all of the features together unless you specify
#  where you want each element but the thing is you cannot specify a specific place of where you want the
# feature to go which is why we are going to learn about two other types of label managers

# The Place() label manager is all about precise positioning
# It's so specific, that you have to provide an x and y value as arguments instead of words like left, 
# right, up, or down.

# Let's try using the place() table manager:

new_label = Label(text='I am going to use place() instead of pack()', font=('Arial', 10, 'bold'))
new_label.place(x=100, y=167)

# Now there is one last type of label manager named: grid()
# Grid() is not about x and y coordinates or positioning things by inaccurate words,
# Grid() is about rows and columns, it is precise but not too precise

# One warning about grid though is that you cannot use pack() and grid() in the same code
# Because these two methods are incompatible with each other

# I commented out the code below out because because I am using pack() in the code above 
# and grid and pack are not compatible

# But here is how you use grid:

# new_button = Button(text='New Button')
# new_button.grid(column=3, row=3)



window.mainloop()
# mainloop() has to be at the end of the program with
#  the tkinter method just like how exitonclick has to be the last thing in any turtle functionality