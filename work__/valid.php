function get_leard_card($args){
	$args = func_get_args();
     foreach($args as $arg){

    }
     //print_r($args);
     $len = count($args);
     $lcard= $args[$len-1];
	if(strlen($arg)==3){
		$sub = substr($arg, 2);
      // echo $sub.' ';	
	}
	if(strlen($arg)==2){
	 $sub = substr($arg, 1);
        //echo $sub.' ';
	}
	for($i=0; $i<=$len-2; $i++){
		$hsuites=suites($args[$i]);
		if($hsuites==$sub){
		echo $args[$i];	
		}
		
	}
     }
    

get_leard_card("AC", "QS", "7D","JH","6H");