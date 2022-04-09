#!/usr/bin/node
if (process.argv[2] && (process.argv[2] > 0)) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
} else if (!process.argv[2]) {
  console.log('Missing number of occurrences');
}
