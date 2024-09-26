my_dict = {'Yaroslav': 2002, 'Anton': 2003, 'Andrey': 1997}
print(my_dict)
print(my_dict['Yaroslav'])
print(my_dict.get('Anna'))
my_dict.update({'Yarik': 2004,
                'Slava': 2008})
print(my_dict['Slava'])
del my_dict['Slava']
print(my_dict)
my_set = [1, 2, 3, 4, 1, 'apple', True]
my_set = set(my_set)
print(my_set)
print(my_set.add(5))
print(my_set.add('orange'))
print(my_set)
print(my_set.discard('apple'))
print(my_set)

