#!/usr/bin/node
exports.converter = function (base) {
  return function NumbConv (numb) {
    return numb.toString(base);
  };
};
