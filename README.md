nba-term
=========
Fall asleep in the third quarter?  Working late and want to get a quick check of the scores? Get them right from your terminal with nba-term.  Just run `python scores.py` to find out the results of all of last night's NBA action.  

Or, if you've been on a bender, check out any night's results with a date argument in `YYYYMMDD` format.

`nba-term` works with Python 2 and 3.

Examples
--------
1. Christmas Day games in 2016:
```
python scores.py 20161225
```

2. See when Golden State blew a 3-1 to the Cavs:
```
python scores.py 20160619
```

Sample Output
-------------

```
╔═════════════════════════════════════════════╗
║                   CHA@GSW                   ║
║CHA                                       111║
║GSW                                       126║
╟─────────────────────────────────────────────╢
║Curry hits 11 3-pointers, scores 39 points   ║
╚═════════════════════════════════════════════╝
```
