<?php

if(!isset($_POST['t'])){
   die;
}
$temperature = $_POST['t'];

$myFile = "data/store.txt";
$fh = fopen($myFile, 'a') or die("can't open file");
$now = date('Y-m-d h:i:s');
$stringData = $now."|".$temperature;
fwrite($fh, $stringData.PHP_EOL);
fclose($fh);
echo $stringData;
