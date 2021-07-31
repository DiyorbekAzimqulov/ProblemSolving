# https://www.hackerrank.com/challenges/service-lane/problem
def serviceLane(n, cases, width):
    # Write your code here
    int_array = []
    for case in cases:
        sub_array = width[case[0]-1: case[1]+1]
        int_array.append(min(sub_array))
    return int_array