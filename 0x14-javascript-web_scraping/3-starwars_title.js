#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as the first argument.');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  try {
    const data = JSON.parse(body);
    console.log(data.title);
  } catch (error) {
    console.error(error);
  }
});
