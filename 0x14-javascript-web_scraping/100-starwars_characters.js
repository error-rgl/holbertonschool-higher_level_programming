#!/usr/bin/node
// prints the characters present in a Star Wars Movie
const axios = require('axios');

axios.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`)
  .then(res => {
    res.data.characters.forEach(async (data) => {
      await axios.get(data)
        .then(res => {
          console.log(res.data.name);
        });
    });
  })
  .catch(err => {
    console.log('Error:', err);
  });
