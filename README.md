Cycle "while"
==============
Reading data up to the stop value
---------------------------------
`````````````````ruby
word = input()
counter = 0
while word != 'стоп' and word != 'хватит' and word != 'достаточно':
    counter += 1
    word = input()
print(counter)
``````````````````````
`````````````````ruby
a = int(input())
counter = 0
while a >= 0:
    counter += a 
    a = int(input())
print(counter)
````````````````````````
