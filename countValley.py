# https://www.hackerrank.com/challenges/counting-valleys/problem
def countingValleys(steps, path):
    # Write your code here
    valley = 0
    mountain = 0
    state = 0
    up = 0
    down = 0
    before_present_state = 0
    for step in range(steps):
        if path[step] == 'D':
            down += 1
        elif path[step] == 'U':
            up += 1
        before_present_state = state
        state = up - down
        if(before_present_state > 0 and state == 0):
            mountain += 1
        elif(before_present_state < 0 and state == 0):
            valley += 1
    return valley