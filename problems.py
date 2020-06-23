import html_parsing, compile
import requests, os, sys, re
from bs4 import BeautifulSoup

page = None
soup = None

def url_parse(URL):
	global page, soup
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')
	
def get_number_of_problems(url):
	turl = url[22:]
	v = str(list(soup.find_all('table', {'class' : 'problems'}))[0])
	no_list = []
	for i in range(len(v)):
		if v.startswith(turl, i):
			p = i + str(v[i:]).find('\"')
			no_list.append(v[i:p].split("/")[4])
	del no_list[::2]
	return no_list

if __name__ == '__main__':
	url = sys.argv[1:][0]
	
	url_parse(url)
	url = url + "/problem/"
	no = get_number_of_problems(url)
	for A in no:
		os.system("cp ~/.cf_gen/code.cpp " + A + ".cpp")
		pid = url + A
		os.system("python3 ~/.cf_gen/html_parsing.py " + pid + " " + A)
