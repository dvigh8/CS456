import math
import sys

f = open('a4.cipher.txt')
p = 12399363407314802534894337901181367912365390278953001273409754922038825316283282383095029550773749866734231576917322906183500383575332035336227711526925327
A = 12079055304900077881496017093520705553618624248737774318027533001099811953633763825284638741718719990914320606147780023938639362506662800193686221296264344
#p = 163
#A = -22
N = 3
xp = 0
yp = 1
values = [];
values = list(f)

cipher = []
mask = []
for v in values:
    x = v.split(' ')
    cipher.append([long(x[0]),long(x[1])])
    mask.append([long(x[2]),long(x[3])])

def point_double(P):
    m = (((3 * (P[xp]**2)) + A) * (inverse(pow((2 * P[yp]),1,p)))) % p
    x = (pow(m,2) - (2 * P[xp])) % p
    y = (P[yp] + (m * (x - P[xp]))) % p
    y = -y % p
    return [long(x), long(y)]
    
def point_add(P, Q):
    m = ((Q[yp]-P[yp]) * inverse((Q[xp]-P[xp]) % p)) % p
    x = (m**2 - (P[xp] + Q[xp])) % p
    y = (P[yp] + m * (x - P[xp])) % p
    y = -y % p
    return [long(x), long(y)]
    
def inverse(e):
    one = p
    two = e
    q = long(math.floor(one/two))
    r = one % two
    x1 = 1
    y1 = 0
    x2 = 0
    y2 = 1
    while(two !=1):
        tmp1 = x2
        tmp2 = y2
        x2 = x1 - (q * x2)
        y2 = y1 - (q * y2)
        x1 = tmp1
        y1 = tmp2
        one = two
        two = r
        q = long(math.floor(one/two))
        r = one % two
    return long(y2 % p)

def decrypt(C, F):
    F[yp] = -F[yp] % p
    return point_add(C, F)

def full_decrypt(C, H):
    F = point_add(H, point_double(H)) # since N = 3
    return decrypt(C, F)

z = open('a4decrypt.txt', 'w')
text = ''
for i in range(314):
    C = cipher[i]
    H = mask[i]
    M = full_decrypt(C,H)
    text += chr(M[0]);

print text
z.write(text) 

    