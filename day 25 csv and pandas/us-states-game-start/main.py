from turtle import Turtle, Screen
import pandas
screen = Screen()
turtle = Turtle()
screen.title("Find U.S STATES")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape("blank_states_img.gif")


# def get_screen_click_coor(x, y):
#     print(x, y)
#
#
# screen.onscreenclick(get_screen_click_coor)
#
#
# screen.mainloop()
guessed_state = []
while len(guessed_state) < 50:
    answer = screen.textinput(title=f"{len(guessed_state)}/50 States correct ",
                              prompt="What the another state name").title()
    data = pandas.read_csv("50_states.csv")
    state_list = data.state.to_list()
    if answer == "Exit":
        missing_state = []
        for each in state_list:
            if each not in guessed_state:
                missing_state.append(each)
        break
    if answer in state_list:
        guessed_state.append(answer)
        word = Turtle()
        word.hideturtle()
        word.penup()
        searched_data = data[data.state == answer]
        xcor = int(searched_data.x)
        ycor = int(searched_data.y)
        word.goto(xcor, ycor)
        word.write(searched_data.state.item())


missed_state = pandas.DataFrame(missing_state)
missed_state.to_csv("missed_state.csv")
