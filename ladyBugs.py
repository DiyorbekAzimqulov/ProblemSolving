# https://www.hackerrank.com/challenges/happy-ladybugs/problem
def happyLadybugs(b):
    # check if there is an empty cell
    for a in set(b):
        if a != "_" and b.count(a) == 1:
            return "NO"
    
    if b.count("_") == 0:
        for i in range(1,len(b)-1):
            if b[i-1]!=b[i] and b[i+1]!=b[i]:
                return "NO"
    return "YES"

# -----------Solution explained---------------
# if there is no empty cell in dashboard and letter appears once in dashboard so there is no happy bug
# else if there is no empty cell in dashboard and letter in adjacent cells do not the same, there is no happy bug
# otherwise there is one.