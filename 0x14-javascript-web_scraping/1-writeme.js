#!/usr/bin/node


const fs = require('fs');

function writeToFile(filePath, content) {
  // Encode the content as UTF-8 before writing
  const contentUtf8 = Buffer.from(content, 'utf-8');

  fs.writeFile(filePath, contentUtf8, (err) => {
    if (err) {
      console.error(err);
    } else {
      console.log(content);
    }
  });
}

// Check if called directly with arguments
if (process.argv.length !== 3) {
  console.error("Usage: node script.js <filepath> <string>");
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

writeToFile(filePath, content);
