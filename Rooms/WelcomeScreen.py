from GameFrame import Level

class WelcomeScreen(Level):
    """
    Intial screen for game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)