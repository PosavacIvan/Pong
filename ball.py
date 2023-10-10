from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

# Kretanje loptice kroz koordinatni sustav
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

# Određivanje novog smjera loptice po y osi nakon dodira vrha ili dna ekrana
    def bounce_y(self):
        #Mijenjamo smijer kretnje jer monožimo sa -1 i dobivamo negativan rezultat
        self.y_move *= -1

# Određivanje novog smjera loptice po x osi nakon dodira loptice sa lijevom ili densom palicom te povečanje brzine loptice
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

# Resetiranje pozicije i brzine loptice nakon što protivnik izgubi ili dobije bod
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
