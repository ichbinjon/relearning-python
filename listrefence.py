#listreference.py
#assigning variable to existing list makes a list reference

christmas = ['bacon','eggs','gifts','santa']
breakfast = christmas
christmas[-1] = 'Hot Chocolate'
print(christmas)
print(breakfast) #notice how breakfast is also updated. This explains list references in python.
#The two variables are pointing to same place in memory.
#'is' command checks if they refer to same thing in memory

same = christmas is breakfast
print(same) #true

#copy makes a new copy of the list.
import copy
easter = copy.copy(christmas)
print()
print(christmas)
print(easter)
same = christmas is easter
print(same) #false 

#copy and deep copy http://stackoverflow.com/questions/17246693/what-exactly-is-the-difference-between-shallow-copy-deepcopy-and-normal-assignm
# essentially deepcopy is good for lists of lists cause if you just copy, there is a new outer list but the lists inside are just references.
