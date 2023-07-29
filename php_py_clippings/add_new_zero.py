#this for strings
def addzero_2_str( s, digits ):
	return s.zfill(digits)

#this for int
def add_zero( int, digits ): 
	para = "%0"+digits+"d";
	return para % int 

print( addzero_2_str('32ia',6) )

print( add_zero(32,"6"))
