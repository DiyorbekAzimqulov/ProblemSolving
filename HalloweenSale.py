# https://www.hackerrank.com/challenges/halloween-sale/problem?h_r=next-challenge&h_v=zen
def howManyGames(p, d, m, s):
    number_of_games = 0
    current_cost = p
    budget = s
    discount = d
    min_price = m
    while(budget >= current_cost):
        budget -= current_cost
        number_of_games += 1
        current_cost -= discount
        if current_cost < min_price:
            current_cost = min_price
    return number_of_games
