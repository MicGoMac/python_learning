


'''
 // set URL and other appropriate options
    curl_setopt($ch, CURLOPT_URL, $tLink );
    curl_setopt($ch, CURLOPT_HEADER, 0);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1 );
    // grab URL and pass it to the browser
    $stext = curl_exec($ch);
 
    //see if there is 404 Not Found
     if ( strpos(  $stext, "404 Not Found")===false ){
		  $img = file_get_contents( $tLink );
		//echo $saveDir."/".$saveFileName;
		file_put_contents( $myDir."/".$saveFileName ,$img);
    }else{
		echo "404 Not Found. End.";
		break;
    }
'''
