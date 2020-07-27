def get_random_user_agent(list_of_user_agents):
    """
    Returns a dictionary containing all necessary header information for a
    request, with a random chosen user agent to bypass being detected
    when scraping.

    Parameters
    ----------------
    list_of_user_agents : list
        A list containing various user agents.

    Returns
    ----------------
    dictionary
        Returns a dictionary of header fields with a random user agent for
        evasion.
    """

    headers = {"Host": "www.metacritic.com",
               "User-Agent": random.choice(list_of_user_agents),
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Accept-Language": "en-US,en;q=0.5",
               "Accept-Encoding": "gzip, deflate",
               "Connection": "keep-alive"}

    return headers


def get_random_proxy(list_of_proxies):
    """
    Returns a dictionary with a random proxy chosen from the given list.

    Parameters
    ----------------
    list_of_proxies : list
        A list containing various proxies.

    Returns
    ----------------
    dictionary
        Returns a dictionary with a random proxy which uses the http protocol.
    """
    random_proxy = "http://" + str(random.choice(list_of_proxies))
    proxy_dict = {"http"  : random_proxy}

    return proxy_dict

def scrape_movie_reviews(movie_links, user_agents_table, proxy_table):
    """
    Harvests all review from all given movie links.
    
    Parameters
    ----------------
    movie_links : list
        A list of movie links to the movies from metacritic.
        
    user_agents_table : Pandas DataFrame
        A pandas dataframe containing various user agents
        to use for the requests.
        
    proxy_table : Pandas DataFrame
        A pandas dataframe containing various proxies to
        use for the requests.
        
    Returns
    ----------------
    review_informations : list
        Returns a list containing the reviews as a list
        so that each review is an own list.
    """
    skipped = 0
    review_informations = []
        
    for movie_link in tqdm(movie_links):
        print("Processing link: ", movie_link)
        movie_review_link = movie_link + "/user-reviews?page="
        page_number = 0

        while True:
            page = requests.get(movie_review_link + str(page_number),
                                headers=get_random_user_agent(user_agents_table),
                                proxies=get_random_proxy(proxy_table))
            soup = BeautifulSoup(page.content, 'lxml')

            if "No reviews yet." in str(soup) or len(soup.find_all("div", class_="review pad_top1")) == 0:
                print(f"Scraped {len(review_informations)} reviews!")
                break
            page_number += 1

            movie_name = get_movie_name(soup)
            reviews = soup.find_all("div", class_="review pad_top1")
            for review in reviews:
                try:
                    rating = get_rating(review).replace(';',',')
                    username = get_username(review).replace(';',',')
                    date = get_date(review).replace(';',',')
                    review_text = get_review_text(review).replace(';',',')
                    thumbs_up = get_thumbs_up(review).replace(';',',')
                    thumbs_total = get_thumbs_total(review).replace(';',',')
                    review_information = [movie_name,
                                          movie_link,
                                          rating,
                                          username,
                                          date,
                                          review_text,
                                          thumbs_up,
                                          thumbs_total]
                    review_informations.append(review_information)
                except:
                    skipped += 1
                
    print("Skipped: ", skipped)
        
    return review_informations
    
def get_movie_name(soup):
    """
    Gets the movie name given.
    
    Parameters
    ----------------
    review : BeutifulSoup object
        The review from metacritic as a BeautifulSoup object.
        
    Returns
    ----------------
    movie_name : string
        Returns the movie_name of the review as a string.
        If it cant be extracted it returns a empty string instead.
    """
    try:
        film_name = soup.find("div", class_="product_page_title upper pad_top2 pad_btm_half oswald").findChildren()[0].text
        if len(film_name) != 0:
            return film_name
        else:
            return ""
    except:
        return ""
            
    
def get_rating(review):
    """
    Gets the rating of the review.
    
    Parameters
    ----------------
    review : BeutifulSoup object
        The review from metacritic as a BeautifulSoup object.
        
    Returns
    ----------------
    rating : string
        Returns the rating as a string.
        If the review doesn't got rated yet, the returned string is empty.
    """
    try:
        METASCORE_CLASSES = ["metascore_w user large movie positive indiv perfect",
                             "metascore_w user large movie positive indiv",
                             "metascore_w user large movie mixed indiv",
                             "metascore_w user large movie negative indiv", ""]

        rating = review.find("div", class_=METASCORE_CLASSES).text
        if len(rating) != 0:
            return rating
        else:
            return ""
    except:
        return ""
    
def get_username(review):
    """
    Gets the username of the review creator.
    
    Parameters
    ----------------
    review : BeutifulSoup object
        The review from metacritic as a BeautifulSoup object.
        
    Returns
    ----------------
    username : string
        Returns the username of the review creator.
        If the username cant get extracted, the returned string is empty.
    """
    try:
        username = review.find("span", class_="author").text
        if len(username) != 0:
            return username
        else:
            return ""
    except:
        return ""
    
