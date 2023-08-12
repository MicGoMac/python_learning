﻿function get_query(){	
	$current_url= "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
	
	//break down the param, e.g.:
	//http://128.199.104.14/ut_rss/index.php?date=2020-03-17d
	$curr_url=explode( "?", $current_url);
	$queries = $curr_url[1];
	$qs=explode( "&", $queries);
	
	$q_items=array();
	foreach($qs as $q){
		$q_str=explode( "=", $q);
		$q_items[$q_str[0]] = $q_str[1];
	}
	return $q_items;
}
