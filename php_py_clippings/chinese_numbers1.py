﻿function chin_num_2_integer( t ){
	//need to improve for full function
	cchars=array( '零','一', '二', '三', '四', '五', '六', '七', '八', '九', '十',  '百', '千', '萬');
	
	t_arr=mbStringToArray( t);
  	strlen = mb_strlen(t);
//print_r(t_arr); exit();	
	//=============
	//echo  "strlen\n";
	first_char= mb_substr(t, 0, 1);
	
	
	//=========
	
	
	totalsum=array_search( end(t_arr), cchars);
			
	 
	switch (strlen){
		case 1:
			return totalsum;
			break;	
		case 2:			
			if(t_arr[1]=="十"){
				//ignore existing totalsum
				totalsum = array_search(t_arr[0], cchars) * 10;
			}elseif(t_arr[1]=="百") {
				totalsum = array_search(t_arr[0], cchars) * 100;							
			}else{
				totalsum += array_search(t_arr[0], cchars);
			}	
			return totalsum;
			break;
		case 3:
			//char 2, can only be 十 或 零, no value added
			arr_pos= array_search(t_arr[1], cchars);
			if ( arr_pos==10 ){ multiply=10;}
			if ( arr_pos==0 ){ multiply=100;}
			
			//char 3
			totalsum += multiply * array_search(t_arr[0], cchars);
			return totalsum;	
			break;	
	}
	  
} 


//from http://php.net/manual/en/function.mb-split.php
function mbStringToArray (string) { 
    strlen = mb_strlen(string); 
    while (strlen) { 
        array[] = mb_substr(string,0,1,"UTF-8"); 
        string = mb_substr(string,1,strlen,"UTF-8"); 
        strlen = mb_strlen(string); 
    } 
    return array; 
} 