def get_date(review):
    """
    Gets the date when the review got created.
    
    Parameters
    ----------------
    review : BeutifulSoup object
        The review from metacritic as a BeautifulSoup object.
        
    Returns
    ----------------
    date : string
        Returns the date of the review as a string.
        If the date cant get found, an empty string is returned.
    """
    try:
        date = review.find("span", class_="date").text
        if len(date) != 0:
            return date
        else:
            return ""
    except:
        return ""
    
def get_review_text(review):
    """
    Gets the text of the review itself. If there is a expand tag,
    it automatically harvests the expanded version of the text.
    
    Parameters
    ----------------
    review : BeutifulSoup object
        The review from metacritic as a BeautifulSoup object.
        
    Returns
    ----------------
    review_text : string
        Returns the review text. If it cant be found it returns
        an empty string.
    """
    try:
        review_tag = review.find("div", class_="review_body").findChildren()[0]
        if len(review_tag.findChildren()) == 4:
            review_text = review_tag.findChildren()[1].text
        else:
            review_text = review_tag.text
        if len(review_text) != 0:
            return review_text
        else:
            return ""
    except:
        return ""
    
def get_thumbs_up(review):
    """
    Gets the total thumbs up given.
    
    Parameters
    ----------------
    review : BeutifulSoup object
        The review from metacritic as a BeautifulSoup object.
        
    Returns
    ----------------
    thumbs_up : string
        Returns the number of total thumbs up given as a string.
        If the review doesn't got rated yet, the returned string is empty.
    """
    try:
        thumbs_up = review.find("span", class_="yes_count").text
        if len(thumbs_up) != 0:
            return thumbs_up
        else:
            return ""
    except:
        return ""
    
def get_thumbs_total(review):
    """
    Gets the total thumbs given.
    
    Parameters
    ----------------
    review : BeutifulSoup object
        The review from metacritic as a BeautifulSoup object.
        
    Returns
    ----------------
    thumbs_total : string
        Returns the number of total thumbs given as a string.
        If the review doesn't got rated yet, the returned string is empty.
    """
    try:
        thumbs_total = review.find("span", class_="total_count").text
        if len(thumbs_total) != 0:
            return thumbs_total
        else:
            return ""
    except:
        return ""

def scrape_movie_list(link, user_agents, proxies):
    """
    Harvests all the movie links from the movie browse site of metacritic.
    
    Parameters
    ----------------
    link : string
        The link to the index site of metacritic. 
        The page number must be removed beforehand!
        
    user_agents : dictionary
        Dictionaries containing various headers for the
        requests to not get detected too fast and banned.
        
    proxies : dictionary
        Dictionary containing the request method and the
        proxy to use for the request.
        
    Returns
    -----------------
    movie_links : list
        List of links to the various movies scraped.
    """
    movie_links = []
    page_number = 0
    
    while True:
        page = requests.get(link + str(page_number),
                            headers=get_random_user_agent(user_agents),
                            proxies=get_random_proxy(proxies))
        soup = BeautifulSoup(page.content, 'lxml')

        if "No movies found." in str(soup):
            print(f"Scraped {len(movie_links)} movie links")
            break

        movie_tags = soup.find_all("a", class_="title")
        for movie_tag in movie_tags:
            movie_links.append(base_url + str(movie_tag["href"]))
        page_number += 1
        
    return movie_links

def save_lines(list_of_lines, output):
    """
    Saves a list of elements to the given output path.
    Where each element of the list has it's own line.
    
    Parameters
    ----------------
    list_of_lines : list
        List containing elements (preferably strings)
        which get written.
        
    output : string
        Path to the file which shall get created.
    """
    file = open(output, "a")
    for line in list_of_lines:
        file.write(str(line) + "\n")
    file.close
    
def read_lines(input_file):
    """
    Reads every line in a file into a list.
    
    Parameters
    ----------------
    input_file : string
        String to the path of the file which shall get read into a list.
        
    Returns
    ----------------
    movie_links : list
        A list where each element is a line of the file.
    """
    with open(input_file) as f:
        movie_links = f.read().splitlines()
        return movie_links

def save_reviews_to_csv(list_of_reviews, output):
    """
    Saves a list of reviews to the given output path.
    Where each reviews of the list has it's own line.
    
    Parameters
    ----------------
    list_of_reviews : list
        List containing reviews, that are itself lists,
        containing information about an review.
        
    output : string
        Path to the file which shall get created.
    """
    df = pd.DataFrame(list_of_reviews,
                      columns =["Movie",
                                "Link",
                                "Rating",
                                "Username",
                                "Date",
                                "Review_text",
                                "Thumbs_up",
                                "Thumbs_total"])
    df.to_csv(output, sep=";", index=False)
