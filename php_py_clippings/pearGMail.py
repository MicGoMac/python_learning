﻿function phpMail($from, $to, $subject, $body, $password )        require_once "MDB2.php";    require_once "Mail.php";    require_once "Mail/mime.php"; /*    $from = "<mini@auto.com>";    $to = "<hello@microlingolo.com>";    $subject = "Test from iyearbook!";    $body = "Hi,\n\nHow are you?";*/    $host = "ssl://smtp.gmail.com";    $port = "465";    $username = "micgomac@gmail.com";    //$password = "";        $headers = array ('From' => $from,        'To' => $to,        'Subject' => $subject);            $smtp = Mail::factory('smtp',        array ('host' => $host,        'port' => $port,        'auth' => true,        'username' => $username,        'password' => $password));        $mail = $smtp->send($to, $headers, $body);    if (PEAR::isError($mail)) {        echo( "Failed. Error: ".$mail->getMessage() );     } else {        echo("OK");     }