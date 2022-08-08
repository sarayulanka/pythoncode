import turtle
import pandas

screen = turtle.Screen()
screen.title('US States Game!')
image = 'blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.tolist()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'correct answers: {len(guessed_states)}/50', prompt='Guess another state:').title()

    if answer_state == "Exit":
        excluded_answers = [state for state in all_states if state not in guessed_states]

        print('These are the states you missed:')
        for answer in excluded_answers:
            print(answer)
            
        break


    if answer_state in all_states and answer_state not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data.state == answer_state]
        t.goto(int(state.x),int(state.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
    else:
        continue

