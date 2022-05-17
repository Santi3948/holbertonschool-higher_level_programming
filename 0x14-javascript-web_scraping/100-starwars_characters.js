#!/usr/bin/node
const axios = require('axios');
const args = process.argv;
axios.get('https://swapi-api.hbtn.io/api/films/' + args[2])
  .then(function (response) {
    for (let i = 0; response.data.characters[i]; i++) {
      axios.get(response.data.characters[i])
        .then(response => {
          console.log(response.data.name);
        });
    }
  });
