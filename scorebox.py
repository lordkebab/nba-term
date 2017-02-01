class Scorebox(object):
    """Creates a box score for NBA
    """

    def __init__(self, vTeam, vScore, hTeam, hScore, nugget):
        """Initialize a new Scorebox object.

        Args:
            vTeam (str): Visiting team's triCode
            vScore (str): Visiting team's score
            hTeam (str): Home team's triCode
            hScore (str): Home team's score
            nugget (str): Game nugget
        """

        self.vTeam = vTeam
        self.vScore = vScore
        self.hTeam = hTeam
        self.hScore = hScore
        self.nugget = nugget

        # set the total width of the box
        if len(self.nugget) == 0:
            self.totalwidth = 26
        else:
            self.totalwidth = len(self.nugget)

        top = u'\u250c' + u'\u2500' * self.totalwidth + u'\u2510' + '\n'
        visitor = u'\u2502' + self.vTeam + self.vScore.rjust(self.totalwidth - 3) + u'\u2502' + '\n'
        home = u'\u2502' + self.hTeam + self.hScore.rjust(self.totalwidth - 3) + u'\u2502' + '\n'
        bottom = u'\u2514' + u'\u2500' * self.totalwidth + u'\u2518' + '\n'

        self.scorebox = top + visitor + home + bottom
