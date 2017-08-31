import datetime #imports the datetime Python module

#Nanostick Calculation
speed_of_light = 299792458.0 #meters per second
cycles_per_second = 35000000000.0 # 3.5GHz
cycle_distance = speed_of_light / cycles_per_second
print 'Nanostick Distance: ' +  str(cycle_distance) + ' meters'
print'------------------------------------------------------\n'

#Age Calculation
date = datetime.date.today()
birthday = datetime.date(1986, 9, 5)
days_alive = date - birthday
print 'Days Alive: ' + str(days_alive)
print'------------------------------------------------------\n'

url
#Strings
name = 'Whitney'
print ('Hello ' + name + '! ') * 3
print name[0] + name[1] #Concatenates
print name[0+1] #Selects character position
print name[4:6] #Subsequence... will select 4 - 5, does not include character for last number in the subsequence
print name[:3]      #Beginning to number characters
print name[3:]      #Number characters to end

#Find in Strings
pythagoras = 'There is geometry in the humming of the strings, there is music in the spacing of the spheres. '
print pythagoras.find('string') #position of 'string'
print pythagoras.find('sphere') #position of 'sphere'
print pythagoras.find('is', 10) #position of 'is', after # position in string
print pythagoras[86:]
print pythagoras.find('derp')   #Error returned as -1 when word is not found
print'------------------------------------------------------\n'


name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

#Random Number
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
    guess = int(raw_input("Input your guess:"))
    guesses_left -= 1
    if guess == random_number:
        print 'You win!'
        print 'The number was', random_number
        break
else:
    print 'You lose!'
    print 'The number was', random_number

#Dictionaries and Lists
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

        # Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

        # Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

        # Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50

#For loops
hobbies = []

for i in range(3):
    hobbies.append(raw_input("Name a hobby: "))
print hobbies[0]
print hobbies[1]
print hobbies[2]

#Find Values in List
def find_element(list, value):
    index = 0
    for e in list:
        if e == value:
            return index
        index += 1
    """
    if e in list
        return list.index(e)
    """
    return -1


print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1

#Union
def union(a, b):
    for u in b:
        if u not in a:
            a.append(u)

#Time Execution
import time

def time_execution(code):
   start = time.clock()
   result = eval(code)  # evaluate any string as if it is a python command
   run_time = time.clock() - start
   return result, run_time

def spin_loop(n):
   i = 0
   while i < n:
       i = i + 1

print time_execution("spin_loop(10 ** 7)")

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

def hash_string(keyword,buckets):
    hash = 0
    for e in keyword:
        hash += ord(e) 
    return hash % buckets

def test_hash_function(func, keys, size):
   results = [0] * size  #this makes a list where all elements refer to same thing(0)
   keys_used = []
   for w in keys:
       if w not in keys_used:
           hv = func(w, size)
           results[hv] += 1
           keys_used.append(w)
   return results

def make_hastable(nbuckets):
    table = []
    for e in range(0, nbuckets):
        table.append([])
    return table

def hastable_get_bucket(htable,key):
    return htable[hash_string(key, len(htable))]

def hashtable_add(htable,key,value):
    # your code here
    hashtable_get_bucket(htable, key).append([key, value])

def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable, key)
    for e in bucket:
        if e[0] == key:
            return e[1]
    return None

def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for e in bucket:
        if e[0] == key:
            e[1] = value
            return htable
    bucket.append([key,value])
    return htable

#Recursion
def factorial(n): 
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#Palindromes
def is_palindrome(p):
    if p == '':
        return True
    else: 
        if p[0] == p[-1]:
            return is_palindrome(p[1:-1])
        else:
            return False

def iter_palindrome(s):
    for i in range(0, len(s) / 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fast_fibonacci(n):
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current + after
    return current

def popularity(t, p):
    if t == 0:
        return 1
    else:
        score = 0
        for f in friends(p):
            score = score + popularity(t - 1, f)
        return score