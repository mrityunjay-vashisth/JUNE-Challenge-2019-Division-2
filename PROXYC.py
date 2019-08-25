import math

n = input()
for i in range(n):
	d = input()
	k = raw_input()

	req = int(math.floor(d*.25))

	absent = 0
	for i in range(d):
		if k[i] == 'A':
			absent += 1
 
 	proxy = 0
 	found = 0
 	for i in range(2, d - 2, 1):
 		if absent <= req:
 			found = 1
 			break
 		if k[i] == 'A':
 			if k[i - 1] == 'P' or k[i - 2] == 'P':
 				if k[i + 1] == 'P' or k[i + 2] == 'P':
 					absent = absent - 1
 					proxy = proxy + 1
 					if absent <= req:
 						found = 1
 						break
 	if found:
 		print proxy
 	else:
 		print -1