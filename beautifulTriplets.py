# https://www.hackerrank.com/challenges/beautiful-triplets/problem?h_r=next-challenge&h_v=zen

def beautifulTriplets(arr, d):
    triplets = []
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)):
            if(arr[j]-arr[i] == d):
                if (j+1 < len(arr)):
                    for k in range(j+1, len(arr)): 
                        if (arr[k] - arr[j] == d):
                            triplets.append([i, j, k])
                            break
    return len(triplets)
arr = list(range(10000))
d = 10
print(beautifulTriplets(arr, d))
    