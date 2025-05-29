# 0x06. Star Wars API

This project is part of the **ALX Interview Preparation Curriculum**. It demonstrates how to interact with an API using Node.js and the `request` module to retrieve and process data from the [Star Wars API (SWAPI)](https://swapi-api.alx-tools.com/).

## Task 0: Star Wars Characters

### Description

Write a script that prints all characters of a specified Star Wars movie.

### Requirements

- The first positional argument passed is the **Movie ID** (example: `3` = “Return of the Jedi”).
- Display one character name per line in the **same order** as listed in the `characters` array of the `/films/` endpoint.
- You **must use the Star Wars API**: `https://swapi-api.alx-tools.com/api/films/<movie_id>`
- You **must use the `request` module** for HTTP requests.

### Example

```bash
alexa@ubuntu:~/0x06$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/0x06$
```

### Usage

```bash
./0-starwars_characters.js <movie_id>
```

### Dependencies

Install the `request` module if not already installed:

```bash
npm install request
```

### File

- `0-starwars_characters.js`

### Repository Structure

```
alx-interview/
└── 0x06-starwars_api/
    ├── 0-starwars_characters.js
    └── README.md
```
