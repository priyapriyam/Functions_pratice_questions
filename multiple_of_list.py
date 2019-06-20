def multi_of_list(list):
    i=0
    multi=1
    while i<len(list):
        multi=multi*list[i]
        i=i+1
    return (multi)
     
list=[8, 2, 3, -1, 7]
print(multi_of_list(list))
