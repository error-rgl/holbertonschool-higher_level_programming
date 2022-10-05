#!/usr/bin/node
// prints the number of movies where the character
// “Wedge Antilles” is present.
const axios = require('axios');

const Id = '18';
let tot = 0;

axios.get(process.argv[2])
  .then(res => {
    const films = res.data.results ? res.data.results : [];
    const size = films.length;
    for (let item = 0; item < size; item++) {
      films[item].characters.forEach(chr => {
        if (chr.includes(Id)) tot++;
      });
    }
    console.log(tot);
  })
  .catch(err => {
    console.log('Error:', err);
  });
