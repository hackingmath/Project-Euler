'''Euler Project Problem 24
Lexicographic permutations
solution in 3.9 s
'''
import time

#there are 3,628,800 permutations of the 10 numerals

def main():
    now = time.time()
    index = 0
    for a in range(10):
        for b in range(10):
            if b != a:
                for c in range(10):
                    if c != a and c != b:
                        for d in range(10):
                            if d != a and d != b and d != c:
                                for e in range(10):
                                    if e not in [a,b,c,d]:
                                        for f in range(10):
                                            if f not in [a,b,c,d,e]:
                                                for g in range(10):
                                                    if g not in [a,b,c,d,e,f]:
                                                        for h in range(10):
                                                            if h not in [a,b,c,d,e,f,g]:
                                                                for i in range(10):
                                                                    if i not in [a,b,c,d,e,f,g,h]:
                                                                        for j in range(10):
                                                                            if j not in [a,b,c,d,e,f,g,h,i]:
                                                                                index += 1
                                                                                if index == 1000000:
                                                                                    print(int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)))
                                                                                    then = time.time()
                                                                                    elapsed = then - now
                                                                                    print(elapsed)
                                                                                    return
                                                                                    
                                                            
main()            

