from turtle import Screen

class Start(Screen.Screen):

    def __init__(self):
        super().__init__()
        self.setup(width = 800, height = 600)
        self.bgcolor("black")
