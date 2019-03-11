'''Euler 2'''

def fibo(n):
    '''generates list of fibonacci numbers
    up to n'''
    fs = [1,1]
    running_sum = 0
    while True:
        #generate the next fibo
        next_f = fs[-1] + fs[-2]
        #if it's more than n
        if next_f >= n:
            break
        #add to fibo list
        fs.append(next_f)
        #if it's even, add to sum
        if next_f % 2 == 0:
            running_sum += next_f
    return running_sum
    
