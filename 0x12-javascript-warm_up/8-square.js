#!/usr/bin/node
if (process.argv[2] && (process.argv[2] > 0)) {
  for (let i = 0; i < process.argv[2]; i++) {
    let pr = '';
    for (let i = 0; i < process.argv[2]; i++) {
      pr = pr + 'X';
    }
    console.log(pr);
  }
} else if (!process.argv[2]) {
  console.log('Missing size');
}
