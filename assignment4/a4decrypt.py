import math
import sys

f = open('a4.cipher.txt')


p = 12399363407314802534894337901181367912365390278953001273409754922038825316283282383095029550773749866734231576917322906183500383575332035336227711526925327
A = 12079055304900077881496017093520705553618624248737774318027533001099811953633763825284638741718719990914320606147780023938639362506662800193686221296264344

N = 3
xp = 0
yp = 1
values = [];
values = list(f)

cipher = []
for x in values:
    points = []
    for j in str.split(x):
        points.append(int(j))
    cipher.append(points)
    

#first find full mask by F = N * H = 3H = 2H + H

def full_mask(H):
    #    return = point_double(point_double(H)) # since N = 4
    return point_add(H, point_double(H)) # since N = 3

def point_double(P):
    m = (((3 * (P[xp]**2)) + A) * (inverse((2 * P[yp]) % p))) % p
    x = (m**2 - (2 * P[xp])) % p
    y = (P[yp] + m * (x - P[xp])) % p
    y = -y % p
    return [int(x), int(y)]
    
def point_add(P, Q):
    m = ((Q[yp]-P[yp]) * inverse((Q[xp]-P[xp]) % p)) % p
    x = (m**2 - (P[xp] + Q[xp])) % p
    y = (P[yp] + m * (x - P[xp])) % p
    y = -y % p
    return [int(x), int(y)]
    
def inverse(e):
    x1 = 1
    y1 = 0
    x2 = 0
    y2 = 1
    one = p
    two = e
    q = math.floor(one/two)
    r = one % two
    while(two !=1):
        tmp1 = x2
        tmp2 = y2
        x2 = x1 - (q * x2)
        y2 = y1 - (q * y2)
        x1 = tmp1
        y1 = tmp2
        one = two
        two = r
        q = one/two
        r = one % two
    return int(y2 % p)

def decrypt(C, F):
    F[yp] = -F[yp] % p
    return point_add(C, F)

def full_decrypt(C, H):
    
#    F = point_double(point_double(H)) # since N = 4
    F = point_add(H, point_double(H)) # since N = 3
    return decrypt(C, F)
    
z = open('a4partdecrypt.txt', 'w')
for first in cipher:
    C = [first[0],first[1]]
    H = [first[2],first[3]]
    M = full_decrypt(C,H)
    z.write(str(M[0]) + ' ' + str(M[1]) + '\n')

    