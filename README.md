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
``````````````````ruby
a = int(input())
total = 0
while a >= 0 and a < 6:
    if a == 5:
        total += 1
    a = int(input())
        
print(total)
```````````````````````
``````````````````ruby
n = int(input())
max = 0
min = 9
while n != 0:
    n1 = n % 10
    if n1 < min:
        min = n1
    if n1 > max:
        max = n1
    n = n//10
print("The maximum number is", max)
print("The minimum number is", min)
```````````````````
```ruby
num = int(input())
last_digit = num % 10
same = True
while num != 0:
    num1 = num % 10
    if last_digit != num1:
        same = False
    num = num//10

if same == True:
        print("YES")
else:
     print("NO")
````
`````ruby
num = int(input())
digi = False
while num > 9:
    last = num % 10
    num1 = num % 100 //10
    if last <= num1:
        digi = True
    else:
        digi = False
        num = 0
    num = num // 10
if digi == True:
    print ("YES")
else:
    print ("NO")
`````
