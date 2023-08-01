/a modern way of get files in dir
//e.g. Listfiles(sdir, ".JPG", 'is_file')
//leave ext empty for folders
def Listfiles(dir,ext, filter){
	if ( substr( dir , -1 ) != "/" ):
		dir .= "/"
	
	
	files = array_filter(glob(dir."*ext"), filter)
	return files


#https://www.geeksforgeeks.org/python-list-files-in-a-directory/
