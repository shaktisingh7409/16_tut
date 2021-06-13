list1  = ["shakti", "deepak", "abhishek", "himanshu", "23",5,11,23,4,45,2,7,657]
for item in list1:
    if type(item) == int:
        if item > 6:
            print(item)