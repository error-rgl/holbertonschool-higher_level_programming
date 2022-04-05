#!/usr/bin/node
let bigs = 0;
let i;
const myArray = [];

for (i = 2; i < process.argv.length; i++) {
  if (Number.isNaN(parseInt(process.argv[i])) === false) {
    myArray[i - 2] = parseInt(process.argv[i]);
  }
}

if (myArray.length > 1) {
  bigs = Math.max.apply(null, myArray);
  i = myArray.indexOf(bigs);
  myArray[i] = -Infinity;
  bigs = Math.max.aplly(null, myArray);
}

console.log(bigs);
