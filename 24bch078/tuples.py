#6.1

def tuple1():

    l = [('boy1','boy2','boy3'),'girls1','girls2']

    print(l)

    b=0

    g=0

    for x in l:

        print(x)

        if isinstance(x,tuple):

            b+=len(x)

        else:

            g +=1

    print("no. of boys:",b)

    print("no. of girls:",g)

tuple1()

 

 

 

#6.2

students=[(1,"jay", 18),(2,"alia",20),(3,"shruti",19),(4,"john",21)]

roll_number =[]

names = []

age =[]

 

for student in students:

    roll_number.append (student[0])

    names.append(student[1])

    age.append(student[2])

 

print("roll numbers of the students:",roll_number)

print("name of the students:",names)

print("age of the students:",age)

 

 

 

#6.3

def q3():

    d1 = (14,5,23)

    d2 = (11,6,23)

    d = d2[0]-d1[0]

    m= (d2[1]-d1[1])*31

    y= (d2[2]- d1[2])*365

    no_of_days = d+ m+ y

    print(no_of_days)

 

q3()

 

 

 

#6.4

def tuple3():

    d1 =(21,3,2025)

    d2 = (4,2,2024)

    date1 = datetime.date(d1[2],d1[1],d1[0])

    date2 = datetime.date(d2[2],d2[1],d2[0])

    print(type(date1))

    print(abs(date1-date2))

 

tuple3()

 

 

 

#6.4

def q4():

    t1= [("maggi",20), ("paneer chilli", 50), ("cold coffee",70), ("cake", 450)]

    for x in t1:

        print(t1)

    print(sorted(t1))

    import operator

    print(sorted(t1,key = operator.itemgetter(1)))

 

q4()

 

#6.5

tuple_list=[(),(1,2),(),(3,4),("hello"),()]

filtered_list= [t for t in tuple_list if t]

print("list after removing the empty tuple:", filtered_list)

 

 

 

#6.6

def q6():

    t1 =('a','b','c','d')

    a = list(t1)

    a[2] = 2

    b = tuple(a)

    print(a)

q6()

 

 

 

#6.7

my_tuple = (1,2,3,4,5,6,7,8)

l = list(my_tuple)

l.pop(2)

print (l)

a = tuple(l)
