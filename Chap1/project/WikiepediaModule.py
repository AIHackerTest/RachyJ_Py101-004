import wikipedia as wk
from bs4 import BeautifulSoup

def wiki():
    '''
    search anything in wikipedia
    '''

    word = input("Wikipedia search: ")
    results = wk.search(word)
    for i in enumerate(results):
        print(i)
    try:
        key = input("Enter the number: ")
    except AssertionError:
        key = input("WikipediaModule ")

    page = wk.page(results[key])
    url = page.url
    pageId = page.pageId
    title = page.title
    pageLength = input('''wiki page type: 1. Full 2. Summary: ''')

    if pageLength == 1:
        soup = fullPage(page)
        print(soup)

    else:
        print(title)
        print("Page ID= ", pageId)
        print(page.Summary)
        print("Page link =", url)

    pass

def fullPage(page):
    soup = BeautifulSoup(page.content, 'lxml')
    return soup

def randomWiki():

    '''
    This function gives you a list of n number of
    random articles
    choose any articles
    '''
    number=input("No: of Random Pages : ")
    lst=wk.random(number)
    for i in enumerate(lst):
        print(i)
    try:
        key=input("Enter the number : ")
        assert key>=0 and key<number
    except AssertionError:
        key=input("Please enter corresponding article number : ")

    page=wk.page(lst[key])
    url=page.url
    #originalTitle=page.original_title
    pageId=page.pageid
    #references=page.references
    title=page.title
    #soup=BeautifulSoup(page.content,'lxml')
    pageLength=input('''Wiki Page Type : 1.Full 2.Summary : ''')
    if pageLength==1:
        soup=fullPage(page)
        print(soup)
    else:
        print(title)
        print("Page Id = ",pageId)
        print(page.summary)
        print("Page Link = ",url)
    #print "References : ",references

    pass


def randomWiki():

    '''
    This function gives you a list of n number of
    random articles
    choose any articles
    '''
    number=input("No: of Random Pages : ")
    lst=wk.random(number)
    for i in enumerate(lst):
        print(i)
    try:
        key=input("Enter the number : ")
        assert key>=0 and key<number
    except AssertionError:
        key=input("Please enter corresponding article number : ")

    page=wk.page(lst[key])
    url=page.url
    #originalTitle=page.original_title
    pageId=page.pageid
    #references=page.references
    title=page.title
    #soup=BeautifulSoup(page.content,'lxml')
    pageLength=input('''Wiki Page Type : 1.Full 2.Summary : ''')
    if pageLength==1:
        soup=fullPage(page)
        print(soup)
    else:
        print(title)
        print("Page Id = ",pageId)
        print(page.summary)
        print("Page Link = ",url)
    #print "References : ",references


#randomWiki()
wiki()
