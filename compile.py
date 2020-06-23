import sys, os

def run(inp, out):
	fi = open(inp, "r")
	fo = open(out, "w")
	os.system("./a.out < " + inp + " > " + out)

def run_file(A, cpp):
	inp = A + "_io" + "/input"
	out = A + "_io" + "/cur_output"
	for i in range(100):
		tinp = inp + str(i) + ".txt"
		tout = out + str(i) + ".txt"
		if os.path.exists(tinp):
			run(tinp, tout)
		else:
			break

def main(A):
	cpp = A + '.cpp'
	os.system("echo compilling " + cpp)
	if os.system("g++ " + cpp + " -O3") == 0:
		os.system("echo compile done")
		os.system("echo running " + cpp)
		run_file(A, cpp)
		os.system("python3 /home/.cf_gen/check_file.py " + A)
	else:
		os.system("echo compilling error")

if __name__ == '__main__':
	A = sys.argv[1:][0]
	main(A)
