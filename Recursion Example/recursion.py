#Recursion is when a function calls itself from within the function

#Example-find the factoral of a number

#def fact(n):
 #   if n == 0:
  #      return 1
   # else:
        #keeps calling fact function as it steps down by 1
    #    return n * fact(n-1)


#print(fact(5))
#in example of 5, the fact function keeps iterrating over itself so you get 5 * 4 * 3 * 2 * 1

def traversedict(d):
    for key in d:
        if isinstance(d[key], dict):
            print('Found dict at', key)
            return traversedict(d[key])
        else:
            print('Unraveling')
            return d[key]

dictionary = {'films':{'genres':{'horror':[],'comedy':[]}}}
print(traversedict(dictionary))




