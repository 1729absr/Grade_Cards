## Used libraries
import multiprocessing as mp
import numpy as np
import pandas as pd
import subprocess
import os
import time
from main.grader import grade
from main.dir_struct import make_dirs
#--------------------------------------------------------------------------------------------------------------------
make_dirs("GradeCards")

## Total marks for each subject
TM = int(input("Enter Total Marks : ")) # Total Marks
ET = str(input("Enter Exam Type : "))
#--------------------------------------------------------------------------------------------------------------------
## Finding out the Session
year = int(time.strftime("%Y"))
if int(time.strftime("%m")) > 4:
	Session = str(year)+"-"+str(year+1)
else:
	Session = str(year-1)+"-"+str(year)
#--------------------------------------------------------------------------------------------------------------------
## DataBase reading
classes = subprocess.getoutput("ls ./DataBase/"+Session+"/"+ET).split("\n")
#--------------------------------------------------------------------------------------------------------------------
## Making the particular tex files and processing them with pdflatex
rnd = 1 # Round off figure
def pdf_gen(K):
    ## Opening database to read and latex files to write
    Sections = subprocess.getoutput("ls ./DataBase/"+Session+"/"+ET+"/"+K).split("\n")
    for Section in Sections:
        class_file = pd.read_excel(r'./DataBase/'+Session+"/"+ET+"/"+K+"/"+Section+"/"+K+"_"+Section+".ods",engine = "odf") # Give only .ods file as input
        cf = np.array(class_file,dtype=str) # converting the excel file to a numpy array of dtype str
        rows = cf.shape[0]
        cols = cf.shape[1]
        ## Finding out class of the students:
        Class = K+" ("+Section+")"
        for i in range(1,rows):
        	(RollNo, Name, MotherName, FatherName, Term, Address)= cf[i,:][0:6]
        	print(RollNo)
        	cg = open("./main/common_generator.tex") # Common latex file which can be used as base for all.
        	pg = open("./main/TexFiles/"+RollNo+"_"+K+".tex","w") # particular tex generator
        	for line in cg:
        		if "GRADE CARD" in line:
        			line = "{\\bf \\Large GRADE CARD ("+ET.replace("_","-")+")}\n"
        		elif "EnterStudentName" in line:
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
        				sub += cf[0,j]+"& "+str(round(float(TM),rnd))+"& "+str(round(float(cf[i,j]),rnd))+"& "+grade(round(float(cf[i,j]),rnd),TM)+"\\\\ \n\\hline \n"
        				tm_rvd += round(float(cf[i,j]),rnd)
        				tm += round(TM,rnd)
        			pg.write(sub[0:-2]+"\n")
        			pg.write("Total & "+str(float(tm))+" & "+str(tm_rvd)+" & "+grade(round(tm_rvd,rnd),tm)+"\\\\ \n\\hline \n")
        			pg.write("\\end{tabular}}\n\\end{center}\n\\vspace{1cm}\n")
        			pg.write("\\hfill{\\bf Date: "+time.strftime("%B %d, %Y")+"}\\\\\\\\ \n")
        		pg.write(line)
        	pg.close()
        	cg.close()
        	os.system("pdflatex ./main/TexFiles/"+RollNo+"_"+K+".tex")
        	os.system("mv "+RollNo+"_"+K+".pdf ./GradeCards/"+Session+"/"+ET+"/"+K+"/"+Section)
        	#os.system("rm ./main/TexFiles/"+RollNo+"_"+K+".tex")
        	os.system("rm "+RollNo+"_"+K+".log "+RollNo+"_"+K+".aux "+RollNo+"_"+K+".out")
#pdf_gen(classes[0])
for cla in classes:
	pdf_gen(cla)


