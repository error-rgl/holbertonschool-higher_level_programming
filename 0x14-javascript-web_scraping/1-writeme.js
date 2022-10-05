#!/usr/bin/node
// script that writes a string to a file
const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];
fs.writeFile(filePath, content, 'utf-8', function (err, data) {
  if (err) {
    console.error(err);
  }
});
