import math
import cmath
import numpy as np

def a2_1(points_xy,n):
	sum1 = 0.0
	for i in range(0,n):
		sum1 = sum1 + points_xy[i][0]*points_xy[(i+1)%n][1] - points_xy[(i+1)%n][0]*points_xy[i][1]
	return math.fabs(sum1/2)

def a2_2(points_xy,n):
	sum1 = 0.0
	for i in range(0,n):
		sum1 +=  math.hypot(points_xy[i][0]-points_xy[(i+1)%n][0],points_xy[i][1]-points_xy[(i+1)%n][1])
	return sum1

def a2_3(points_xy,n):
	farea = a2_1(points_xy,n)
	cx,cy,sum1 = 0,0,0
	for i in range(0,n):
		cx += (points_xy[i][0]+points_xy[(i+1)%n][0])*(points_xy[i][0]*points_xy[(i+1)%n][1] - points_xy[(i+1)%n][0]*points_xy[i][1])
		cy += (points_xy[i][1]+points_xy[(i+1)%n][1])*(points_xy[i][0]*points_xy[(i+1)%n][1] - points_xy[(i+1)%n][0]*points_xy[i][1])
	cx /= 6*farea
	cy /= 6*farea

	for i in range(0,n):
		sum1 += math.hypot(points_xy[i][0]-cx,points_xy[i][1]-cy)
	return sum1/n

def a2_4(points_xy,n):
	farea = a2_1(points_xy,n)
	mean = a2_3(points_xy,n)
	cx,cy,sum1 = 0,0,0
	for i in range(0,n):
		cx += (points_xy[i][0]+points_xy[(i+1)%n][0])*(points_xy[i][0]*points_xy[(i+1)%n][1] - points_xy[(i+1)%n][0]*points_xy[i][1])
		cy += (points_xy[i][1]+points_xy[(i+1)%n][1])*(points_xy[i][0]*points_xy[(i+1)%n][1] - points_xy[(i+1)%n][0]*points_xy[i][1])
	cx /= 6*farea
	cy /= 6*farea

	for i in range(0,n):
		sum1 += math.pow(math.hypot(points_xy[i][0]-cx,points_xy[i][1]-cy) - mean , 2)
	return math.sqrt(sum1/(n-1))

def a2_5(points_xy,n):
	T = a2_2(points_xy,n)
	v_cp = np.zeros((n,1),dtype=np.complex)
	delv = np.zeros((n,1),dtype=np.complex)
	normv = np.zeros((n,1),dtype=np.float)
	ph = np.zeros((n,1),dtype=np.float)
	dels = np.zeros((n,1),dtype=np.complex)
	c = np.zeros((201,1),dtype=np.complex)
	t = np.zeros((n,1),dtype=np.float)
	x = np.zeros((201,1),dtype=np.complex)
	b = 1+1j
	for i in range(0,n):
		v_cp[i] = points_xy[i][0] + 1j*points_xy[i][1]
	for i in range(0,n):
		delv[i] = v_cp[(i+1)%n] - v_cp[i]
		temp = delv[i]
		r = math.hypot(temp.real,temp.imag)
		normv[i] = r
		dels[i] = delv[i]/normv[i]
		if i == 0:
			t[0]=0
		else:
			for j in range(0,i):
				t[i] += normv[j]
		
	i = 0
	for i in range(0,201):
		if i == 100:
			for j in range(0,n):
				c[i] = (v_cp[j]+v_cp[j])*normv[j]
			c[i] = c[i]/(2*T)
		else:
			for k in range(0,n):
				a = -3.142*2*t[k]*3.142/T
				fhg = cmath.exp(a)
				c[i] = (dels[(k+1)%n]+dels[k])*fhg
			c[i] = c[i]*T/math.pow(3.142*(i-100)*2,2)
	for i in range(0,201):
		nci = math.hypot(c[i].real,c[i].imag)
		nc1 = math.hypot(c[101].real,c[101].imag)
		phin = math.atan2(c[i].imag,c[i].real)
		phi1 = math.atan2(c[1].imag,c[1].real)
		phi2 = math.atan2(c[1].imag,c[2].real)
		a = (phin+(1-i-100)*phi2-(2-i-100)*phi1)
		x[i] = (nci/nc1)*cmath.exp(1j*a)
	ncn1 = nc1 = math.hypot(c[99].real,c[99].imag)
	fMa = ncn1+nc1;
	fMi = math.fabs(ncn1-nc1)

	return (x.real,fMa,fMi)

def a2_8(points_xy,n):
	xbar = 0
	ybar = 0
	mu = np.zeros((4,4),dtype=np.float)
	nu = np.zeros((4,4),dtype=np.float)
	p = np.zeros((7,1),dtype=np.float)
	for i in range(0,n):
		xbar += points_xy[i][0]
		ybar += points_xy[i][1]
	xbar /= n
	ybar /= n
	mu00 = n*n

	for i in range(0,4):
		for j in range(0,4):
			for k in range(0,n):
				for l in range(0,n):
					mu[i][j] += math.pow((points_xy[k][0]-xbar),i)*math.pow((points_xy[l][1]-ybar),j)
	for i in range(0,4):
		for j in range(0,4):
			gamma = (i+j)/2+1
			nu[i][j] = mu[i][j]/math.pow(mu00,gamma)
	p[0] = nu[2][0]+nu[0][2]
	p[1] = math.pow((nu[2][0]-nu[0][2]),2)+4*nu[1][1]*nu[1][1]
	p[2] = math.pow((nu[3][0]-3*nu[1][2]),2)+math.pow((3*nu[2][1]-nu[0][3]),2)
	p[3] = math.pow((nu[3][0]+nu[1][2]),2)+math.pow((nu[2][1]+nu[0][3]),2)
	p[4] = (nu[3][0]-3*nu[1][2])*(nu[3][0]+nu[1][2])*(math.pow((nu[3][0]+nu[1][2]),2)-math.pow((nu[2][1]+nu[0][3]),2))+(3*nu[2][1]-nu[0][3])*(nu[2][1]+nu[0][3])*(math.pow((nu[3][0]+nu[1][2]),2)-math.pow((nu[2][1]+nu[0][3]),2))
	p[5] = (nu[2][0]-nu[2][0])*(math.pow((nu[3][0]+nu[1][2]),2)-3*math.pow((nu[2][1]+nu[0][3]),2))+4*nu[1][1]*(nu[3][0]+nu[1][2])*nu[1][1]*(nu[0][3]+nu[2][1])
	p[6] = (3*nu[2][1]-nu[3][0])*(nu[3][0]-nu[1][2])*(math.pow((nu[3][0]-nu[1][2]),2)-3*math.pow((nu[2][1]+nu[0][3]),2))+(3*nu[1][2]-nu[3][0])*(nu[2][1]+nu[0][3])*(3*math.pow((nu[3][0]+nu[1][2]),2)-math.pow((nu[2][1]+nu[0][3]),2))

	return p




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
					x = distance*math.cos(angle)
					y = distance*math.sin(angle)
					points.append([x,y])
				

				print len(a2_5(points,len(points)));