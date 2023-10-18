#a list is an ordered and indexed collection of values that are changeable and allows duplicates
simple_list = ['Dan',2,3,4,'Python',2.71]
print(simple_list)
print(simple_list[0])
print(simple_list[3])
print(simple_list[-1])
print(simple_list[-2])
print(len(simple_list))

#it is easy to change entries of a list
simple_list[3] = 52
print(simple_list[3]) #index is based on 0
simple_list.append('to the back')
print(simple_list)
print(len(simple_list))
simple_list.pop(4)
print(simple_list)

#it is easy to initialize a list of a particular size with all entries the same
repeated_list = [5]*4
print(repeated_list)

#we can even use lists as entries of a list
simple_list[1] = [1,2,3]
print(simple_list)
print(simple_list[1])
print(simple_list[1][1])

#copying lists is a little tricky
list2 = simple_list
print(list2)
print(simple_list)
list2[1] = 0
print(list2)
print(simple_list)

#we must use the copy method to prevent this behaviour
list3 = simple_list.copy()
print(list3)
print(simple_list)
list3[0] = 'Mitchel'
print(list3)
print(simple_list)
