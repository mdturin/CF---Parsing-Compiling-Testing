#! /usr/bin/bash

com=($1)
p="-p"
c="-c"

if [ "$com" = "$p" ]; then
	echo "parsing starting"
	parse_link=($2)
	python3 /home/psy__cho/.cf_gen/problems.py

elif [ "$com" = "$c" ]; then
	echo "compiling starting"
	cpp_file=($2)
	python3 /home/psy__cho/.cf_gen/compile.py "$cpp_file"

else
	echo "syntex error"

fi
