#!/usr/bin/node

const request = require('request');

const movieId = process.argv[1];

if (!movieId) {
  console.error('Please provide a movie ID as the first argument.');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve data: ${response.statusCode}`);
    return;
  }

  const data = JSON.parse(body);

  console.log(`Title: ${data.title}`);
});
