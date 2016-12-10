import sys
import math
import os
import random


p_length = int(raw_input('prime bit length: '))
print p_length



def gen_num(length):
	num = '1'
	for i in range(2,length):
		num = num + str(int(math.floor(random.random() * 2)))
	
	return int(num + '1',2)

mr_rounds = 1000 # number tests

def mr(n):
	assert n >= 2
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	b = 0
	d = n-1
	while True:
		quo, rem = divmod(d, 2)
		if rem == 1:
			break
		b += 1
		d = quo
	assert(2**b * d == n-1)
	def is_composite(a):
		if pow(a, d, n) == 1:
			return False
		for i in range(b):
			if pow(a, 2**i * d, n) == n-1:
				return False
		return True 
	for i in range(mr_rounds):
		print i
		a = random.randrange(2, n)
		if is_composite(a):
			return False
	return True

def get_prime():
	num = gen_num(p_length)
	while mr(num) != True:
		num = gen_num(p_length)
	return num
p = get_prime()
q = get_prime()
if p < q:
	temp = p
	p = q
	q = temp
n = p*q
phi = (p-1)*(q-1)
print 'p is: ' + str(p)
print 'q is: ' + str(q)
print 'n is: ' + str(n)
print 'phi is: ' + str(phi)


	
