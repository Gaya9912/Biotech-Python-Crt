set={'python','c','c++','javascript','HTML','AngulaR js'}
print(set)
print(type(set))
print('python' in set)
set.add('jython')
print(set)
set.add('nodejs')
print(set)
set.update(['pypy','iron python'])
print(set)
set.remove('pypy')
print(set)
set.pop()
print(set)
set.discard('c')
print(set)
#set methods
set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))
#set intersection
print(set1 & set2)
#set difference
print(set1-set2)
#subset
a={3,4,5,6}
b={7,8,9,1}
isub=a.issubset(b)
print(isub)
isub=a.issuperset(b)
print(isub)