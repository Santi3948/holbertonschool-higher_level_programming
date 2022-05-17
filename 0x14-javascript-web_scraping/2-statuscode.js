#!/usr/bin/node
const axios = require('axios');
const args = process.argv;
axios.get(args[2])
  .then(function (response) {
    console.log('code:', response.status);
  })
  .catch(function (error) {
    if (error.response) {
      console.log('code:', error.response.status);
    }
  });
