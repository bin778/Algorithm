function solution(s){
    let cnt = 0;
	for (let i of s) {
		if (cnt < 0) {
			break;
		} else {
			if (i === "(") {
            	cnt++;
        	} else {
            	cnt--;
        	}
		}
    }
    
    return (cnt === 0) ? true : false;
}