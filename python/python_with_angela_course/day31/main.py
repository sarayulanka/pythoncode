from tkinter import *
import pandas
import random

from pandas.core.base import IndexOpsMixin

BACKGROUND_COLOR = "#B1DDC6"
new_card = {}

try:
    data_file = pandas.read_csv('data/words_to_learn.csv')
except:
    original = pandas.read_csv('data/french_words.csv')
    to_learn = original.to_dict(orient='records')
else:
    to_learn = data_file.to_dict(orient='records')



def word_generator():
    global new_card, flip_timer
    window.after_cancel(flip_timer)
    new_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text='french', fill='black')
    canvas.itemconfig(card_word, text=f"{new_card['French']}", fill='black')
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=new_card['English'], fill='white')


def known_card():
    to_learn.remove(new_card)
    print(len(to_learn))

    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)



    word_generator()



window = Tk()
window.title('Flashcard program')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))
canvas.grid(row=1,column=1, columnspan=2)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=known_card)
known_button.grid(row=2, column=2)


wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=word_generator)
unknown_button.grid(row=2, column=1)

word_generator()


window.mainloop()