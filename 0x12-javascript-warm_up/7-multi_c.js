#!/usr/bin/node
let myNum = parseInt(process.argv[2]);
if (Number.isNaN(myNum)) {
	console.log('Missing number of occurrences');
} else {
	while (myNum > 0) {
		console.log('C is fun');
		myNum--;
	}
}
