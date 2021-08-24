#!/usr/bin/env python

import time
import subprocess
import os

## Finding out the Session
year = int(time.strftime("%Y"))
if int(time.strftime("%m")) > 4:
	Session = str(year)+"-"+str(year+1)
else:
	Session = str(year-1)+"-"+str(year)

## list of exam types:
ET = ["FA_1", "FA_2", "FA_3", "FA_4", "SA_1", "SA_2", "Final"]
classes = ["Nursery", "LKG", "UKG", "1st", "2nd", "3rd","4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"]
sections = ["Genius","Brilliance","Superb","Excellance"]
def dir_gen(direc):
	os.system("mkdir ./"+direc+"/"+Session)
	for i in ET:
		os.system("mkdir ./"+direc+"/"+Session+"/"+i)
		for j in classes:
			os.system("mkdir ./"+direc+"/"+Session+"/"+i+"/"+j)
			for k in sections:
				os.system("mkdir ./"+direc+"/"+Session+"/"+i+"/"+j+"/"+k)
	
## Making the directory structure
def make_dirs(direc):
	sessions = subprocess.getoutput("ls ./"+direc)

	if Session in sessions:
		print(f"The directory/folder structure for session {Session} already exists.")
	else:
		dir_gen(direc)
