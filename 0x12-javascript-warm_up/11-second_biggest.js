#!/usr/bin/node
const list = process.argv;
list.shift();
list.shift();
list.sort();
const Max = Math.max(list);
if (list.length >= 2) {
  for (let i = list.length - 1; i > 0; i--) {
    if (Max != list[i]) {
      console.log(list[i]);
      break;
    }
  }
} else {
  console.log('0');
}
