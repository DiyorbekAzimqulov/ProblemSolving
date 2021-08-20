# https://www.hackerrank.com/challenges/strange-code/problem?h_r=next-challenge&h_v=zen

# import datetime
# def binary_search(arr, low, high, x):
 
#     # Check base case
#     if high >= low:
 
#         mid = (high + low) // 2
 
#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid
 
#         # If element is smaller than mid, then it can only
#         # be present in left subarray
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid - 1, x)
 
#         # Else the element can only be present in right subarray
#         else:
#             return binary_search(arr, mid + 1, high, x)
 
#     else:
#         # Element is not present in the array
#         return -1

# # def strangeCounter(t):
# #     # Write your code here
# #     last_big = 3
# #     degree = 0
# #     data = {1: 3, 2: 2, 3: 1}
# #     while(last_big < t):
# #         keys = list(range(3*(2**degree) - 2, 2*(3*2**degree) - 3))
# #         values = list(reversed(range(1, 3*(2**degree)+1)))
# #         last_big = keys[-1]
# #         degree += 1 
# #     if t > 3:
# #         index = binary_search(keys, 0, len(keys)-1, t)
# #         return values[index]
# #     return data[t]
# # def strangeCounter1(t):
# #     # Write your code here
# #     last_big = 3
# #     degree = 0
# #     data = {1: 3, 2: 2, 3: 1}
# #     while(last_big < t):
# #         start_key = 
# #         end_key = 2*(3*2**degree) - 3
# #         keys = list(range(start_key, end_key+1))
# #         start_value = 3*(2**degree)
# #         values = list(reversed(range(1, start_value+1)))
# #         last_big = keys[-1]
# #         data = dict(zip(keys, values))
# #         degree += 1 
# #     return data[t]
# def linear_search(arr, val):
#     ctr = 0
#     for i in arr:
#         if val == i:
#             return ctr
#         ctr += 1

# def strangeCounter(t):
#     degree = 0
#     l = list(range(3*(2**degree) - 2, 2*(3*2**degree) - 2))
#     while(t not in l):
#         l = list(range(3*(2**degree) - 2, 2*(3*2**degree) - 2))
#         degree += 1
#     index = binary_search(l, 0, len(l)-1, t)
#     degree -= 1
#     values = list(reversed(range(1, (3*2**degree)+1)))
#     return values[index]
# t = 100000000
# l = strangeCounter(t)
# start_time = datetime.datetime.now()
# # print(binary_search(l, 0, len(l)-1, t))
# print(linear_search(l, t))
# end_time = datetime.datetime.now()
# print(end_time-start_time)

def strangeCounter(t):
    n=3
    while 2*n-2<=t:
        n*=2
    return n-(t-(n-2))
print(strangeCounter(100))