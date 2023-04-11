inlets = 1; 
outlets = 2; 
autowatch = 1; 

// outputs a list with indicies of where the ones are in the binary string input.

function getOnesPos(bin) {
	var output = []
	for (i=0; i<bin.length; i++) {
		if (bin[i] === "1") {
			output.push(i);
		}
	}
	outlet(0, output);
}