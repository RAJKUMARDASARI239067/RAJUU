# ! --------> COMMON FUNCTIONS FOR LIST


 lst1  = [6, 7, 8, 9, 0]
  print(len(lst1))


  print(max(lst1))
   print(min(lst1))


 l1 = [6, 8, 9, "p","u"]
 print(max(lst1)) # --> error coz its a combination of hint and string
 print(min(lst1)) # --->error coz its a combination of hint and string

  l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
   print(min(lst1)) # -5


   l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
   index() --> to get index value of specicific element
   print(l1.index(9))

   l1 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
   count() --> how many number of times an element is repeated
   print(l1.count(6))
   # ! some functions which is specially used for list

    To add element inside list
    ? insert (index_value, element)---> to adfd element at specific index position
   l1 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
l1. insert (2,"cars")
   print(l1)


# ? To delent element from list
  l1 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
  pop() ---> last element will be deleted
  l1.pop()---> last element will be deleted
  l1.pop()
  print(l1)



# *pop(index_value)--> used to delete element at specific index
  l1.pop(4) #  4 is index value
  print(l1)

# remove(element) ---> used to list delete element directly
  l1. remove(8)
  print(l1)


#* clear() ---> to delete all element in list
 l1. clear()
 print(l1)


del---> to delete the list
del l1 # or del(l1)
 print(l1)

#  ? ----> join 2 list
 l1 = [9, 0, 8]
 121 = ("p","o","t",34)
 print(11+12)



# ! 0r

extent()-----> to cobine 2 list
l1. extent(12)
print(11)


# ! ----> copy

11 = [6, 7, 8, 9, 3]
12 = 11. copy()
print(12)
print(11)

print(id(11))
print(id(l2)) 



# ! diff b/w shallow copy and deep copy
 shallow copy
 import copy
 l1 = [8, 9, 0, [5, 6],[3, 2, 1]]
 l2 = copy.copy(l1)
 l1.append(890)
 print(l1)
  print(l2)


# * deep copy ---> used to copt the list with nested list
 import copy
 l1 = [8, 9, 0, [5, 6],[3, 2, 1]]
 print(l1[-1][1]) --> to index nested list
 l2 =copy. deepcopy(l1)
 l1.append(cars)
 print(l1)
  print(l2)



# ? sort --> arrange elements in list assending or descending order
 l1 = [9,7, 45, 0 -6, 5, 12]
 11.sort() to arrange in assending order\
  print(11)

 l1. sort(reverse=True) # to soret in desending order
  print(l1)

# l1 = ['z', 'i', 'o', 'p',9]
 l1.sort()
 print(11) #  ---> error



# ? list constructor
# * list() --> to convert other collection datatype to list
# l3 = ((8, 9, 0))
# print(list(13))

# l4 = (8, 9)
# print(list(4))


# ! ---> nested list

  l1 = [8, 9, [0, 8, 7], ["p", "o", 'y'], [8,'t']]
  print(l1[-2][1]) # --> 0


  print(l1[1:4])
  print(l1(1:-1))

# ? top delete "t" from l1
 l1[-1].remove('t')
 print(l1)

# ? combine these ["p","o",'y'], [8,'t'] lists in l1  ["p","o",'y'], [8,'t']
 l1[-2].extend(l1[-1])
 l1.pop(-1)
 print(l1)


# ! ------> Tuple
# *char of tuple


# 1.) Tuple have to be surrounded by()
# 2.)The elements inside tuple are not changable
# 3.)The elements inside tuple are indexed
# 4.) The elements will execute in order
# 5.) It is heterogenous
# 6.)It allow duplicate elements


# eg:
# t1 = (8, 8, 9, 6, 5.78, [9,0],(6,8),"hey",9+6j)
# print(t1)
# print(type(t1))


# ? indexing slicing all same as list



# ? ways to create couple
 l1 = (8)
 print(type(l1)) # int
 

  l1 = (8,)
 print(type(l1)) # int

 t1 = 8,9
 print(type(t1))# tuple
 

  t2 = 8,
 print(type(t2)) # tuple


# len(),min(),max(),index(),count()---->all same as list



# to add element inside tuple ---> cannot add
  cannot delete any element from tuple


# * join 2 tuples
 t1 = (8, 9, 0)
 t2 = (6, 7, 8)
 print(t1+t2)


# * To all element inside list and tuple
  sum()
  l1 = (8, 9, 7, 6)
  print(sum(l1))


# * sort tuplke
 t1 =(8, 9, 0, 89, 12)
 print(tuple(sorted(t1))
 print(tuple(sorted(t1, reverse= True)))


# * Iterate list and tuples

 l1 = [9,8, 0, 6, 5]
 for i in l1:
     print(i)


# * Iterate based on index value
 l1 = [9,8, 0, 6,5,8, 56]
 for i in range(0,len(l1)):
       print(l1[i])


# ! ------> String

 s1 = 'o'
 print(type(s1))

 s1 = "u"
  print(type(s1))
     
       
 s1 = "hello world"
  * To access string
 print(s1)
  indexing and slicing ---> same as list and tuple
 print(s1[0:5])
       

# ---> common functions

# len(),min(),max(),index(),count()
    s1 = "hello world"
    print(len(s1))
     print(max(s1))
     print(min(s1))

# ord()------>used top find the ASCII value oif a charecter
     s1 = 'u'
     print(ord(s1))

# ! Functions of string
 s1 = "hello world"

# ? to convert all charecters to upper case
# print(s1.upper())

# ? to convert to lower case
    s1 = "HFREDGiou"
       print(s1.lower())

# ? strip()----> to eliminate the space in beggining and end of string
    s1 = "Where are you?"
       print(s1.lstrip())
       print(s1.rstrip())
       print(s1.lstrip())


# ! spilt()--->
  s1 = "Where are you?"
  print(s1.split())     
   print(s1.split("r"))     

   print(s1.count('e'))   

# * Print the string in revese manner
   s1 = "Welcome to all"
   print(s1[::-1)]

# ! -----> Eg:1
# Wap to find the number of lower case letters
  s1 = "hey there you are"



# ! --------> Eg:3


 s1 =  Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsue', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
 s2 = s1.strip()

 characters = len(s1)
 print(len(words))

 space = 0
  for val in s1:
       if val ==" ":
           space=space+1
 print(space)      


       

















        
                

 
 

 
