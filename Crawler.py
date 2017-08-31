import datetime
import Crawler
import time
import timeit
import urllib2

#print 'Input URL to Crawl:'
seed = 'http://cs101.udacity.com/urank' #Page where the crawl will begin

def union(a, b):
    for u in b:
        if u not in a:
            a.append(u)

def get_page(url):           #Get HTML as text for seed page
    return urllib2.urlopen(url).read()

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link) + 1
    end_quote = page.find('"', start_quote)
    url = page[start_quote:end_quote]
    return url, end_quote #returns url and second_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            if url not in links:
                links.append(url)
                page = page[endpos:]
        else:
            break
    return links

def add_to_index(index,keyword,url):
   for entry in index:
       if entry[0] == keyword:
           entry[1].append(url)
           return
   # not found, add new keyword to index
   index.append([keyword,[url]])

def add_page_to_index(index, url, content): 
    words = content.split() 
    for word in words: 
        add_to_index(index, word, url) 

def lookup(index, keyword):
   if keyword in index:
       return index[keyword]
   return None

def crawl_web(seed):
    to_crawl = seed
    crawled = []
    graph = {} # <url>, [list of pages it links to]
    index = {}
    while to_crawl:
        page = to_crawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(to_crawl, outlinks)
            crawled.append(page)
    return index, graph

def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10

    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[nodes] / len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks

def WhitneyRank():
    return

links = get_all_links(get_page(seed))
for link in links:
    print link