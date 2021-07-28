# https://www.hackerrank.com/challenges/minimum-distances/problem

def minimumDistances(a):
    # Write your code here
    array_dic = {}
    for i in range(len(a)):
        if a[i] not in array_dic:
            temp_array = []
            temp_array.append(i)
            array_dic[a[i]] = temp_array
        else:
            l = array_dic[a[i]]
            l.append(i)
            array_dic[a[i]] = l
    # discard element from the dic if its length of value is equal to 1
    clean_dic = {k:v for k, v in array_dic.items() if len(v) != 1}
    min_distance = 1000000
    for v in clean_dic.values():
        value = v[-1] - v[-2]
        if (value < min_distance):
            min_distance = value
    if len(clean_dic) == 0:
        return -1
    return min_distance