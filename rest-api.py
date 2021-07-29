import requests
ENDPOINT = "https://jsonmock.hackerrank.com/api/football_matches"
def getNumDraws(year):
    draws = 0
    for goal in range(0,11):
        params = {
            'year': year,
            'team1goals': goal,
            'team2goals': goal,
            'page': 2
        }
        response = requests.get(url=ENDPOINT, params=params).json()
        draws += response['total']
    return draws

print(getNumDraws(year=2011))