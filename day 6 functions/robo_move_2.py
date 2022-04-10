# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# use the above link to use the below code .
# the below code is the set of functions which will move robo by climbing walls and reach goal point


def turn_right():
    turn_left()
    turn_left()
    turn_left()



    
while at_goal() == False:
    if front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()