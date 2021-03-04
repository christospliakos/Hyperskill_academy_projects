import requests
from bs4 import BeautifulSoup
import string
import os


class WebScraper:
    
    def __init__(self, pages, article_type):
        self.url = "https://www.nature.com/nature/articles"
        self.pages = pages
        self.article_type = article_type
        self.r = None
        self.info = {"title": None, "description": None}
        self.articles = None
        self.articles_list = []
        
    def response_get(self):
        self.r = requests.get(self.url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    
    # This method makes sure that we get the right response from the HTTP handler, and calls the right methods.
    def response_analyze(self, n_):
        if self.r.status_code != 200:
            return f"The URL returned {self.r.status_code}!"
        else:
            soup = BeautifulSoup(self.r.content, 'html.parser')
            self.articles = soup.find_all('li', {"class": "app-article-list-row__item"})
            for article in self.articles:
                type = article.find("span", {"data-test": "article.type"}).text.strip('\n')
                if type == self.article_type:
                    article_url = "https://www.nature.com" + article.find('a')['href']
                    article_soup = BeautifulSoup(requests.get(article_url).content, 'html.parser')
                    body = self.body_finder(article_soup)
                    self.files_writing(article, body, n_)
                else:
                    pass
            return self.articles_list
        
    def body_finder(self, soup_element):
        try:
            return soup_element.find("div", {"class": "article__body cleared"}).text.strip()
        except AttributeError:
            return soup_element.find("div", {"class": "article-item__body"}).text.strip()
    
    # This method writes the article's body to a .txt file with the correct encoding.
    def files_writing(self, article_, body, n):
        title = article_.find('h3', {'itemprop': "name headline"}).text.strip('\n')
        title = title.translate(str.maketrans('', '', string.punctuation)).replace(" ", "_")
        with open(f"Page_{n + 1}/{title}.txt", 'wb') as f:
            f.write(str.encode(body))
        self.articles_list.append(title + '.txt')
    
    # Creates the directory when articles from each page get stored. The folder name is Page_N
    def directory_creation(self, n_):
        try:
            os.mkdir(f"Page_{n_ + 1}")
        except OSError:
            pass
        
    def main(self):
        for n in range(self.pages):
            self.url = f"https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page={n + 1}"
            self.directory_creation(n)
            self.response_get()
            self.response_analyze(n)
        return "Saved all articles."
    

quote = WebScraper(int(input()), input()).main()
print(quote)
