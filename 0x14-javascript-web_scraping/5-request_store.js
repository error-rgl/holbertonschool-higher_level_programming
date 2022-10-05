#!/usr/bin/node
// prints the number of movies where the character
// “Wedge Antilles” is present.
const axios = require('axios');
const fs = require('fs');

axios.get(process.argv[2])
  .then(res => {
    fs.writeFile(process.argv[3], res.data, err => {
      if (err) {
        return console.log(err);
      }
    });
  });
