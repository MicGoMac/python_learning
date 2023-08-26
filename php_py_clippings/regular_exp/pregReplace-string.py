<?php
$mainDir = $argv[1]; //e.g. 28-11 , date and month, from end of nov 2011 on, all file dates created by iMacro are zero added, while month is NOT
$n = "\n";
mb_language('uni');
mb_internal_encoding('UTF-8');

$mainDirHandle = opendir( $mainDir );
while($folders=readdir($mainDirHandle)){ 

 if( is_dir($mainDir.$folders) && ( $mainDir.$folders != '.' || $mainDir.$folders != '..' ) ){ 
  // readDirs($main.$file); // no need to go sub folders
  //curious why need include parent dir like: $main.$file
  echo $mainDir.$folders;
  //checkDir ( $mainDir.$folders ) ; 
  }
  
  }//end while



function checkDir ( $dir ) 
 //load list of files in argv path
 $dirHandle = opendir( $dir);
 $totalWordCount = 0;
 $c=1;  // for test use
 while($file=readdir($dirHandle)){ 
  if( is_dir($dir.$file) || $dir.$file == '.' || $dir.$file == '..' ){ 
  // readDirs($main.$file); // no need to go sub folders
  //curious why need include parent dir like: $main.$file
  echo "skip".$file."\n"; 
  continue; // exit repeat
  }
  else{
   //files. where work start
   $path_info = pathinfo($dir.$file);
     if ( strlen($file) > 19 && ($path_info['extension']=='htm' || $path_info['extension']=='html' )) { 
       
      $tFileContent = file_get_contents( $dir."/".$file );
      //clean up to plain Chinese text
      $tLocalFile =strip_tags($tFileContent);
      // NOT work >>> echo "unicode =".is_unicode( $tLocalFile);
      $count=0;
     //check if utf8, +ve --echo "utf ".mb_check_encoding($tLocalFile, 'UTF-8');
 
     // $tLocalFile = preg_replace(array('/\d/', '/\s/', '/\n/', '/\r/', '/\t/'), '', $tLocalFile, -1 , $count);
     // not include this '/年/' , '/月/' , '/日/' , 
     
     $replaceElements = array('/\d/' , '/ /' , '/\n/', '/\r/', '/\t/' , '/%/' , '/，/', '/。/', '/（/', '/）/' , '/「/', '/」/','/[a-zA-Z]/', '#(信報財)(.*)(不得轉載)#e', '/信報網站/' ,  '/星期/' , '/返回前頁/' , '/｜/' , '/列印/' , '/歡迎 MicMac（帳戶設定｜登出）/' , '/訂閱信報網上版一年港幣/' , '/最新消息/' , '/今日備忘錄/' , '/股價敏感資料/' , '/主頁/' , '/即時新聞/' , '/金融行情/' , '/今日信報/' , '/地產投資/' , '/信報論壇/' , '/信博/' , '/專題特輯/' , '/信網智庫/' , '/優雅生活/' , '/信報月刊/' , '/視聽頻道/' , '/信網購物/' , '/目錄/' , '/要聞/' , '/理財投資/' , '/信報評論/' , '/財經新聞/' , '/地產市道/' , '/獨眼．政治/' , '/兩岸國際/' , '/體育消息/' , '/生活藝術/' , '/股市行情表/' , '/搜尋/' , '/社評/' , '/全文/' , '/文章/' , '/今日熱門文章/', '/、/' , '/：/' , '/《/' , '/》/' , '/﹐/' , '/＊/' , '/；/' , '/年月日/', '/　/', '/．/');
     
     $tLocalFile = preg_replace( $replaceElements , '', $tLocalFile, -1 , $count);
     $tLocalFile =str_replace( ".", "", $tLocalFile ); 
    // echo "clean count ".$count.$n; 
      //----for visual checking
      // echo $tLocalFile.$n;
   // echo substr( $tLocalFile, 0, 21).$n;  //this show that 3 char  = 1 chinese char 
   
    //now word by word DB check
      for( $i=0; $i< strlen($tLocalFile); $i++){
        //this is the char to be submitted to DB !!!
        //echo substr( $tLocalFile, $i, 3).$n;
        $i=$i + 2;
        }
      } //end if file extension
  } //end if != .
   
   
   if( $file != '.' && $file != '..' ){
    //----- clean away <base href= from $tLocalFile
		// $regex = '#(<base href=)(.*)(">)#e'; //takes away the base href tag
		 //$cleaned_tLocalFile = preg_replace($regex,"(' ')",$tLocalFile); 
		 }
		 
		 $totalWordCount= $totalWordCount + strlen($tLocalFile)/3;
		 echo $file." done."."\n"; 
		 echo 'strlen='.(strlen($tLocalFile)/3).$n;
		 
		 //for testing, limiting file check
		 $c= $c+1;
		 if ( $c>9){
		 //die();
		 }
  } //end while
  
  echo "One Directory done."."\n"; 
  echo "Total word count=".$totalWordCount."\n"; 
  } //end function checkDir
?>