#!/usr/bin/node
const axios = require('axios');
const fs = require('fs');
const args = process.argv;
axios.get(args[2])
  .then(function (response) {
    fs.writeFileSync(args[3], response.data);
  });
