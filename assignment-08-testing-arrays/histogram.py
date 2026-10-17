# takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT
# Ruth-ann Rudolph RDLRUT001
# 20/04/2023

mark_list = input("Enter a space-separated list of marks:\n")
mark_Array = mark_list.split() #splits the marks entered into an array of marks
fail = 0 #holds the number of marks which constitue a fail
third = 0 #holds the number of marks which constitue a "third" category
lower_second = 0 #holds the number of marks which constitue a "lower_second" category
upper_second = 0 #holds the number of marks which constitue a "upper_second" category
first = 0 #holds the number of marks which constitue a "first" category

for i in range(0,len(mark_Array)):
    """loops through all the marks in the array and adds one to the category in which the mark falls"""
    evaluate = eval(mark_Array[i]) #takes the current mark out of the array and put it into a number form for evaluating
    if evaluate < 50:
        fail = fail +1
    elif (evaluate >= 50) and (evaluate < 60):
        third = third +1
    elif (evaluate >= 60) and (evaluate < 70):
        lower_second = lower_second + 1
    elif (evaluate >= 70) and (evaluate < 75):
        upper_second = upper_second + 1
    elif evaluate >= 75:
        first = first + 1

#creates the histogram shape from the values found in the for loop
print("1 |"+ ("X"*first))
print("2+|"+ ("X"*upper_second))
print("2-|"+ ("X"*lower_second))
print("3 |"+ ("X"*third))
print("F |"+ ("X"*fail))