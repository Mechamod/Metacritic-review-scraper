![Metacritic logo](https://seekvectorlogo.com/wp-content/uploads/2020/06/metacritic-vector-logo.png)

# Metacritic review scraper

This project was intended to extract reviews from a movie of metacritic.com. It now contains two sub projects which are used to perform requests without getting blocked.

1. The first subproject scrapes various user-agents.
2. The second subprojects scrapes proxy ip's. With them both it is easier to perform multiple requests to metacritic.

The program itself first scrapes from the browse page where all the movies are listed all the movie titles, then (after saving them to a file so this step can be skipped the next time), all movies itself are requested and every review given. So theoretically, all reviews given should be harvested.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [License](#license)


## Installation

Clone and Setup the project as follows. If done, open the Jupyter notebook file and run it in order to start the scraping process.

### Clone

- Clone this repo to your local machine using `https://github.com/Mechamod/Metacritic-review-scraper

### Setup

- Run this in shell in the main folder to install al dependencies from the requirements file.

```shell
$ pip -r requirements.txt
```

---

## Usage

Open the .ipynb in the main folder with jupyter notebook (or any other .ipynb editor) and press start.\
If scraping multiple times, it is possible to reuse the proxy list which gets generated, just comment out the corresponding cell. \
But be aware, proxies may change, so after sometime you need to rerun the cell to generate a more recent version of the proxyfile.

## Documentation 

See files for documentation.

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

