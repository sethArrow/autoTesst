<?php
$ranks = array('6'=>'6', '7'=>'7', '8'=>'8', '9'=>'9', '10'=>'10', 'J'=>'11', 'Q'=>'12', 'K'=>'13', 'A'=>'14');
$hand1 =array('AD','6H','9C','QC', '8H');
$hand2 =array('9H','10C','8D','6C', '10S');
function play($cd, $play, $p1){
	global $hand1;
	global $hand2;
	$cd = $cd;
	$play = $play;
	$p1 = $p1;
	
	if($play==1 && $p1=='p1'){
		unset($hand1[0]);
		$len = count($hand1);
		return $len;
	
	}elseif($play==1 && $p1=='p2'){
		unset($hand2[0]);
		$len = count($hand2);
		return $len;
	}
	
	elseif($play==2 && $p1=='p1'){
		unset($hand1[0]);
		unset($hand1[1]);
		$len = count($hand1);
		return $len;
	}elseif($play==2 && $p1=='p2'){
		unset($hand2[0]);
		unset($hand2[1]);
		$len = count($hand2);
		return $len;
	}
	//3rd play p2 leads
	elseif($play==3 && $p1=='p2'){
		unset($hand2[0]);
		unset($hand2[1]);
		unset($hand2[2]);
		$len = count($hand2);
		return $len;
	}elseif($play==3 && $p1=='p1'){
		unset($hand1[0]);
		unset($hand1[1]);
		unset($hand1[2]);
		$len = count($hand1);
		return $len;
	}
	//4th play p1 leads
	
	elseif($play==4 && $p1=='p1'){
		unset($hand1[0]);
		unset($hand1[1]);
		unset($hand1[2]);
		unset($hand1[3]);
		$len = count($hand1);
		return $len;
	}elseif($play==4 && $p1=='p2'){
		unset($hand2[0]);
		unset($hand2[1]);
		unset($hand2[2]);
		unset($hand2[3]);
		$len = count($hand2);
		return $len;
	}
	//5th play p1 leads
	elseif($play==5 && $p1=='p1'){
		unset($hand1[0]);
		unset($hand1[1]);
		unset($hand1[2]);
		unset($hand1[3]);
		unset($hand1[4]);
		$len = count($hand1);
		return $len;
	}elseif($play==5 && $p1=='p2'){
		unset($hand2[0]);
		unset($hand2[1]);
		unset($hand2[2]);
		unset($hand2[3]);
		unset($hand2[4]);
		$len = count($hand2);
		return $len;
	}
	}
//echo play('AD',1, 'p1');

    function suites($args){
	$args = func_get_args();
     foreach($args as $arg){
	if(strlen($arg)==3){
		$sub = substr($arg, 2);
       return $sub;	
	}
	if(strlen($arg)==2){
	 $sub = substr($arg, 1);
        return $sub;
	}
	
     }
}
suites('AD', 'BC');


/**********************************************************/


?>