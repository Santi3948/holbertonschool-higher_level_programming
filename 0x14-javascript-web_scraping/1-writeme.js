#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const content = args[3];
fs.writeFile(args[2], content, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
  // file written successfully
});
