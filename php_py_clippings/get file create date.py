<?php
$file=$argv[1];
echo getcdate( $file );

function getcdate( $fullPathFile ) {
$commandtext= 'mdls '.'"'.$fullPathFile.'"';
$metaData = shell_exec( $commandtext );
//echo $metaData;

$p1 = "/kMDItemContentCreationDate.+(.*).[0-9]/"; 

if ( !preg_match($p1 , $metaData, $match)) {
 	$p2 = "/kMDItemFSCreationDate.+(.*).[0-9]/";
 	if ( !preg_match($p2 , $metaData, $match)) {
 	return "Error. ".$metaData; }  
  }
//print_r( $match[0] );
 $res = $match[0];
 
$trim2 =  strpos( $res, "= ", 0 ); //the = space marks a start, kMDItemContentCreationDate     = 2011-03-04 01:31:36 +0800
$trim2 = $trim2 + 2;
$trim3 =  strpos( $res, " +", $trim2 ); //the first + sign marks an end
$dateData= substr( $res, $trim2,  $trim3-$trim2);

return $dateData; 
//sample result= 2011-03-16 17:52:38

 /*
$trim1 = strpos( $metaData, "kMDItemContentCreationDate" ); // I met file without this
$trim1b = strpos( $metaData, "kMDItemFSCreationDate" ); 
	if ($trim1===false)  {  
	return "Error. No kMDItemContentCreationDate from system."; 
	}else{
	$trim1=$trim1+strlen("kMDItemContentCreationDate");
	}
	
$trim2 =  strpos( $metaData, "= ", $trim1 ); //the = space marks a start, kMDItemContentCreationDate     = 2011-03-04 01:31:36 +0800
$trim3 =  strpos( $metaData, " +", $trim1 ); //the first + sign marks an end
$trim4 =  strpos( $metaData, "kMDItemContentModificationDate", $trim1 ) - 1;  //for double check in case
$dateData= substr( $metaData, $trim2,  $trim3-$trim2);
*/

}

?>