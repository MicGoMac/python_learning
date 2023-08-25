


'''
function checkDir ( $ddir ) {
 //works on FILES in a given Directory. Skip any Dir inside
 $dirHandle = opendir( $ddir); 
 while($file=readdir($dirHandle)){  
      if( is_dir($file) || substr($file, 0,1) == '.' ){ 
          // readDirs($main.$file); // no need to go sub folders 
          echo "skip".$file."\n"; 
          continue; // exit repeat
      }
      else{
       //files. where work start
       $path_info = pathinfo($ddir.$file);
          // optiional check // if ( strlen($file) > 19 && ($path_info['extension']=='htm' || $path_info['extension']=='html' ) ) { 
             
        } 
      }
  }
'''
