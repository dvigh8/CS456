import sys
import math
import os
import random

p_length = int(raw_input('prime bit length: '))

def gen_num(length):
	num = '1'
	for i in range(2,length):
		num = num + str(int(math.floor(random.random() * 2)))
	return int(num + '1',2)

def mr(n):
	assert n >= 2
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	r = 0
	d = n-1
	while True:
		quo, rem = divmod(d, 2)
		if rem == 1:
			break
		r += 1
		d = quo
	assert(2**r * d == n-1)
	def is_composite(a):
		if pow(a, d, n) == 1:
			return False
		for i in range(r):
			if pow(a, 2**i * d, n) == n-1:
				return False
		return True 
	for i in range(100):
		a = random.randrange(2, n)
		if is_composite(a):
			return False
	return True

def plv(one, two):
	quo, rem = divmod(one,two) 
	x1 = 1
	y1 = 0
	x2 = 0
	y2 = 1
	while(two !=1):
		tmp1 = x2
		tmp2 = y2
		x2 = x1 - (quo * x2)
		y2 = y1 - (quo * y2)
		x1 = tmp1
		y1 = tmp2
		one = two
		two = rem
		quo, rem = divmod(one,two) 
	return long(y2 % p)

def get_prime():
	num = gen_num(p_length)
	while mr(num) != True:
		num = gen_num(p_length)
	return num
p = get_prime()
q = get_prime()
e = gen_num(p_length/2)
while p == q:
	q = get_prime()
if p < q:
	temp = p
	p = q
	q = temp
while pow(p,1,e) == 1 or pow(q,1,e) == 1:
	e = gen_num(p_length/2)
n = p*q
phi = (p-1)*(q-1)
d = plv(phi,e);

z = open('keys.txt', 'w')
z.write(str(p) + '\n') 
z.write(str(q) + '\n') 
z.write(str(n) + '\n') 
z.write(str(e) + '\n') 
z.write(str(d) + '\n') 
z.write(str(phi) + '\n') 
z.close()

message = raw_input('what is your message: ')
m = open('message.txt','w')
for i in range(len(message)):
	print ord(message[i])
#	m.write(pow(ord(i),e,n))
print message[2]
