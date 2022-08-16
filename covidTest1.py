from nose.tools import assert_equal, assert_raises, raises


DATA = "daily-tests-per-thousand-people-smoothed-7-day-20200729.csv"


def clean (data_row):
    data_rowlst=[]

    data_rowlst.append(data_row)
  

    list1=[]
    for i in data_rowlst:
        line = i.split("/n")
        line2 =[]
        for j in line:
            j1 = j.strip()
            line2.append(j1)
        list1.append(line2)
    listhead1 = "".join(list1[0])
    final = []
    final.append(listhead1[:49])
    
    for i in range(1,len(list1),1):
        liststr = "".join(list1[i])
        res = [j for j in range(len(liststr)) if liststr.startswith('"', j)]
        date = liststr[int(res[0])+1:int(res[1])].replace(",","")
        final.append(liststr[:res[0]-1] +","+ date + liststr[res[1]+1:])
    final2 = "/n".join(final)
    return final2

DATA = "daily-tests-per-thousand-people-smoothed-7-day-20200729.csv"
with open(DATA,'r') as file:
    print(clean(file.readline()))

DATA = "daily-tests-per-thousand-people-smoothed-7-day-20200729.csv"
with open(DATA,'r') as file:
    for line  in file:
        # assert_equal(clean(file.readline()), "Entity,Code,Date,Daily tests per thousand people ")
        print(clean(line))
        # assert_equal(clean(file.readline()), "Argentina,ARG,Feb 18 2020,0")
assert_raises(ValueError, clean, 'text"moretext')

print("So far, so good on the practice tests. Remember there will be additional tests applied. You should test your code to ensure it meets the specification.")
