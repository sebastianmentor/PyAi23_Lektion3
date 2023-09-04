list_of_lists= [[1,2,3],
                [4,5,[]],
                [7,8,9]]
print(list_of_lists)

value = list_of_lists[1][2] 
list_of_lists[1][2].append(6)

print(value)
print(list_of_lists)