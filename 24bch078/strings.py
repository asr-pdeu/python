#3.1

def countvowels():

    str = input("ENTER THE STRING: ")

    print(str.count("a")+str.count("e")+str.count("i")+str.count("o")+str.count("u")+str.count("A")+str.count("E")+str.count("I")+str.count("O")+str.count("U"))

    c = 0

    for ch in str:

        if ch in "AEIOUaeiou":

            c += 1

        print(c)

countvowels()

 

 

#3.2(a)

def lower(str):

    newstr = ''

    for ch in str:

        if'A'<=ch<='Z':

          newstr += chr(ord(ch)+32)

        else:

              newstr += ch

    print(newstr)

s = input("ENTER THE STRING: ")

lower(s)

 

 

#3.2(b)

def upper(str):

    newstr = ''

    for ch in str:

        if'a'<=ch<='z':

          newstr += chr(ord(ch)-32)

        else:

              newstr += ch

    print(newstr)

s = input("ENTER THE STRING: ")

upper(s)

 

 

#3.2(c)

def toggle(str):

    newstr = ''

    for ch in str:

        if'A'<=ch<='Z':

          newstr += chr(ord(ch)+32)

        elif'a'<=ch<='z':

          newstr += chr(ord(ch)-32)

        else:

              newstr += ch

    print(newstr)

s = input("ENTER THE STRING: ")

toggle(s)

 

 

#3.3

def check():

    s1 = input("ENTER A STRING: ")

    s2 = input("ENTER THE 2nd STRING ")

    print(s2 in s1)

check()

 

 

#3.4

def remove():

    s1 = input("ENTER A STRING: ")

    s2 = input("ENTER THE 2nd STRING ")

    if s2 in s1:

        s1 = s1[:s1.find(s2)]+ s1[s1.find(s2)+len(s2):]

    print(s1)

remove()
