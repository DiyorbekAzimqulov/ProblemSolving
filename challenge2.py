ENDPOINT_COMPETITION = "https://jsonmock.hackerrank.com/api/football_competitions"
ENDPOINT_MATCHES = "https://jsonmock.hackerrank.com/api/football_matches"
import requests


def getWinnerTotalGoals(competition, year):
    params_competition = {
        'name': competition,
        'year': year
    }
    response = requests.get(url=ENDPOINT_COMPETITION, params=params_competition)
    winner = response.json()['data'][0]['winner']



    total_goals = 0
    host_goals = 0
    guest_goals = 0
    params_matches = {
    'year': year,
    'competition': competition,
    f'team1': winner
    }
    response = requests.get(url=ENDPOINT_MATCHES, params=params_matches).json()
    num_request = response['total_pages']
    for i in range(num_request):
        
        params_matches = {
            'year': year,
            'competition': competition,
            'team1': winner,
            'page': i+1
        }

        response = requests.get(url=ENDPOINT_MATCHES, params=params_matches).json()
        for d in response['data']:
            host_goals += int(d[f'team1goals'])
    # guest
    params_matches = {
    'year': year,
    'competition': competition,
    f'team2': winner
    }
    response = requests.get(url=ENDPOINT_MATCHES, params=params_matches).json()
    num_request = response['total_pages']
    for i in range(num_request):
        
        params_matches = {
            'year': year,
            'competition': competition,
            'team2': winner,
            'page': i+1
        }

        response = requests.get(url=ENDPOINT_MATCHES, params=params_matches).json()
        for d in response['data']:
            guest_goals += int(d[f'team2goals'])
    return host_goals + guest_goals
print(getWinnerTotalGoals(competition='UEFA Champions League', year=2011))