## Used libraries
import numpy as np
import pandas as pd
import subprocess
import os
import time
import grader
#--------------------------------------------------------------------------------------------------------------------
## Formal inputs
#TN = str(input("Enter Teacher's Name : ")) # Teacher Name
TM = int(input("Enter Total Marks : ")) # Total Marks
#--------------------------------------------------------------------------------------------------------------------
## Finding out the Session
year = int(time.strftime("%Y"))
if int(time.strftime("%m")) > 4:
	Session = str(year)+"-"+str(year+1)
else:
	Session = str(year-1)+"-"+str(year)
#--------------------------------------------------------------------------------------------------------------------
## Opening database to read and latex files to write
K = str(input("Enter File Name: "))
class_file = pd.read_excel(r'./DataBase/'+K+'.xlsx') # Give only .xlsx file as input
cf = np.array(class_file,dtype=str) # converting the excel file to a numpy array of dtype str
rows = cf.shape[0]
cols = cf.shape[1]
#--------------------------------------------------------------------------------------------------------------------
## Finding out class of the students:
Class = K.replace("_"," ")
#--------------------------------------------------------------------------------------------------------------------
## Making the particular tex files and processing them with pdflatex
rnd = 1 #Round off figure
for i in range(1,rows):
	(RollNo, Name, MotherName, FatherName, Term, Address)= cf[i,:][0:6]
	print(RollNo)
	cg = open("common_generator.tex") # Common latex file which can be used as base for all.
	pg = open(K+"_"+RollNo+".tex","w") # particular tex generator
	for line in cg:
		if "EnterStudentName" in line:
			line = "Name : {\\bf "+ Name+"} &  & Class : {\\bf "+Class+"}     \\\\ \n"
		elif "EnterFatherName" in line:
			line = "Father's Name : {\\bf "+FatherName+"}  &  & Roll No : {\\bf "+RollNo+"} \\\\ \n"
		elif "EnterMotherName" in line:
			line = "Mother's Name : {\\bf "+MotherName+"}  &  & Session : {\\bf "+Session+"}    \\\\ \n"
		elif "EnterAddress" in line:
			line = "Address : {\\bf "+Address+"}       &  & Term : {\\bf "+Term+"} \n"
		elif "%keypoint" in line:
			pg.write("\\begin{center}\n{\\large \n\\begin{tabular}{"+4*"|c"+"|}\n\\hline\n")
			sub = "{\\bf Subject} & {\\bf Total Marks} &{\\bf Marks Received} & {\\bf Grade}\\\\ \n \\hline \n"
			tm_rvd = 0
			tm=0
			for j in range(6,cols):
				sub += cf[0,j]+"& "+str(round(float(TM),rnd))+"& "+str(round(float(cf[i,j]),rnd))+"& "+grader.grade(round(float(cf[i,j]),rnd),TM)+"\\\\ \n\\hline \n"
				tm_rvd += round(float(cf[i,j]),rnd)
				tm += round(TM,rnd)
			pg.write(sub[0:-2]+"\n")
			pg.write("Total & "+str(float(tm))+" & "+str(tm_rvd)+" & "+grader.grade(round(tm_rvd,rnd),tm)+"\\\\ \n\\hline \n")
			pg.write("\\end{tabular}}\n\\end{center}")
		pg.write(line)
	pg.close()
	cg.close()
	os.system("pdflatex "+K+"_"+RollNo+".tex >/dev/null")
	os.system("mv "+K+"_"+RollNo+".pdf ./GradeCards")
	os.system("mv "+K+"_"+RollNo+".tex ./TexFiles")
	os.system("rm "+K+"_"+RollNo+"*")




