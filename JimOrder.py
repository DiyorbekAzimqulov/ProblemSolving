# https://www.hackerrank.com/challenges/jim-and-the-orders/problem
def jimOrders(orders):
    # Write your code here
    result = []
    serve_time = []
    
    for order in orders:
        serve_time.append(order[0] + order[1])
    times = []
    for i in sorted(serve_time):
        if i not in times:
            times.append(i)
    
    for time in times:
        index = 1
        for order in orders:
            if time == order[0] + order[1]:
                result.append(index)
            index += 1
    return result