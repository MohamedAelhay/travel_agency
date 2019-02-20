from bs4 import BeautifulSoup
from abc import abstractmethod,ABC
import urllib.request
import random
import re

class Image_Crawler(ABC):
    def __init__(self):
        self.urls = []

    def crawl_page(self, url):
        with urllib.request.urlopen(url) as response:
            html = response.read()
            return BeautifulSoup(html,'html.parser')

    @abstractmethod
    def search(self, keyword):
        pass
    
    def get_random_url(self):
        if len(self.urls)>10:
            return self.urls[0 : 10 ][random.randint(0, 9)]
        elif(len(self.urls)>10):
            return self.urls[0]
        else:
            return "nothing was found"
        
    def get_urls(self, num_of_urls):
        if num_of_urls > len(self.urls):
            num_of_urls = len(self.urls)

        return self.urls[0 : num_of_urls]


class Gretty_Image_Crawler(Image_Crawler):
    def __init__(self, keyword):
        super().__init__()
        self.search(keyword)

    def search(self, keyword):
        self.urls = []
        url      = "https://www.gettyimages.com/photos/"+ keyword +"?alloweduse=availableforalluses&family=creative&license=rf&phrase=" + keyword + "&sort=best#license"
        crawler  = self.crawl_page(url)
        img_tags = crawler.findAll("a", {"class","search-result-asset-link"})
        for tag in img_tags:
            id = tag["data-asset-id"]
            self.urls.append("https://media.gettyimages.com/photos/picture-id" + id)

        return self.urls

class Yahoo_Image_Crawler(Image_Crawler):
    def __init__(self, keyword):
        super().__init__()
        self.search(keyword)

    def search(self, keyword):
        self.urls = []
        url      = "https://images.search.yahoo.com/search/images;_ylt=F;_ylc=X?&fr2=sb-top-images.search.yahoo.com&p=" + keyword
        crawler  = self.crawl_page(url)
        lis  = crawler.findAll("li",{"class":"ld"})
        for li in lis:
            a = li.find("a")
            href = a["href"]
            img_url = re.search(r'imgurl=(.*?)&rurl', href).group(1)
            img_url = img_url.replace("%2F", "/")
            self.urls.append(img_url)