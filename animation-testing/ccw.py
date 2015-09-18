
ERR = 0.0000001
# floating-point comparison
def approx_equal(x1, x2, err):
	return abs(x1 - x2) < err

def pts_equal(A, B):
	return approx_equal(A[0], B[0], ERR) and approx_equal(A[1], B[1], ERR)

# true if b > a > c or c < a < b
def is_middle(a, b, c):
	return (c > a and a > b) or (b > a and a > c)

def is_ri(A, B, C):
	if not (is_middle(A[0], B[0], C[0]) or (approx_equal(A[0], B[0], ERR) or approx_equal(A[0], C[0], ERR))):
		return False	
	if not (is_middle(A[1], B[1], C[1]) or (approx_equal(A[1], B[1], ERR) or approx_equal(A[1], C[1], ERR))) :
		return False
	if approx_equal(C[0]-B[0], 0, ERR) and approx_equal(A[0]-B[0], 0, ERR):
		return True
	elif approx_equal(C[0]-B[0], 0, ERR) or approx_equal(A[0]-B[0], 0, ERR):
		return False
	slope_1 = float(C[1]-B[1])/(C[0]-B[0])
	slope_2 = float(A[1]-B[1])/(A[0]-B[0])
	if approx_equal(slope_1, slope_2, ERR):
		return True
	return False
	
# checks if point A is in the closure of BC, given that det=0
def is_cl(A, B, C):
	# since det=0, only need to check one value
	if pts_equal(A,B):
		return True
	if pts_equal(A,C):
		return True
	if is_ri(A, B, C):
		return True
	return False

# A, B, C are tuples of (x, y) form
def ccw(A, B, C):
	if pts_equal(A, B):
		if pts_equal(A, C):
			return 0
		else:
			return 2
	# compute signed determinant; cross product (B-A)x(C-A)
	d = (B[0]-A[0])*(C[1]-A[1])-(B[1]-A[1])*(C[0]-A[0])
	if d > 0:
		return -1
	elif d < 0:
		return 1
	else:
		if is_cl(C, A, B):
			return 0
		elif is_ri(B, A, C):
			return 2
		# then A lies in relative interior of BC
		else:
			return -2

# determines if two line segments intersect
# s1 and s2 are tuples of the form ((x1, y1), (x2, y2))
def intersect(s1, s2):
	i = ccw(s1[0], s1[1], s2[0])
	j = ccw(s1[0], s1[1], s2[1])
	i_1 = ccw(s2[0], s2[1], s1[0])
	j_1 = ccw(s2[0], s2[1], s1[1])
	# intersection pt is in closure of both segments
	if (i+j==0) and (i_1+j_1==0):
		return True
	# endpt of s2 lies in closure of s1
	elif (i==0 or j==0) or (i_1==0 or j_1==0):
		return True
	else:
		return False
