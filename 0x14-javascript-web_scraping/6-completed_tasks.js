#!/usr/bin/node
const axios = require('axios');
const args = process.argv;
const dicc = {};
let count = 0;
axios.get(args[2])
  .then(function (response) {
    for (let i = 0; i < (response.data).length; i++) {
      if (response.data[i].completed === true) {
        count = count + 1;
      }
      if (response.data[i].id % 20 === 0) {
        dicc[response.data[i].userId] = count;
        count = 0;
      }
    }
    console.log(dicc);
  });
