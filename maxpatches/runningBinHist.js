inlets = 1; 
outlets = 2; 
autowatch = 1; 

var accum = [];
var norm_hist = [];
var count = 0;

// add binaries "on top of each other" for a histogram effect.

function bin2hist(bin) {
	
	if (!accum.length || !norm_hist.length) {
		init(bin.length);
	}
	
	// accumulate binary values 
	for (i=0; i<bin.length; i++) {
		accum.splice(i, 1, Number(bin[i]) + accum[i]);
	}

	count += 1;
		
	// normalize values based on count
	for (i=0; i<accum.length; i++) {
		norm_hist.splice(i, 1, (1/count)*accum[i])
	}
 
	
	outlet(0, count);
	outlet(1, norm_hist);

}

function init(length){
	for (i=0; i<length; i++) {
		accum.push(0);
		norm_hist.push(0);
	}
	
	outlet(0, count);
	outlet(1, norm_hist);
}


function clear() {
	accum = [];
	norm_hist = [];
	count = 0;
	
	outlet(0, 0);
	outlet(1, 0);
}