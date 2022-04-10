# http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# use the above link to use the below code .
# the below code is the set of functions which will move robo to clear whatever the maze and reach it to goal.




def turn_right():
    turn_left()
    turn_left()
    turn_left()



while at_goal() == False:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
  