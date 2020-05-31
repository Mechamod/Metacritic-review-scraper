# Metacritic-review-scraper
This project was intended to extract reviews from a movie of metacritic.com. It now contains two sub projects which are used to perform requests without getting blocked.

1. The first subproject scrapes various user-agents.
2. The second subprojects scrapes proxy ip's. With them both it is easier to perform multiple requests to metacritic.

The program itself first scrapes from the browse page where all the movies are listed all the movie titles, then (after saving them to a file so this step can be skipped the next time), all movies itself are requested and every review given. So theoretically, all reviews given should be harvested.

## Usage
Programs usage is fairly simple. First install all requirements in the requirements.txt file via `<pip install -r requirements.txt>`. Then just run the ipynb with e.g. jupyter notebook and let it finish, it may take a long time. Multithreading with 16 workers is implemented, but it took me ~32 hours for all reviews to load (~7s for each review).
The reviews get saved in a complete csv file (which is too big to upload on github) and 5 splitted csv files with each 100.000 reviews.
