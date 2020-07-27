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

- Run this in shell in the main folder to install al dependencies from the requirements file.

> update and install this package first

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

