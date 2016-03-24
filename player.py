import requests

class Player:
    def __init__(self, name):
        self.name = name
        
def get_player_stats(date_from='',
                     date_to='',
                     game_segment='',
                     last_n_games='0',
                     league_id='00',
                     location='',
                     measure_type='Base',
                     month='0',
                     opponent_team_id='0',
                     outcome='',
                     po_round='',
                     pace_adjust='N',
                     per_mode='PerGame',
                     period='0',
                     player_id='203080',
                     plus_minus='N',
                     rank='N',
                     season='2015-16',
                     season_segment='',
                     season_type='Regular+Season',
                     ShotClockRange='',
                     vs_conference='',
                     vs_division=''
                     ):
    stats_url = 'http://stats.nba.com/stats/playerdashboardbygeneralsplits?DateFrom=%s&DateTo=%s&GameSegment=%s&LastNGames=%s&LeagueID=%s&Location=%s&MeasureType=%s&Month=%s&OpponentTeamID=%s&Outcome=%s&PORound=%s&PaceAdjust=%s&PerMode=%s&Period=%s&PlayerID=%s&PlusMinus=%s&Rank=%s&Season=%s&SeasonSegment=%s&SeasonType=%s&ShotClockRange=%s&VsConference=%s&VsDivision=%s' % (
      date_from,
      date_to,
      game_segment,
      last_n_games,
      league_id,
      location,
      measure_type,
      month,
      opponent_team_id,
      outcome,
      po_round,
      pace_adjust,
      per_mode,
      period,
      player_id,
      plus_minus,
      rank,
      season,
      season_segment,
      season_type,
      ShotClockRange,
      vs_conference,
      vs_division)
    resp = requests.get(stats_url)
    if resp.status_code == 200:
        return resp.json()
    else:
        raise Exception(resp.text)


print get_player_stats()