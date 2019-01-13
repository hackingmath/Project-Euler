'''Arn zrn's solution of prob 31'''

def nway( total, coins):
    if not coins: return 0
    c, coins = coins[0], coins[1:]
    count = 0 
    if total % c == 0: count += 1    
    for amount in range( 0, total, c):
        count += nway(total - amount, coins)    
    return count
# main
print(nway( 200, (1,2,5,10,20,50,100,200)))
