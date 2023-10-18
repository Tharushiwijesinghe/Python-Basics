#a set is an unordered collection of values that are changeable and does not allow duplicates
simple_set = {11,-2,'water',-2}
print(simple_set) 

#print(simple_set[1])
#above commented code is given error output that is unordered so there is no such notion as the index one location on this simple set

print('water' in simple_set)
#we can get output logical value of either true or false 

#can't change values but can add remove entries from a set
simple_set.add(72)
print(simple_set)
simple_set.remove('water')
print(simple_set)
