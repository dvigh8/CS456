import itertools
import operator



def most_common(L):
    groups = itertools.groupby(sorted(L))
    def _auxfun((item, iterable)):
        return len(list(iterable)), -L.index(item)
    return max(groups, key=_auxfun)[0]
    
f = open('a2.cipher.txt')
z = open('pub.keys.txt')
l = list(z)
a = []
a.append(int(l[0]))
a.append(int(l[1]))
values = [];
values = list(f)
numbers = []
for x in values:
    numbers.append(int(x))
#print len(numbers)
asci = [] 
vals = []
for i in range(128):
    asci.append(chr(i))
    vals.append(pow(i,a[1],a[0]))

message = ''
for x in numbers:
    message += asci[vals.index(x)]
    
w = open('a2decrypted.txt', 'w')
w.write(message);


print message