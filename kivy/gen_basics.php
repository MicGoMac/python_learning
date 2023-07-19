<?php

$appname = readline("App name?");

//must the app name be one word?
//make it one word, meaning no space
$appname = ucwords($appname);
$appname = str_replace( " ", "", $appname);

echo "App name is $appname";

//3 diff var for diff use
$Appname = ucfirst($appname);
$AppName = ucwords($appname);
$appname = strtolower($appname);

//output dir, every thing gen here
//
$app_dir =dirname(__FILE__). "/$appname" . "_kv" ;

//check if dir already there
if (file_exists($app_dir)){

}else{
	mkdir( $app_dir );
}

?>
