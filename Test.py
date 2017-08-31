#Make Index for Test
def add_to_index(index,keyword,url):
   for entry in index:
       if entry[0] == keyword:
           entry[1].append(url)
           return
   index.append([keyword,[url]])

def make_string(p):
   s=""
   for e in p:
       s = s + e
   return s

def make_big_index(size):
   index = []
   letters = ['a','a','a','a','a','a','a','a']
   while len(index) < size:
       word = make_string(letters)
       add_to_index(index, word, 'fake')
       for i in range(len(letters) - 1, 0, -1):
           if letters[i] < 'z':
               letters[i] = chr(ord(letters[i])+ 1)
               break
           else:
               letters[i] = 'a'
   return index

def add_to_index(index,keyword,url):
   for entry in index:
       if entry[0] == keyword:
           entry[1].append(url)
           return
   # not found, add new keyword to index
   index.append([keyword,[url]])

def lookup(index, keyword):
   for entry in index:
       if entry[0] == keyword:
           return entry[1]
   return None

def bad_hash_string (keyword, buckets):
   return ord(keyword[0]) % buckets # output is the bucket based on the first letter of the keyword

def hash_string(keyword,buckets):
    finnum = 0
    for e in keyword:
        finnum += ord(e) 
    return finnum % buckets

def make_hastable(nbuckets):
    table = []
    for e in range(0, nbuckets):
        table.append([])
    return table
    """
    i = 0
    while i < nbuckets:
        table.append([])
        i = i + 1
    """