#!/usr/bin/node

function add (a, b) {
  const numA = parseInt(a, 10);
  const numB = parseInt(b, 10);

  if (isNaN(numA) || isNaN(numB)) {
    console.error('Error: Please provide valid numbers');
    return;
  }
  return numA + numB;
}

module.exports.add = add;
