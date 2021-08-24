import os
import time
from main.dir_struct import make_dirs
make_dirs("DataBase")
## Finding out the Session
year = int(time.strftime("%Y"))
if int(time.strftime("%m")) > 4:
	Session = str(year)+"-"+str(year+1)
else:
	Session = str(year-1)+"-"+str(year)

ET = ["FA_1", "FA_2", "FA_3", "FA_4", "SA_1", "SA_2", "Final"]
classes = ["Nursery", "LKG", "UKG", "1st", "2nd", "3rd","4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"]
for i in ET:
	for j in classes:
		os.system("cp ./main/Base.ods ./DataBase/"+Session+"/"+i+"/"+j+"/Genius/"+j+"_Genius.ods")
		os.system("cp ./main/Base.ods ./DataBase/"+Session+"/"+i+"/"+j+"/Brilliant/"+j+"_Brillianance.ods")
		os.system("cp ./main/Base.ods ./DataBase/"+Session+"/"+i+"/"+j+"/Superb/"+j+"_Superb.ods")
		os.system("cp ./main/Base.ods ./DataBase/"+Session+"/"+i+"/"+j+"/Superb/"+j+"_Excellence.ods")
print("You can now upload it!!!")
