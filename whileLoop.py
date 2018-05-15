# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:24:20 2017

@author: Suharshith
"""

n=0
while n<5: 
    print(n)
    n=n+1
    

#for loop
    for n in range(10):
        print(n)
        
# in range of 
        mysum1=0
        for i in range(7, 10):
            mysum1 += i
        print(mysum1)
        
        mysum2=0
        for i in range(5, 11, 2):
            mysum2 += i
            if mysum2 == 5:
                break
            
        print(mysum2)
        
num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 

num = 10
while num > 3:
    num -= 1
    print(num)
    
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))

num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')

num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num)) 

n=2
for n in range (2,14,2):
    if n< 12 : print(n)
print("GoodBye!")


for n in range (2,14,2):
    while n< 12 : print(n)
print("GoodBye!")


print("Hello!")
n=12;
while n> 3:
    n=n-2;
    print(n)


num = 10
for num in range(5):
    print(num)
print(num)


divisor = 2
for num in range(0, 10, 2):
    print(num/divisor)


for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!') 
        
for letter in 'hola':
    print(letter) 
    
count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)

myStr = '6.00x'

for char in myStr:
    print(char)

print('done')

greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
    
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break
    
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    
count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    
    
    s="abcdefghiu"
    for index in range(len(s)):
        if s[index] == 'i' or s[index] == 'u':
            print("There is an i or u")
            
    s="abicdefghiu"     
    for char in s:
        if char == 'i' or char =='u':
            print("There is i or u")
            
    an_letters ="aefhilmnorsxAEFHILMNORSX"
    word = input("I will cheer for you! Enter a word:")
    times = int(input("Enthusiasm level (1-10):"))
    i=0;
    
    while i< len(word):
        char =word[i]
        if char in an_letters:
            print("Give me an " + char + "! " + char)
        else:
            print("Give me a" + char + "! " + char)
        i += 1
    print("What does that spell?")
    for i in range(times):
        print(word, "!!!")
               
        
  iteration = 0
  count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1           
        
    
    iteration = 0
    while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
    
    
    iteration = 0
    while iteration < 5:
        count = 0
        for letter in "hello, world":
            count += 1
            if iteration % 2 == 0:
                break
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        iteration += 1 