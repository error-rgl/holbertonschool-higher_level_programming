#!/usr/bin/node
const myNum = parseInt(process.argv[2]);
if (Number.isNaN(myNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myNum);
}
