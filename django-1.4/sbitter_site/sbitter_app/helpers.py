import urllib2


def simple_func():
    return "Hello from helpers.simple_func()!"

def scrape(url):
    return urllib2.urlopen(url).read()
