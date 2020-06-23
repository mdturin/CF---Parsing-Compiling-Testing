import requests, os, sys
from bs4 import BeautifulSoup

page = None
soup = None

def urlparse(URL):
	global page, soup
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')

def get_input():
	inp = []
	inp_area = soup.find_all('div', {'class': 'input'})
	for __ in inp_area:
		v = str(list(__)[3])[6:-7]
		inp.append(v)
	return inp

def get_output():
	out = []
	out_area = soup.find_all('div', {'class': 'output'})
	for __ in out_area:
		v = str(list(__)[3])[6:-6]
		out.append(v)
	return out

def print_inp_out(inp, out):
	for i in range(len(inp)):
		print("INPUT :", (i+1))
		print(inp[i])
		print("")
		
		print("OUTPUT :", (i+1))
		print(out[i])
		print("")

def create_dir(A):
	B = A + "_io"
	os.system("echo creating directory " + B)
	if os.path.exists(B) == False:
		os.system("mkdir " + B)
	os.system("echo done creating " + B)

def write_input(inp, A):
	B = A + "_io"
	for i in range(len(inp)):
		f = open(B + "/input" + str(i) + ".txt", "w")
		f.write(inp[i])

def write_output(inp, A):
	B = A + "_io"
	for i in range(len(out)):
		f = open(B + "/output" + str(i) + ".txt", "w")
		f.write(out[i])

if __name__ == '__main__':
	url = sys.argv[1:][0]
	A = sys.argv[1:][1]
	
	# url = "https://codeforces.com/contest/1370/problem/F1"
	# A = "F1"
	
	urlparse(url)
	create_dir(A)
	inp = get_input()
	out = get_output()
	write_input(inp, A)
	write_output(out, A)
	#print_inp_out(inp, out)
