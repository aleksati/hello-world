inlets = 1;
outlets = 1;
autowatch = 1;

// convert an integer into a 8-bit binary list, such as "1 0 0 1 1 0 1".

function msg_int(numb) {
	var intResult = numb2bin(numb); 
	outlet(0, intResult);
}

function list() {
	var lstInput = arrayfromargs(arguments);
	var lstResult = [];
	
	for (j=0;j<lstInput.length;j++) {
		var lstBin = numb2bin(lstInput[j]);
		
		for (k=0;k<lstBin.length;k++) {
			lstResult.push(lstBin[k]);
		}
	}
	
	outlet(0, lstResult);
}

function numb2bin(numb) {
	var listBin = []
	var bin = numb.toString(2);
	
	// if the bin is less than 8 char long, add 0s until length is 8
	while (bin.length != 8) {
		bin = "0"+bin;
	}
	
	// add items as sperate items in a list
	// much easier to use in max
	for (i=0;i<bin.length;i++) {
		listBin.push(Number(bin[i]));
	}
	
	return listBin;
}


