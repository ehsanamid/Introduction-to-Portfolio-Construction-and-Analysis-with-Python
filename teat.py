
from traceback import print_tb


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

# count = append_list_new([1, 2, 3, 4, 5], [1])
# print(count)

# count = append_list_new([1, 2, 1, 2, 1, 2], [2, 3, 4, 5])
# print(count)
# test_list = [10, 20, 30]
# count = append_list_new(test_list, [1])
# test_list[0] = 5
# if count != [10, 20, 30, 1]:
#     print("Your new list is still referencing old lists!")



def get_name(name_dict, id_num):
    if id_num in name_dict:
        return name_dict[id_num]
    else:
        return None

# test_dictionary = {11:'Fred', 2001:'Agnes'}
# ans = get_name(test_dictionary, 2001)
# print(ans)

# test_dictionary = {11:'Fred', 2001:'Agnes'}
# ans = get_name(test_dictionary, 10)
# print(ans)

def word_counter(input_str):
    out_dict = {}
    for i in input_str.split():
        if i.lower() in out_dict:
            out_dict[i.lower()] += 1
        else:
            out_dict[i.lower()] = 1
    return out_dict

# word_count_dict = word_counter("This is a sentence")
# items = word_count_dict.items()
# sorted_items = sorted(items)
# print(sorted_items)
  

# word_count_dict = word_counter("A WORD is a word it is")
# items = word_count_dict.items()
# sorted_items = sorted(items)
# print(sorted_items)

def find_key(input_dict, value):
    for key, val in input_dict.items():
        if val == value:
            return key
    return None

# test_dictionary = {100:'a', 20:'b', 3:'c', 400:'d'}
# print(find_key(test_dictionary, 'b'))

# test_dictionary = {100:'a', 20:'b', 3:'c', 400:'d'}
# print(find_key(test_dictionary, 'e'))

def make_index(words_on_page):
    out_dict = {}
    for key, val in words_on_page.items():
        for s in val:
            if s in out_dict:
                out_dict[s].append(key)
            else:
                out_dict[s] = [key]
    return out_dict

# input_dict = {
#    1: ['hi', 'there', 'fred'], 
#    2: ['there', 'we', 'go'],
#    3: ['fred', 'was', 'there']}
# output_dict = make_index(input_dict)
# for word in sorted(output_dict.keys()):
#     print(word + ': ' + str(output_dict[word]))

def make_dictionary(filename):
   with open(filename, 'r') as f:
       out_dict = {}
       for s in f:
            s_lower = s.lower().strip()
            if(s_lower != ''):
                if s_lower in out_dict:
                    
                    out_dict[s_lower] += 1
                else:
                    out_dict[s_lower] = 1
       return out_dict

# dictionary = make_dictionary('.\lab8_object_files\data3.txt')
# for key in sorted(dictionary.keys()):
#     print(key + ': ' + str(dictionary[key]))
   

def isbn_dictionary(filename):
    try:
        f = open(filename, 'r')  
        out_dict = {}
        for s in f:
            sep = s.strip().split(",")
            out_dict[sep[2]] = (sep[0], sep[1])
        return out_dict
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return
   
        

# your_dict = isbn_dictionary(".\\lab8_object_files\\books.csv")
# if your_dict != None:
#     for isbn in sorted(your_dict.keys()):
#         print(isbn + ':', your_dict[isbn])

# your_dict = isbn_dictionary('.\\lab8_object_files\\loads_of_books.csv')
# if your_dict != None:
#     for isbn in sorted(your_dict.keys()):
#         print(isbn + ':', your_dict[isbn])

def long_enough(strings, min_length):
    out_list = []
    for s in strings:
        if len(s) >= min_length:
            out_list.append(s)
    return out_list

# strings = ['a', 'bc', 'def', 'ghij', 'klmno']
# print(long_enough(strings, 3))

def my_enumerate(items) :
    out_list = []
    index = 0
    for item in items:
        out_list.append((index,item))
        index += 1
    return out_list

# ans = my_enumerate([10, 20, 30])
# print(ans)

def run_length_encode(data):
    out_list = []
    length  = 1
    for i in range(len(data)):
        if i == len(data) - 1:
            out_list.append((data[i], length ))
        elif data[i] == data[i+1]:
            length  += 1
        else:
            out_list.append((data[i], length ))
            length  = 1
    return out_list

