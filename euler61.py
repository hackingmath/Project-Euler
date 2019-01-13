'''Problem 61
Cyclical Figurate numbers'''

def triangle():
    '''Generates a list of 4-digit triangular numbers.'''
    tris = [str(int((n+1)*n/2)) for n in range(40,150)]
    tris = [tri for tri in tris if len(tri) == 4]
    return tris

def squares():
    '''Generates a list of 4-digit square numbers.'''
    squares = [str(n**2) for n in range(100)]
    squares = [square for square in squares if len(square) == 4]
    return squares

def pents():
    '''Generates a list of 4-digit pentagonal numbers.'''
    pent = [str(int((3*n-1)*n/2)) for n in range(100)]
    pent = [p for p in pent if len(p) == 4]
    return pent

def hexnums():
    '''Generates a list of 4-digit hexagonal numbers.'''
    hexes = [str(int((2*n-1)*n)) for n in range(100)]
    hexes = [h for h in hexes if len(h) == 4]
    return hexes

def heptnums():
    '''Generates a list of 4-digit pentagonal numbers.'''
    hepts = [str(int((5*n-3)*n/2)) for n in range(100)]
    hepts = [h for h in hepts if len(h) == 4]
    return hepts

def octnums():
    '''Generates a list of 4-digit pentagonal numbers.'''
    octs = [str(int((3*n-2)*n)) for n in range(100)]
    octs = [h for h in octs if len(h) == 4]
    return octs

trinums = triangle() # list of triangular numbers
#sets of beginning two or ending two numbers:
tri_pair = {x[:2]:x[2:] for x in trinums}

squ = squares()
squ_pair = {x[:2]:x[2:] for x in squ}

pentas = pents()
pent_pair = {x[:2]:x[2:] for x in pentas}

hexes = hexnums()
hex_pair = {x[:2]:x[2:] for x in hexes}

hepts = heptnums()
hept_pair = {x[:2]:x[2:] for x in hepts}

octs = octnums()
oct_pair = {x[:2]:x[2:] for x in octs}

dicts = [tri_pair,squ_pair,pent_pair,hex_pair,hept_pair,oct_pair]

def search_dicts(num,level):
    if level == 0:
        return num
    for pair in dicts[level].keys():
        if dicts[level][pair] not in dicts[level-1].keys():
            return False
        search_dicts(dicts[level][pair],level-1)

print(search_dicts('42',5
        

'''print('tris: ',trinums)
print('squares: ',squ)
print('pents: ',pentas)
print('hexes: ',hexes)
print('hepts: ',hepts)
print('octs: ',octs)'''

'''firsts = [tri_first,squ_first,pent_first,hex_first,hept_first,oct_first]
lasts = [tri_last,squ_last,pent_last,hex_last,hept_last,oct_last]

def narrow():
    oct_first_ok = set()
    for p in oct_first:
        for last in [squ_last,tri_last,pent_last,hex_last,hept_last]:
            if p in last:
                oct_first_ok.add(p)
    print(oct_first_ok)

#narrow()

tri_first_ok = {'39', '86', '35', '23', '20', '89',
                '36', '45', '81', '52', '44', '85',
                '53', '14', '43', '59', '50', '67',
                '71', '46', '16', '25', '37', '21',
                '56', '58', '76', '22', '47', '78',
                '26', '40', '64', '11', '95', '65',
                '73', '75', '24', '77', '32', '57',
                '62', '18', '29', '15', '87', '30',
                '31', '51', '70', '80', '12', '91',
                '33', '82', '10', '17', '41', '90',
                '61', '49', '69', '28', '55'}

pent_first_ok = {'15', '75', '67', '77', '71', '59',
                 '84', '55', '28', '50', '95', '61',
                 '20', '21', '51', '43', '17', '69',
                 '41', '14', '12', '23', '10', '35',
                 '53', '31', '65', '26', '46', '88',
                 '18', '73', '11', '25', '81', '45',
                 '86', '30', '37', '40', '16'}

hex_first_ok = {'17', '16', '76', '64', '14', '30',
                '28', '86', '21', '53', '69', '40',
                '49', '89', '33', '41', '78', '36',
                '62', '55', '18', '25', '71', '43',
                '91', '73', '10', '45', '20', '12',
                '11', '51', '47', '57', '59', '22',
                '24', '81', '31', '15'}

hept_first_ok = {'47', '10', '26', '61', '12', '11',
                 '45', '80', '15', '25', '69', '30',
                 '56', '22', '16', '28', '95', '86',
                 '49', '89', '64', '92', '33', '77',
                 '31', '52', '20', '17', '41', '35'}

oct_last_ok = {'47', '77', '15', '80', '52', '16',
               '74', '22', '65', '59', '71', '62',
               '30', '12', '10', '44', '57', '86',
               '36', '24', '14', '32', '49', '89',
               '28', '40', '18', '26', '11', '96',
               '92', '21'}
'''
