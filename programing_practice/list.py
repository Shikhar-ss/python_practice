
# Goal: implement list data structure 
# objectives: 
#   1.  create class
#   2. methods: add, remove by index, lenght
#   3. Initialize the list (empty, with elements) 
# What does list do -> [] (not an array, since it has multiple data types)
# , index, elements, multiple data types, 

# create list class
class MyList:
    def __init__(self):
        self.list = []

    def add(self, element):
        self.list.append(element)
    
    def get(self, index):
        if(index < 0 or index >= len(self.list)):
            return print('Index out of range')
        return self.list[index]
    
    def length(self):
        return len(self.list)
    
    def pop(self,index):
        if (index < 0 or index >= len(self.list)):
            return None
        self.list.pop(index)
    
    def pop_delete(self,index):
        del self.list[index]
# create list attributes
# define parameters
# define list constructor 
# create list methods
# create list test cases
    


import timeit

my_list = MyList()
my_list.add(1)
my_list.add(3)
my_list.add(4)
my_list.pop(0)
# Comparing the time difference using del and pop for removing list item

#  timeit: default_timer is a wall clock timer.
# This means that it measures real time, not CPU time.
# then, timeit.timeit() will return the number of seconds it took to run the code in the first argument,
# timeit.default_timer() is a function that returns the current time in seconds.

# using .timeit() : { main statement, 
# setup ()which it imports the class/module and runs it in a seperate process), 
# # times to run the code:  to get accurate results}

pop_timer_setup = """
from __main__ import MyList
my_list = MyList()
my_list.add(3)
my_list.add(4)
"""
 
pop_statemnet = "my_list.pop(0)"

pop_timer = timeit.timeit(setup = pop_timer_setup, stmt=  "my_list.pop(0)", number = 1000000)

print('Time taken: ', pop_timer)
# print(my_list)
# print(my_list.get(1))