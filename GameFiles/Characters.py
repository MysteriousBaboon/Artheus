class player(object):
    def __init__(self, Shape_X):
        self.X = Shape_X
        self.Y = Shape_Y
        self.Width = Shape_Width
        self.Height = Shape_Height
        self.Shape = Shape
    if Shape == "Rectangle":
        draw_rectangle()

        def draw_rectangle():
            pygame.draw.rect(win, (Red, Green, Blue), (Shape_X, Shape_Y, Shape_Width, Shape_Height))