import math
import sys

x1 = 1
y1 = 0
x2 = 0
y2 = 1
one = int(sys.argv[1])
two = int(sys.argv[2])
q = math.floor(one/two)
r = one % two
while(two !=1):
	print(str(int(one)).rjust(5)  + ' ' + str(int(two)).rjust(5) + ' ' + str(int(q)).rjust(5) + ' ' + str(int(r)).rjust(5) + ' ' + str(int(x1)).rjust(5) + ' ' + str(int(y1)).rjust(5) + ' ' + str(int(x2)).rjust(5) + ' ' + str(int(y2)).rjust(5))
	
	tmp1 = x2
	tmp2 = y2
	x2 = x1 - (q * x2)
	y2 = y1 - (q * y2)
	x1 = tmp1
	y1 = tmp2
	one = two
	two = r
	q = math.floor(one/two)
	r = one % two
	
print(str(int(one)).rjust(5)  + ' ' + str(int(two)).rjust(5) + ' ' + str(int(q)).rjust(5) + ' ' + str(int(r)).rjust(5) + ' ' + str(int(x1)).rjust(5) + ' ' + str(int(y1)).rjust(5) + ' ' + str(int(x2)).rjust(5) + ' ' + str(int(y2)).rjust(5))

