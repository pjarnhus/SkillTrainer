import bs4
import io_funcs
import re
import requests

class WebItem:
    def __init__(self, url):
        self.url = url
        try:
            self.webpage = requests.get(self.url, timeout = 5)
            if self.webpage.status_code == 200:
                self.succeeded = True
                self.content = bs4.BeautifulSoup(self.webpage.content,
                                                 'html.parser')
            else:
                self.succeeded = False
        except:
            self.succeeded = False


    def get_title(self):
        if not self.succeeded:
            return None
        return (self
                .content
                .find('title')
                .text
                .replace("'", " ")
                .replace('"', ' ')
               )


    def get_suggested_topics(self, n_max=10):
        topics = io_funcs.get_all_topics()
        body = self.content.find('body').text
        word_pattern = re.compile(r'\w+')
        unique_words = set(word_pattern.findall(body.lower()))
        found_topics = [topic for topic in topics
                        if all([topic_word.lower() in unique_words
                                for topic_word in
                                word_pattern.findall(topic)])]
        return found_topics[:n_max]
