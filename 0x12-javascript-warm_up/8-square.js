#!/usr/bin/node
const mySize = parseInt(process.argv[2]);
if (Number.isNaN(mySize)) {
	console.log('Missing size');
} else {
	for (let i = 0, chr; i < mySize; i++) {
		chr = '';
		for (let j = 0; j < mySize; j++) {
			chr += 'X';
		}
		console.log(chr);
	}
}
