'''arvin's solution'''

coins = [ 200, 100, 50, 20, 10, 5, 2, 1 ]

def foo (rest, i = 0):
    if i == len (coins) - 1:
        return rest % coins[i] == 0
    else:
        return sum (foo (rest - j*coins[i], i + 1)
                    for j in range (int(rest / coins[i]) + 1))

print(foo (200))

#wow! That's fast.
