import math

th = 1
th_gap = 1
th_rgap = 1
def max_len(points,n):
	max = 0
	for i in range(0,n):
		if max<points[i][0]:
			max = points[i][0]
	return max
def minima(d1,d2,d3):
	if d2<d1 and d2<d3:
		return 1
	else:
		return 0

def a1_1(points,n):
	sum1 = 0.0
	for i in range(0,n):
		sum1 += math.fabs(points[i][0]-points[(i+1)%n][0])
	return sum1/n

def a1_2(points,n):
	sum1 = 0.0
	mean = a1_1(points,n)
	for i in range(0,n):
		sum1 += math.pow(math.fabs(points[i][0]-points[(i+1)%n][0]) - mean , 2)
	return math.sqrt(sum1/(n-1))

def a1_3(points,n):
	sum1 = 0.0
	for i in range(0,n):
		if points[i][0] < th:
			dist = points[i][0]
		else:
			dist = th
		if points[(i+1)%n][0] < th:
			dist_n = points[(i+1)%n][0]
		else:
			dist_n = th
		sum1 += math.fabs(dist-dist_n)
	return sum1/n

def a1_4(points,n):
	sum1 = 0.0
	mean = a1_3(points,n)
	for i in range(0,n):
		if points[i][0] < th:
			dist = points[i][0]
		else:
			dist = th
		if points[(i+1)%n][0] < th:
			dist_n = points[(i+1)%n][0]
		else:
			dist_n = th
		sum1 += math.pow(math.fabs(dist-dist_n) - mean , 2)
	return math.sqrt(sum1/(n-1))

def a1_5(points,n):
	sum1 = 0.0
	for i in range(0,n):
		sum1 += points[i][0]
	return sum1/n

def a1_6(points,n):
	sum1 = 0.0
	mean = a1_5(points,n)
	for i in range(0,n):
		sum1 += math.pow(points[i][0] - mean , 2)
	return math.sqrt(sum1/(n-1))

def a1_7(points,n):
	sum1 = 0.0
	for i in range(0,n):
		if math.fabs(points[i][0]-points[(i+1)%n][0]) < th_gap:
			dist = 0
		else:
			dist = 1
		sum1 += dist
	return sum1/n

def a1_9_10(points,n):
	min1,min2,mind1,mind2 = 0,0,max_len(points,n),max_len(points,n)
	temp = 0
	for i in range(0,n):
		d1 = points[(n+i-1)%n][0]
		d2 = points[i][0]
		d3 = points[(i+1)%n][0]
		if minima(d1,d2,d3):
			if d2 < mind2:
				mind2 = d2
				min2 = i
			if mind2<mind1:
				temp = mind1
				mind1 = mind2
				mind2 = temp
				temp = min1
				min1 = min2
				min2 = temp
	f = [math.hypot(points[min1][0]*math.cos(points[min1][1])-points[min2][0]*math.cos(points[min2][1]),points[min1][0]*math.sin(points[min1][1])-points[min2][0]*math.sin(points[min2][1])),1]
	f[1] = math.fabs(points[min1][1]-points[min2][1])
	return f

def a1_11(points,n):
	sum1 = 0.0
	for i in range(0,n):
		sum1 += math.fabs(points[i][0]/points[(i+1)%n][0])
	return sum1/n

def a1_12(points,n):
	sum1 = 0.0
	mean = a1_11(points,n)
	for i in range(0,n):
		sum1 += math.pow(math.fabs(points[i][0]/points[(i+1)%n][0]) - mean , 2)
	return math.sqrt(sum1/(n-1))

def a1_13(points,n):
	sum1 = 0.0
	d_max = max_len(points,n)
	for i in range(0,n):
		sum1 += math.fabs(points[i][0]/d_max)
	return sum1/n

def a1_14(points,n):
	sum1 = 0.0
	d_max = max_len(points,n)
	mean = a1_13(points,n)
	for i in range(0,n):
		sum1 += math.pow(math.fabs(points[i][0]/d_max) - mean , 2)
	return math.sqrt(sum1/(n-1))

def a1_15(points,n):	
	sum1 = 0.0
	for i in range(0,n):
		if math.fabs(points[i][0]/points[(i+1)%n][0]) < th_rgap:
			dist = 0
		else:
			dist = 1
		sum1 += dist
	return sum1/n

def a1_16(points,n):
	fd = a1_5(points,n)
	fsigma = a1_6(points,n)
	sum1 = 0.0
	for i in range(0,n):
		sum1 += math.pow(points[i][0]-fd,4)
	return (sum1/(n*math.pow(fsigma,4)))-3


if __name__ == '__main__':
	with open('../room1') as f:
		for line in f:
			points = [] ##It is a 2d array
			if line[0] != 'H':
				parts = line.split('(')
				for i in range(1,len(parts)):
					value = parts[i].split(' , ')
					angle = value[0]
					angle = float(angle) 
					useless = value[1].split(' )')
					distance = float(useless[0])
					points.append([distance,angle])
				

				print a1_16( points,len(points));