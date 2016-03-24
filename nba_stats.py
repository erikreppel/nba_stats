import requests
import json
import pandas as pd

HEADERS = {'User-Agent': 'Mozilla/5.0'}


class Player:

    def __init__(self, player_name, stat_type='PerGame'):
        """
        player_name: an NBA players full name including spaces
        stat_type: "PerGame"||"Totals"||"Per36"
        """
        self.player_name = player_name
        league_leaders_url = 'http://stats.nba.com/stats/leagueleaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2015-16&SeasonType=Pre+Season&StatCategory=REB'
        league_leaders = requests.get(
            league_leaders_url, headers=HEADERS).json()
        self.player_ids = {i[2]: i[0]
                           for i in league_leaders['resultSet']['rowSet']}

        self.stats = {}
        self.get_career_stats(player_name, stat_type)

    def df(self, season_type='SeasonTotalsRegularSeason'):
        s = self.stats[season_type]
        return pd.DataFrame(s['seasons'], columns=s['headers'])

    def get_career_stats(self, player_name, stat_type='PerGame'):
        career_url = '''http://stats.nba.com/stats/playercareerstats?LeagueID=00&PerMode=%(stat_type)s&PlayerID=%(player_id)s''' % \
            {
                "stat_type": stat_type,
                "player_id": self.player_ids[player_name]
            }
        resp = requests.get(career_url, headers=HEADERS)
        # print resp
        if resp.status_code != 200:
            raise Exception(resp.text)
        else:
            data = resp.json()
            headers = data['resultSets'][0]['headers']
            for i in data['resultSets']:
                print i['name']

                parsed = []
                for row in range(len(i['rowSet'])):
                    season = {}
                    for j in range(len(i['rowSet'][row])):
                        season[headers[j]] = i['rowSet'][row][j]
                    parsed.append(season)
                self.stats[i['name']] = {
                    'headers': headers,
                    'seasons': parsed
                }


if __name__ == "__main__":
    lebron = Player("LeBron James", "PerGame")
    # print lebron.stats['SeasonTotalsRegularSeason']

    s = lebron.stats['SeasonTotalsRegularSeason']
    print pd.DataFrame(s['seasons'], columns=s['headers'])
    print s['seasons']
