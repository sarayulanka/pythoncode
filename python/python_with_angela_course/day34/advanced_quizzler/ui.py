from tkinter import *
from quiz_brain import QuizBrain

# Class based tkinter GUI
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz  = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='Statement goes here.', width=280, font=('arial', 15, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2)


        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, font=('Arial', 15, 'italic'))
        self.score_label.grid(row=0, column=1)

        self.true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=self.true_image, highlightthickness=0, bg=THEME_COLOR, pady=20, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=self.false_image, highlightthickness=0, bg=THEME_COLOR, pady=20, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions() == True:
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of this quiz! Your final score is {self.quiz.score}/10.")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg='green')

        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)

