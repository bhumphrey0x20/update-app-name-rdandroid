'''
	Python script to change app name in rawdrawandroid. 
	It updates AndroidManifest.xml, strings.xml, and Makefile

	** Must provide old name and new name, without file extensions,  on CLI
		ex: python editAppName.py <old Name> <new Name>
	
'''

import numpy as np
import sys
import os


input_files = ["AndroidManifest.xml", "strings.xml","Makefile"]
file = "strings.xml"
dir_name = "updated"
out_path = "./"+dir_name+"/"


if (len(sys.argv) < 3):
	print("Cannot parse data, please provide new file names");
else:
	app_old_name, app_new_name = sys.argv[1], sys.argv[2]
	print(app_old_name, app_new_name)	


if(not os.path.isdir(dir_name) ):
	os.mkdir(dir_name)

for file_ in input_files:
	#print(file_)


	out_file = out_path+file_
	fout = open(out_file, 'w')
	
	for line in open(file_, 'r'):
		#print(line)
		# search for keyword in line
		ret = line.find(app_old_name)

		# if keyword found, splice it
		if(ret > -1):
			split_line = line.split(app_old_name)
			new_line = split_line[0]+app_new_name+split_line[1]
		else:
			new_line = line
		
		fout.write(new_line);


	fout.close()
	print(file_+" updated with new app name.\n")
	

