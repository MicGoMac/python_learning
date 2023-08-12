
import os.path
dir ="/home/micgomac/python_learning/php_py_clippings"

afile=dir + "myfile.php"

bname=os.path.basename(dir)
bdir=os.path.dirname(dir)

fexist=os.path.exists(dir)
f_isfile=os.path.isfile(afile)
f_isdir=os.path.isdir(afile)

p="~/python_learning/php_py_clippings"
#expand to full path /home/xxx/....
# path,isabs checks if full path
full_path_str = os.path.expanduser(p)

ext = os.path.splitext(afile)
print(ext)

'''
$pi = pathinfo($dir);
$dn= $pi['dirname'];
$bn= $pi['basename'];
$ext= $pi['extension'];
$fn= $pi['filename'];
'''
