#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const size = list.length;
  for (let i = 0; size > i; i++) {
    if (searchElement === list[i]) {
      count++;
    }
  }
  return count;
};
