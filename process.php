<?php
$integers = $_GET['integers'];
$threshold = $_GET['threshold'];

$output = shell_exec("python3 bitwise_operations.py '$integers' '$threshold'");
echo nl2br($output);
?>
