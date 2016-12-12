import sys
import math
import os
import random

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

def plv(one, two, n):
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
	return long(y2 % n)

def gcd(x, y):
	while y != 0:
		(x, y) = (y, x % y)
	return x
	
def get_prime(p_length):
	num = gen_num(p_length)
	while mr(num) != True:
		num = gen_num(p_length)
	return num

def key_gen():
	p_length = int(raw_input('prime bit length: '))

	p = get_prime(p_length)
	q = get_prime(p_length)
	e = gen_num(p_length/2)
	while p == q:
		q = get_prime(p_length)
	if p < q:
		temp = p
		p = q
		q = temp
	n = p*q
	phi = (p-1)*(q-1)
	while gcd(phi,e) != 1:
		e = gen_num(p_length/2)
	d = plv(phi, e, n);
	while (d*e % phi) != 1:
		e = gen_num(p_length/2)
		while gcd(phi,e) != 1:
			e = gen_num(p_length/2)
		d = plv(phi, e, n);
	return n, e, d

#ans = raw_input('encrypt(e) decrypt (d): ')
#if ans == 'e':
#ans = raw_input('use keys(k) gen keys(g) ')
#if ans == 'g':
#	print ' d*e % phi  = ' + str(d*e % phi)
#
#	z = open('public.keys.txt', 'w')
#	z.write(str(n) + '\n') 
#	z.write(str(e) + '\n') 
#	z.close()
#	z = open('private.keys.txt', 'w')
#	z.write(str(p) + '\n') 
#	z.write(str(q) + '\n') 
#	z.write(str(phi) + '\n') 
#	z.write(str(d) + '\n') 
#	z.write(str(n) + '\n') 
#	z.close()
#else:
#	f = open('public.keys.txt')
#	l = list(f)
#	n = int(l[0])
#	e = int(l[1])
#	f.close()
#ans = raw_input('from file (f) enter message (e) ')
#if ans == 'f': 
#	file_name = raw_input('input file name: ')
#	f = open(file_name)
#	l = list(f)
#	f.close()
#	message = ''
#	for i in range(len(l)):
#		message += l[i]
#else:
#	message = raw_input('what is your message: ')
#file_name = raw_input('output file name: ')
#m = open(file_name,'w')
#for i in range(len(message)):
#	m.write(str(pow(ord(message[i]),e,n)) + '\n')
#m.close()
#elif ans == 'd':
#f = open('private.keys.txt')
#l = list(f)
#p = int(l[0])
#q = int(l[1])
#phi = int(l[2])
#d = int(l[3])
#n = int(l[4])
#f.close()
#file_name = raw_input('input file name: ')
#f = open(file_name)
#l = list(f)
#f.close()
#text = ''
#for i in range(len(l)):
#	text += chr(pow(int(l[i]),d,n))
#print text