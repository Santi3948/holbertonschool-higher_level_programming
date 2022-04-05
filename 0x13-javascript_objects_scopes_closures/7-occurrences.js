#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((acc, elem) => {
    return (searchElement === elem ? acc + 1 : acc);
  }, 0);
};
