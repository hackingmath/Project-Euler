#by begoner on PE forum. doesn't work for me? 'reduce'?

# First load the file and sort it.

'''x = eval( '[' + open( 'names.txt' ).readlines()[ 0 ] + ']' )
x.sort()

# Then calculate what is needed.

reduce( lambda x, y: x + y, [ reduce( lambda x, y: x + y, [ ( j + 1 ) * ( ord( i ) - 64 ) for i in x[ j ] ] ) for j in range( len( x ) ) ] )
'''
#by lassevk on forum. AttributeError: "'map' object has no attribute 'sort'"
#works if I open, read and sort "names"

f = open('names.txt','r') #open the names file
text = f.read()         #read it into text form
names = list(eval(text)) #turn into a list
#print(names[:10])
names.sort()

'''names = map(lambda x: x.strip('"'), open('names.txt').read().strip().split(','))
names.sort()'''
print(sum(sum(map(lambda x: ord(x)-64, names[index])) * (index+1) for index in range(len(names))))
f.close()
