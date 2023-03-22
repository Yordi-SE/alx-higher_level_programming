#!/usr/bin/node
for (let i = 2; ; i += 1) {
  if (process.argv[i]) {
    console.log(process.argv[i]);
  } else if (i === 2) {
    console.log('No argument');
    break;
  } else {
    break;
  }
}
