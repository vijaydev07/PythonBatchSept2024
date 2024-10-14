#!/usr/bin/python3

"""
Purpose: check call by value for all other data types
 immutable: int, float, none,bool,str,frozenset
 mutable: list,set,dict
"""

def computation(int_val,float_val,bool_val,str_val,my_list,my_set,my_dict,my_frozenset):
    print(f'Inside method before change:\n'
          f'{int_val =}, {float_val =}, {bool_val =}, {str_val =}, {my_list =}, {my_set =}, {my_dict =}, {my_frozenset =}')
    
    int_val,float_val,bool_val,str_val = 20, 20.5,True,"Python3.0"
    my_list = [4,5,6]
    my_set = {10,20,30}
    my_dict = {'a': 1, 'b': 2}
    my_frozenset = frozenset([10,20,30])
    print(f'\nInside method after change:\n'
          f'{int_val =}, {float_val =}, {bool_val =}, {str_val =}, {my_list =}, {my_set =}, {my_dict =}, {my_frozenset =}')

int_val,float_val,bool_val,str_val = 10, 10.5,False,"Python"
my_list = [101,102]
my_set = {11,12}
my_dict = {'c': 10, 'd': 20}
my_frozenset = frozenset([1,2,3])
computation(int_val, float_val, bool_val, str_val, my_list, my_set, my_dict,my_frozenset)

print(f' \nOutside method after change \n'
          f'{int_val =}, {float_val =}, {bool_val=}, {str_val=}, {my_list =}, {my_set =}, {my_dict =}, {my_frozenset =}')