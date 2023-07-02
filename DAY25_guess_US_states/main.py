import turtle
import pandas

screen = turtle.Screen()
screen.title('Guess U.S states')

screen.addshape('blank_states_img.gif')
turtle.shape('blank_states_img.gif')

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'Guessed {len(guessed_states)}/50 states',prompt='guess one of the states').title()

    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states to learn')
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)


def coordi_on_click(x,y):
    print(x,y)
turtle.onscreenclick(coordi_on_click)


