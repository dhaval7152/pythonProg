# Function On List
# 1.list_to_tuple.py
# weekDays=["sun","Mon","tue","wed","thu","fri","sat"]

# listToTuple=tuple(weekDays)
# print(listToTuple)
# ------------------------------------------------
#2. list_to_string
# weekDays=["sun","Mon","tue","wed","thu","fri","sat"]

# listAsString=','.join(weekDays).upper()
# print(listAsString)

# listFunctions.py

# ------------------------------------------------
# 3.list_to_set.py

# weekDays=["sun","Mon","tue","wed","thu","fri","sat"]

# listToset=set(weekDays)
# print(listToset)


# 4.) How to count the occurrences of a particular element in the list?

weekDays=["sun","Mon","tue","wed","sun","Mon","thu","fri","sat","Mon"]
# Using For loop
# cntr=0

# for value in  weekDays:
#     if 'Mon'==value:
#         cntr+=1
# print(f"The Mon Element is repeting: {cntr} Times")

# USing "count" function

# print(weekDays.count("Mon"))

# For Loop with Count function
# print([[x,weekDays.count(x)] for x in set(weekDays)])
