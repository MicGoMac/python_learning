

echo $_SERVER["REQUEST_URI"];
echo $_SERVER["REMOTE_ADDR"];
echo $_SERVER["DOCUMENT_ROOT"];
echo $_SERVER["SERVER_ADDR"];
echo $_SERVER["PHP_SELF"];
/*e.g.
/video/_Sep09/test.php 
192.168.1.102  from
/var/www/html/ full doc root
192.168.1.89 domain 
/video/_Sep09/test.php  me
*/
