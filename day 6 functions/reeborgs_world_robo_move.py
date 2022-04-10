# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# use the above link to use the below code .
# the below code is the set of functions which will move robo by climbing walls and reach goal point

def turn_right():
    turn_left()
    turn_left()
    turn_left()

for each in range(1,7):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()