# data = [5, 5, 5, 10, 10]
# print(run_length_encode(data))

# data = [10, 20, 30, 30, 30, 30]
# print(run_length_encode(data))

def isPrime(i):
    if i == 1:
        return False
    for j in range(2, i//2+1):
        if i % j == 0:
            return False
    return True

def  composite2(N):
    count = 0
    i = 4
    while True:
        is_prime = True
        for j in range(2, i//2+1):
            if i % j == 0:
                is_prime = False
                break
        
        if(not is_prime and i % 2 != 0):
            count += 1
        if count == N:
            return i  
        i +=1     
        
# print(composite2(3))

def series(x):
    sum = 0
    i = 0
    term = 2 ** i
    # sum += term
    while term >= x:
        sum += term
        i += 1
        term = 1/2 ** i
    return round(sum,4)

# print(series(0.5))
# print(series(0.25))
# print(series(0.05))
# print(series(0.01))
# print(series(0.001))

def nextRound(k,scores):
    count_next_round = 0
    for score in scores:
        if score >= scores[k-1] and score > 0:
            count_next_round += 1
    return count_next_round

# print(nextRound(5,[10,9,8,7,6,6,6,5,4]))

# print(nextRound(2,[0,0,0,0]))

def singleDigit(N):
    n_str = str(N)
    while len(n_str) > 1:
        sum = 0
        for i in n_str:
            sum += int(i)
        n_str = str(sum)
    return int(n_str)

# print(singleDigit(48))

# print(singleDigit(198))

def sequence(n):
    out_list = []
    out_list.append(n)
    while(n > 1):
        if(n%2 == 0):
            n = n//2
        else:
            n = 3*n+1
        out_list.append(n)
    return out_list


address = "amid.ehsan@gmail.com"
def splitEmailAddress(Address):  
    sp1 = Address.split("@")
    ret = []
    for s in sp1:
        sp2 = s.split(".")
        ret += sp2
    return ret
# s = splitEmailAddress(address)
# print(s)   
 
p = '/Users/michaelw/CITS1401/exam.doc'
def basename(P):
    sp = P.split("/")
    ret = sp[-1].split(".")
    return ret[0]

# print(basename(p))

def manhat(x,y):
    sum = 0
    for i in range(len(x)):
        sum += abs(x[i]-y[i])
    return sum

# print(manhat([1,3,5,7],[1,9,25,42]))

import os as os
f = "D:\\Projects\\CITS1401\\Project_2\\Sample.txt"

def retpath(f):
    if os.path.exists(f):
        return[c for c in open(f,'r').read().split('\n') if c != '']

def retpath1(f):
    if os.path.exists(f):
        ret = []
        strings = open(f,'r').read().split('\n')
        for s in strings:
            if s != '':
                ret.append(s)
        return ret

# print(retpath(f))
# print(retpath1(f))

def ft6b():
    ng = {}
    ng[(1,2,4)] = 5
    ng[(4,2,1)] = 10
    ng[(1,2)] = 12

    try:
        sum = 1
        for k in ng:
            sum *= ng[k]
        ng.append(sum)
        print("try")
    except:
        print("except")
    print(ng,'Sum=',sum)

# ft6b()

def merge(list1,list2):
    out_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            out_list.append(list1[i])
            i += 1
        else:
            out_list.append(list2[j])
            j += 1
    if i < len(list1):
        out_list += list1[i:]
    if j < len(list2):
        out_list += list2[j:]
    return out_list

# print(merge([1,3,5,11,12],[2,4,6,8]))

def mk(D):
    ret = {}
    for key,value in D.items():
        if value < 50:
            ret["N"] = ret.get("N",0) + 1
        elif value < 60:  
            ret["P"] = ret.get("P",0) + 1
        elif value < 70: 
            ret["Cr"] = ret.get("Cr",0) + 1
        elif value < 80: 
            ret["D"] = ret.get("D",0) + 1
        else:
            ret["HD"] = ret.get("HD",0) + 1
    return ret

# print(mk({"Fred":55, "James":67, "Jemima":71}))

def rec_pow(x,N):
    if N== 0:
        return 1
    val = rec_pow(x,N//2)
    if(N%2 == 0):
        return val*val
    return val*val*x

print(rec_pow(3,1001))