#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[1];
const fileContent = process.argv[2];

if (!filePath || !fileContent) {
  console.error('Please provide a file path as the first argument and a string to write as the second argument.');
  process.exit(1);
}

fs.writeFile(filePath, fileContent, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(fileContent);
  }
});
