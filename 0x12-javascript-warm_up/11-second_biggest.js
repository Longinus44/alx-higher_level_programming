#!/usr/bin/node

function findSecondLargestNum (args) {
  if (args.length <= 1) { return 0; }

  const nums = args.map(num => parseInt(num));

  let max = nums[0];
  let secondMax = null;
  for (const num of nums) {
    if (num > max) {
      secondMax = max;
      max = num;
    } else {
      if (num > secondMax && num < max) {
        secondMax = num;
      }
    }
  }
  return secondMax;
}

const args = process.argv.slice(2);

console.log(findSecondLargestNum(args));
