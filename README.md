## Usage
Programs usage is fairly simple. First install all requirements in the requirements.txt file via `<pip install -r requirements.txt>`. Then just run the ipynb with e.g. jupyter notebook and let it finish, it may take a long time. Multithreading with 16 workers is implemented, but it took me ~32 hours for all reviews to load (~7s for each review).
The reviews get saved in a complete csv file (which is too big to upload on github) and 5 splitted csv files with each 100.000 reviews.

![Image of Yaktocat](https://seekvectorlogo.com/wp-content/uploads/2020/06/metacritic-vector-logo.png)

# Metacritic review scraper

This project was intended to extract reviews from a movie of metacritic.com. It now contains two sub projects which are used to perform requests without getting blocked.

1. The first subproject scrapes various user-agents.
2. The second subprojects scrapes proxy ip's. With them both it is easier to perform multiple requests to metacritic.

The program itself first scrapes from the browse page where all the movies are listed all the movie titles, then (after saving them to a file so this step can be skipped the next time), all movies itself are requested and every review given. So theoretically, all reviews given should be harvested.

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)
- [Team](#team)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)


## Installation

Clone and Setup the project as follows. If done, open the Jupyter notebook file and run it in order to start the scraping process.

### Clone

- Clone this repo to your local machine using `https://github.com/Mechamod/Metacritic-review-scraper

### Setup

- If you want more syntax highlighting, format your code like this:

> update and install this package first

```shell
$ brew update
$ brew install fvcproductions
```

> now install npm and bower packages

```shell
$ npm install
$ bower install
```

- For all the possible languages that support syntax highlithing on GitHub (which is basically all of them), refer <a href="https://github.com/github/linguist/blob/master/lib/linguist/languages.yml" target="_blank">here</a>.

---

## Features
## Usage (Optional)
## Documentation (Optional)
## Tests (Optional)

- Going into more detail on code and technologies used
- I utilized this nifty <a href="https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet" target="_blank">Markdown Cheatsheet</a> for this sample `README`.

---

## Support

Reach out to me at one of the following places!

- TODO 

---

## Donations (Optional)

- paypal.me/Mechamod


---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**

