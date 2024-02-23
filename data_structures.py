#lists
#they are ordered and mutable
my_list = [1, 2, 3, 'hello', 5.0]
my_list.append(8)
print(my_list)

#tuples
#they are ordered but cannot be modified(immutable)
my_tuple = (1, 2, 'world', 3.14)
print(my_tuple)

#sets
#they are unordered and mutable
#they are unique elements
my_set = {1, 2, 3, 3, 4}
my_set.add(5)
print(my_set)

#dictionaries
#it is an unordered collection of elements using key_value pairs instead of index
my_dict = {
    'name': 'John',
    'age': 21,
    'city': 'Nairobi'
           }
my_dict['gender'] = 'Male'
print(my_dict)

#stacks
#a last in, first out (lifo) data structure
stack = []
stack.append(1)
stack.append(2)
print(stack)
print(stack.pop())

#queues
#a first in, first out (fifo) data structure
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)
print(queue.popleft())


#some other algorithms I've not included in here:
#heap
#linked lists
