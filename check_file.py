import os, sys

def check_file(f1, f2):
	return list(f1.read()) == list(f2.read())

def check(A):
	out = A + "_io/output"
	cout = A + "_io/cur_output"
	c = 0
	w = 0
	for i in range(100):
		tout = out + str(i) + ".txt"
		tcout = cout + str(i) + ".txt"
		if os.path.exists(tout):
			f1 = open(tout, "r")
			f2 = open(tcout, "r")
			if check_file(f1, f2):
				c += 1
			else:
				w += 1
		else:
			break
	if w == 0:
		os.system("echo all ok")
	else:
		os.system("echo correct " + str(c) + " out of " + str(c+w))

if __name__ == '__main__':
	A = sys.argv[1:][0]
	# A = "A"
	check(A)
