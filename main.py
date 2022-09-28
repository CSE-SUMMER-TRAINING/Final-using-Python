from data_input import *
from college import *
from display import *
from groups_input import *
# import sys

# build Tree of College
for i in range(num_of_branches):
    branch.append(Branch(branch_name[i], i, num_of_builds[i]))

get_and_store_groups()

DISPLAY()

def printCollege(branch :Branch)->None:
    for hall in branch.hallsInBranch: 
        print(f"{hall.name} {hall.volume}")
    print()
    for g in branch.groupsInBranch:
        print(f"{group[g].name} {group[g].volume}")

# with open('output.txt', 'w', encoding = 'utf-16') as fout:
#     sys.stdout = fout
