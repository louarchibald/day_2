# 1. Create an empty list called `task_list`

# 2. Add a few `str` elements, representing some everyday tasks e.g. 'Make Dinner'

# 3. Print out `task_list`

# 4. Remove the last task

# 5. Print out `task_list`

# 6. Print out the number of elements in `task_list`

task_list = []

task_list.append('Have shower', 'Brush teeth', 'Make lunch', 'Read book')
print(task_list)

task_list.pop(3)
print(task_list)

num_of_elements = len(task_list)
print(num_of_elements)

