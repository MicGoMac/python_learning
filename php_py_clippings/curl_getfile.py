﻿//e.g.link//"http://app3.rthk.hk/podcast/media/Free_as_the_wind/527_1401021529_67164.mp3"function getfile($link, $exptofile){    $ch = curl_init();    curl_setopt($ch, CURLOPT_URL, $link);    $fp = fopen( $exptofile, "w");        curl_setopt($ch, CURLOPT_FILE, $fp);    curl_setopt($ch, CURLOPT_HEADER, 0);        curl_exec($ch);    curl_close($ch);    fclose($fp);}