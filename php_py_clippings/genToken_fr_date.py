﻿function generate_token(  ) {    $salt="loklok";    date_default_timezone_set('Asia/Hong_Kong');	$token= $salt.date("j-n-Y-H-i-s" );    return md5($token);}