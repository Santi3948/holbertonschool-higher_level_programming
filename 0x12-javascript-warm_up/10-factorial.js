#!/usr/bin/node
function factorial (a) {
  if (a === 0 || isNaN(a)) { return (1); }
  return (factorial(a - 1) * a);
}
console.log(factorial(parseInt(process.argv[2])));
