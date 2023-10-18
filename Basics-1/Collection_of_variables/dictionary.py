#a dictionary is a collection of values that are unordered (but indexed) and changeable
simple_dict = {
    "brand": "Apple",
    "product": "iphone",
    "model": "X"
}

print(simple_dict)

print('I bought an', simple_dict['product'], 'model', simple_dict['model'], 'from', simple_dict['brand'])
simple_dict["model"] = "11 pro"
print('I bought an',simple_dict['product'],"model",simple_dict['model'],'from',simple_dict['brand'])

#we can also add entries to the dictionary
simple_dict['color'] = 'red'
print('I bought an',simple_dict['color'],simple_dict['product'],"model",simple_dict['model'],'from',simple_dict['brand'])
