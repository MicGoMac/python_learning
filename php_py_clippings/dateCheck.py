<?php 
$exp_date = "2006-01-16";
$todays_date = date("Y-m-d");
$today = strtotime($todays_date);
$expiration_date = strtotime($exp_date);
if ($expiration_date > $today) {
     //$valid = "yes";
     echo "";
} else {
    // $valid = "no";
} ?>
