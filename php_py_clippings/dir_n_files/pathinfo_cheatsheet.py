import os.path as pi

dir ="/home/micgomac/python_learning/php_py_clippings/"

afile=dir + "test.py"

bname=pi.basename(afile)
bdir=pi.dirname(afile)

print( "basename & dirname="+ bname + "," + bdir)

fexist=pi.exists(afile)
f_isfile=pi.isfile(afile)
f_isdir=pi.isdir(afile)

if (fexist and f_isfile):
    print( "file exist ")

p="~/python_learning/php_py_clippings"
#expand to full path /home/xxx/....
# path,isabs checks if full path
full_path_str = pi.expanduser(p)

ext = pi.splitext(afile)
print ("extension=")
print(ext)

