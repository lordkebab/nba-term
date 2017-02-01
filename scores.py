from __future__ import print_function
from datetime import date, timedelta
from scorebox import Scorebox

import json
import urllib2
import re
import sys

def get_scores(dt):
    url = 'http://data.nba.net/data/10s/prod/v1/' + dt + '/scoreboard.json'

    res = urllib2.urlopen(url)
    data = res.read()
    datadict = json.loads(data)

    num_games = str(datadict['numGames'])
    games = list()

    for g in datadict['games']:
        vTeam = str(g['vTeam']['triCode'])
        vScore = str(g['vTeam']['score'])
        hTeam = str(g['hTeam']['triCode'])
        hScore = str(g['hTeam']['score'])
        nugget = str(g['nugget']['text'])

        box = Scorebox(vTeam, vScore, hTeam, hScore, nugget)
        print(box.scorebox)

if __name__ == '__main__':

    if len(sys.argv) == 1:
        # the default is last night's games
        dt = re.sub('-','',str(date.today() - timedelta(1)))
    else:
        # user supplied an argument, see if it's valid YYYYMMDD
        dt = sys.argv[1]
        try:
            # this is not very good but it'll do for now
            # TODO: meh, make this a little better
            date(dt)
        except:
            print(dt + " is not in YYYYMMDD format or is not a valid date.")

    gamesdict = get_scores(dt)
