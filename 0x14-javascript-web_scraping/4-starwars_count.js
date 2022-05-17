#!/usr/bin/node
const axios = require('axios');
const args = process.argv;
let count = 0;
axios.get(args[2])
  .then(function (response) {
    for (let i = 0; i < (response.data.results).length; i++) {
      for (let j = 0; j < (response.data.results[i].characters).length; j++) {
        if (response.data.results[i].characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
          count = count + 1;
        }
      }
    }
    console.log(count);
  });
