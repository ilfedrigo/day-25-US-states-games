import turtle
import pandas

states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0
correct_guesses = []

while score < 50:
    guess = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    
    if guess == "Exit" or guess == "Quit":
        missing_states = [state for state in all_states if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States-to-learn.csv")
        break
    
    if guess in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guess)
        score += 1
        correct_guesses.append(guess)



turtle.mainloop()