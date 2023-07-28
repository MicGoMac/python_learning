function add_zero( $str, $digits ) {
	$para = "%0".$digits."d";
	return 	sprintf($para, $str);
}