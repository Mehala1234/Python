pi=3.14
r=float(input("Enter radius:"))
Area=pi*r*r
print("Area of the circle",Area)

import os
split_tup=os.path.splitext('abc.py')
print(split_tup)
file_name=split_tup[0]
file_extension=split_tup[1]
print("File Extension:",file_extension)


