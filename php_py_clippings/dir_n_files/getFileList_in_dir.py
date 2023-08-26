import os, sys
my_file = sys.argv[0]
print(my_file)

#Listfiles( dir, ".JPG", 'is_file')

def Listfiles(dir,ext, filter):
	if ( substr( dir , -1 ) != "/" ):
		dir =dir + "/"
	
	
	files = array_filter(glob(dir,"*ext"), filter)
	return files


#https://www.geeksforgeeks.org/python-list-files-in-a-directory/
