#!/usr/bin/node
const list = process.argv.slice();
list.shift();
list.shift();
list.sort(function (a, b) { return a - b; });
if (list.length === 0 || list.length === 1) {
  console.log(0);
} else if (list[list.length - 2]) {
  console.log(list[list.length - 2]);
}
