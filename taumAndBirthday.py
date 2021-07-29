# https://www.hackerrank.com/challenges/taum-and-bday/problem
def taumBday(b, w, bc, wc, z):
    max_cost_gift = 0
    min_cost_gift = 0
    if (bc > wc):
        max_cost_gift = bc
        min_cost_gift = wc
    else:
        max_cost_gift = wc
        min_cost_gift = bc
    if max_cost_gift > min_cost_gift + z:
        if min_cost_gift == bc:
            total = (b + w) * bc + w * z
        else:
            total = (b + w) * wc + b * z
    else:
        total = b * bc + w * wc
    return total