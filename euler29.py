'''Problem 29 Distinct Powers'''

#one-line solution by godspiral:

#print(len(set([i**j for i in range(2,101) for j in range(2,101)])))

#my solution (9183):

p = []

for a in range(2,101):
    for b in range(2,101):
        c = a**b
        if c not in p:
            p.append(c)

print(len(p))
