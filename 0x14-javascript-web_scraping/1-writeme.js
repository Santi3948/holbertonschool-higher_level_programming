#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const content = args[3];
fs.writeFile(args[2], 'utf8', content, err => {
  if (err) {
    console.error(err);
  }
  // file written successfully
});
