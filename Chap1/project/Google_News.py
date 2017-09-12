import bs4
# Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def news():
    # specify the url of Google News RSS
    # my_url = "https://news.google.com/news/rss/?ned=us&hl=en"
    my_url = "http://www.dynamsoft.com/blog/feed/"
    # open the url and assign it to Client
    Client = urlopen(my_url)

    # read the page content to xml_page
    xml_page = Client.read()
    # close it
    Client.close()

    # extract content as xml
    soup_page = soup(xml_page,"xml")
    news_list = soup_page.findAll("item")

    for news in news_list:
        print(news.title.text)
        print(news.link.text)
        print(news.pubDate.text)
        print("-"*150)

    # What was the below line for?
    #n = input()

news()
