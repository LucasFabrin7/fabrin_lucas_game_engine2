from random import randint

# game settings 
WIDTH = 1080
HEIGHT = 768
FPS = 30
SCORE = 0

# player settings
PLAYER_JUMP = 30
PLAYER_GRAV = 1.5

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKYBLUE = (150, 200, 255)

# Starting platforms and coding the random color generator using randint for RGB values
# sets up the position of the platforms with any extra conditions like moving
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, " ", RED),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, " ", ((randint(0, 255)), randint(0, 255), randint(0, 255))),
                 (125, HEIGHT - 350, 100, 20, "moving", ((randint(0, 255)), randint(0, 255), randint(0, 255))),
                 (350, 200, 100, 20, " ", ((randint(0, 255)), randint(0, 255), randint(0, 255))),
                 (175, 100, 50, 20, " ", ((randint(0, 255)), randint(0, 255), randint(0, 255))),
                 (45, 250, 50, 20, " ", ((randint(0, 255)), randint(0, 255), randint(0, 255))),
                 (280, 350, 50, 20, " ", ((randint(0, 255)), randint(0, 255), randint(0, 255)))
                 ]

# postiion of the winning dot and the color
WINNING_DOT = [(200, 120, 20, 20, BLUE),
               ]

