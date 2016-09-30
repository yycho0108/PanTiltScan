function setAutomaticScan(){
	if(startedAutomaticScan){
		theta = MIN_ANGLE;
		phi = MIN_ANGLE;
		startedAutomaticScan = false;
	} else{
	// looping through theta and phi: setting every possible value for phi before incrementing theta
		if(theta <= MIN_ANGLE && dir == -1){
			if(phi >= MAX_ANGLE){
				// scan complete
				automaticScan = false;
				return;
			}
			// otherwise, increment theta, and return phi to start angle
			dir = 1; // now scan upwards
			phi += offset;
			theta = MIN_ANGLE;
		}
		else if(theta >= MAX_ANGLE && dir == 1){
			if(phi >= MAX_ANGLE){
				// scan complete
				automaticScan = false;
				return;
			}
			// otherwise, increment theta, and return phi to start angle
			phi += offset;
			dir = -1; // now scan downwards
			theta = MAX_ANGLE;
		} else{
			// keep the theta, and move the phi
			theta += offset * dir;
		}
	}
}
