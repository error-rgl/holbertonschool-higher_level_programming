#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');

const fArg = fs.readFileSync(argv[2]).toString();
const sArg = fs.readFileSync(argv[3]).toString();
fs.writeFileSync(argv[4], fArg + sArg);
