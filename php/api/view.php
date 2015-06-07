<?php
//Read all contents of temperature log and put it in a variable $data
$data = file_get_contents('data/store.txt');
// Convert new lines(\n) to HTML <br> tag
echo nl2br($data);
