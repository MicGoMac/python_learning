
#ref to read:https://stackoverflow.com/questions/39094125/python-can-i-add-utf8-bom-to-a-file-without-opening-it
bom=(b"0xEF" )

#print(bom

print(bom.encode("UTF-8"))

#$bom =( chr(0xEF) . chr(0xBB) . chr(0xBF) ); 
