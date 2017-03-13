from __future__ import print_function
from datetime import date, timedelta

import json
import requests
import re
import sys

class Scorebox(object):
    """Creates a box score for NBA
    """

    def __init__(self, vTeam, vScore, hTeam, hScore, nugget, totalwidth):
        """Initialize a new Scorebox object.

        Args:
            vTeam (str): Visiting team's triCode
            vScore (str): Visiting team's score
            hTeam (str): Home team's triCode
            hScore (str): Home team's score
            nugget (str): Game nugget
            totalwidth(str): Width of the box scores
        """

        self.vTeam = vTeam
        self.vScore = vScore
        self.hTeam = hTeam
        self.hScore = hScore
        self.nugget = nugget
        self.totalwidth = totalwidth

        # set the total width of the box
        if len(self.nugget) == 0:
            self.nugget = u'\u2573' * self.totalwidth

        # fix the right justify variable if the nugget is shorter than the totalwidth
        if len(self.nugget) < self.totalwidth:
            rjust = (self.totalwidth-len(self.nugget)) + 1
        else:
            rjust = self.totalwidth-len(self.nugget)

        top = u'\u2554' + u'\u2550' * self.totalwidth + u'\u2557' + '\n'
        matchup = u'\u2551' + (self.vTeam + '@' + self.hTeam).rjust((self.totalwidth+7)/2) + u'\u2551'.rjust((self.totalwidth-((self.totalwidth+7)/2))+1) + '\n'
        visitor = u'\u2551' + self.vTeam + self.vScore.rjust(self.totalwidth - 3) + u'\u2551' + '\n'
        home = u'\u2551' + self.hTeam + self.hScore.rjust(self.totalwidth - 3) + u'\u2551' + '\n'
        divider = u'\u255f' + u'\u2500' * self.totalwidth + u'\u2562' + '\n'
        bottom = u'\u255a' + u'\u2550' * self.totalwidth + u'\u255d' + '\n'
        nugget = u'\u2551' + self.nugget + u'\u2551'.rjust(rjust) + '\n'

        self.scorebox = top + matchup + visitor + home + divider + nugget + bottom

def get_scores(dt):
    url = 'http://data.nba.net/data/10s/prod/v1/' + dt + '/scoreboard.json'

    res = requests.get(url)

    datadict = res.json()

    num_games = str(datadict['numGames'])
    if num_games == '0':
        return "No games played on this date."

    # all boxes should be the same size, represented by the length
    # of the longest game nugget
    nuggets = list()
    for g in datadict['games']:
        nuggets.append(len(str(g['nugget']['text']).strip()))

    totalwidth = max(nuggets) or 40
    boxes = list()

    for g in datadict['games']:
        vTeam = str(g['vTeam']['triCode'])
        vScore = str(g['vTeam']['score'])
        hTeam = str(g['hTeam']['triCode'])
        hScore = str(g['hTeam']['score'])
        nugget = str(g['nugget']['text']).strip()

        box = Scorebox(vTeam, vScore, hTeam, hScore, nugget, totalwidth)
        boxes.append(box.scorebox)

    return boxes

if __name__ == '__main__':

    if len(sys.argv) == 1:
        # the default is last night's games
        dt = re.sub('-','',str(date.today() - timedelta(1)))
    else:
        dt = sys.argv[1]

    scores = get_scores(dt)

    if isinstance(scores, list):
        for game in scores:
            print(game)
    else:
        print(scores)
