﻿function stripping ( $source_t , $s1, $s2){	$t1 = strpos( $source_t, $s1 );		if ($t1 === false ) {		return "";		}		$t2 = strpos( $source_t, $s2, $t1 );			if ($t2 === false ) {		$t2= strlen( $source_t) ;		}					return substr( $source_t, $t1, $t2-$t1 );}