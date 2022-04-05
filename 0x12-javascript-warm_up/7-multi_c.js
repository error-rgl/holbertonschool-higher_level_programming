#!/usr/bin/node
const myNum = parseInt(process.argv[2]);
if (Number.isNaN(myNum)) {
	console.log('Missing number of occurrences');
} else {
	for (let i = 0; i <= myNum; i++) {
		console.log('C is fun');
	}
}
