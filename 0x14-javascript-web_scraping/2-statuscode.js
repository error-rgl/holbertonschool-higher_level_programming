#!/usr/bin/node
// displays the status code of a GET request.
const request = require('request');

const URL = process[2];
request(URL, function (err, response) {
  if (err) {
    console.error(err);
  }
  console.log('code:', response.statusCode);
});
