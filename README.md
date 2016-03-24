nba_stats
===

A utility for accessing data from the NBA stats website. 

Note: all data is property of the NBA, this is merely a utility to make programmatic access of the data easier.

### Install: 

Coming soon.. If you want to try it out, clone the repo and include nba_stats.py


### Example Usage:

nba_stats currently has player season stats implemented. I am currently working on expanding the functionality.

```
from nba_stats import Player

lebron = Player("LeBron James")
print lebron.stats        # return LeBron's career stats as a list of dicts
lebron.stats.keys()       # shows the different stat options available

print lebron.df()         # returns a pandas DataFrame of stats. 
                          # Defaults to SeasonTotalsRegularSeason
```
