
import datetime

def generate_token( salt ):
	#this is the client side use, never too close to minute change
	if (salt==None):
		print( "you forgot to add salt")

	
	if ( curr_date <= 55 ):
		token=""
	else:
		sleep
		token=""
	return 1

'''
function generate_token(  ) {
    //this is the client side use, never too close to minute change
    $salt="loklok";
     date_default_timezone_set('Asia/Hong_Kong');
     $today_code_m_d = date("n-d");  // m-d is directory use
	  
    if (date( "s" ) <= 55 ) {
        $token= $salt.date("j-n-Y-H-i" );
     } else {
         //wait till next minute... f
         sleep( (60 - date( s ) + 1) );
         $token= $salt.date("j-n-Y-H-i" );
     }
    return md5($token);
    }
'''
