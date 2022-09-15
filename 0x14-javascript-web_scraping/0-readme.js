#!/usr/bin/node
// reads and prints the content of a file.
// Include the fs module
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', function (err, content) {
  if (content === undefined) {
    console.log(err);
  } else {
    console.log(content);
  }
});
