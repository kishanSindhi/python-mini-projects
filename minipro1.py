#author - Kishan Sindhi
#date - 29-5-2021
#discription - its a simple python mini project named as "mid lib genrator"
#in this the user have to guess the correct ans and fill it in the blank
#Each blank contains one mark

print("You have to fill the correct answer in the story\n")
que = '''
One day in ____(1) I saw my ___(2) acting ___(3). She was ___(4) a big ___(5) then she went 
to ___(6) and hide it.
'''
print(que)
m1 = 0
m2 = 0
m3 = 0
m4 = 0
m5 = 0
m6 = 0
b1 = "petlad"
b2 = "mom"
b3 = "wierd"
b4 = "hiding"
b5 = "box"
b6 = "bedroom"

i1 = input("fill in the blank no1\n")
i2 = input("fill in the blank no2\n")
i3 = input("fill in the blank no3\n")
i4 = input("fill in the blank no4\n")
i5 = input("fill in the blank no5\n")
i6 = input("fill in the blank no6\n")

if b1 == i1:
    m1 = m1+1
else:
    pass

if b2 == i2:
    m2 = m2+1
else:
    pass

if b3 == i3:
    m3 = m3+1
else:
    pass

if b4 == i4:
    m4 = m4+1
else:
    pass

if b5 == i5:
    m5 = m5+1
else:
    pass

if b6 == i6:
    m6 = m6+1
else:
    pass

marks = m1+m2+m3+m4+m5+m6
print(f'''\nOne day in "{i1}" I saw my "{i2}" acting "{i3}". She was "{i4}" a big "{i5}" 
then she went to "{i6}" and hide it.\n''')
print("And the real answer key is...\n")
print(f'''One day in "petlad" I saw my "mom" acting "wierd". She was "hiding" a big "box" 
then she went to "bedroom" and hide it.\n''')
print(f"So, You got {marks}")
