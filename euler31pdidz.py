target = 20
cs = [1,2,5,10,20,50,100,200]
ways = [1] + target*[0]

for coin in cs :
    for i in range(coin, target+1):
        print("coin:",coin,"i:",i)
        ways[i] += ways[i-coin] #this is brilliant! Why does it work???
        print(ways)
print (ways[target], " ways")

#almost instantaneous!
