# https://www.hackerrank.com/challenges/mars-exploration/problem?h_r=next-challenge&h_v=zen
def marsExploration(s):
    # Write your code here
    transit = 0
    for i in range(len(s)):
        if i % 3 == 0 and s[i] == "S":
            continue
        elif i % 3 == 1 and s[i] == "O":
            continue
        elif i % 3 == 2 and s[i] == "S":
            continue
        else:
            transit += 1
    return transit

print(marsExploration("SOSSOSSOS"))