#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((counter, currentNum) => 
	  currentNum === searchElement ? counter + 1 : counter, 0);
};
