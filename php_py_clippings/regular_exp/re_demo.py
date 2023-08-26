
#a greedy test


t='''function getAllDir $ddir  {
	while($file=readdir($dirHandle)){  
		if( substr($file,  ' idfasfaskdklklsdsdfsfsdf' file'vvvvvvvile'dafadfs' ){ 
			//echo "skip".$file."\n"; 
			continue;
		} elseif (is_dir($ddir.$file)) {
			echo $ddir.$file."/"; echo "\n";
			$res[]=$ddir.$file."/" ;
			getAllDir( $ddir.$file."/" );
'''
import re

ser= re.search( "file.*\'", t)

print("re.search")
print(ser)
print(ser.group())
 
ser= re.search( "file.*?\'", t)
print(ser)
print(ser.group()) 

ser= re.findall( "file.*\'", t)
print("re.findall greedy")   
print(ser)

print("re.findall non greedy")  
ser= re.findall( "file.*?\'", t)
print(ser) 



