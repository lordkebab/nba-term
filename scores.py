from __future__ import print_function
from datetime import date, timedelta

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
        d = {
            'vTeam': {
                'triCode': str(g['vTeam']['triCode']),
                'score': str(g['vTeam']['score'])
            },
            'hTeam': {
                'triCode': str(g['hTeam']['triCode']),
                'score': str(g['hTeam']['score'])
            },
            'nugget': str(g['nugget']['text'])
        }

        games.append(d)

    gamesdict = {
        'numGames': num_games,
        'games': games
    }

    print(json.dumps(gamesdict, indent=4, sort_keys=True))

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
