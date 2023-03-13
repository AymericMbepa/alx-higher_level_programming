#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  let max1 = args[0];
  let max2 = args[1];

  if (max2 > max1) {
    [max1, max2] = [max2, max1];
  }

  for (let i = 2; i < args.length; i++) {
    const num = args[i];

    if (num > max1) {
      max2 = max1;
      max1 = num;
    } else if (num > max2 && num < max1) {
      max2 = num;
    }
  }

  console.log(max2);
}
