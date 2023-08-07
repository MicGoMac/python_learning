import os

#Listfiles( dir, ".JPG", 'is_file')

def Listfiles(dir,ext, filter){
	if ( substr( dir , -1 ) != "/" ):
		dir .= "/"
	
	
	files = array_filter(glob(dir."*ext"), filter)
	return files


#https://www.geeksforgeeks.org/python-list-files-in-a-directory/
