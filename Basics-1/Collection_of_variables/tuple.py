#a tuple is an ordered collection of values that are unchangeable and allows duplicates
simple_tuple = (12,42,11,99,2351)
print(simple_tuple)
print(simple_tuple[1])

#it is not possible to change entries in a touple
#simple_tuple[0] = 5 #cannot change value in a tuple

#we can around this through..
dummy = list(simple_tuple)
dummy[0] = 5
simple_tuple = tuple(dummy)
print(simple_tuple)
