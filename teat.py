
def list_sorting(lst1,lst2):
    new_list = []
    for i in range(len(lst1)):
        new_list.append((lst1[i],lst2[i]))
    ss = sorted(new_list, key=lambda employee: employee[0])
    ss = sorted(ss, key=lambda employee: employee[1],reverse=True)
    lst1_copy = []
    lst2_copy = []
    for i in ss:
        lst1_copy.append(i[0])
        lst2_copy.append(i[1])
    return lst1_copy, lst2_copy




# lst1 = ['tom','ali',  'sam','reza']
# lst2 = [34,10,40,34]


# lst1_copy, lst2_copy = list_sorting(lst1, lst2)
# print(lst1_copy)
# print(lst2_copy)


def append_list_new(data1, data2):
    new_list = data1.copy()
    new_list.extend(data2)
    return new_list

count = append_list_new([1, 2, 3, 4, 5], [1])
print(count)

count = append_list_new([1, 2, 1, 2, 1, 2], [2, 3, 4, 5])
print(count)
test_list = [10, 20, 30]
count = append_list_new(test_list, [1])
test_list[0] = 5
if count != [10, 20, 30, 1]:
    print("Your new list is still referencing old lists!")

# list of intgers
int_list = []

# sum of the list of intgers
def int_list_sum(list):
    return list.sum()

# average of the list of intgers
def int_list_avg(list):
    return list.sum()/len(list)

# return Maximum value of the list of intgers
def int_list_max(list):
    return list.max()
