#
DATA = "daily-tests-per-thousand-people-smoothed-7-day-20200729.csv"


input_file = open(DATA, "r")
lines = input_file.readlines()
line_list=[]
for line in lines:
    l = line.strip()
    sep = l.split(",")
    line2 =[]
    temp_list = []
    found = False
    for j in sep:
        if(j.startswith('"')):
            temp_list.append(j)
            found = True
        else:
            if(found):
                temp_list.append(j)
                if(j.endswith('"')):
                    line2.append(",".join(temp_list))
                    found = False
                    temp_list = []
            else:
                line2.append(j)
    line_list.append(line2)

list1 = line_list[1:]

for i in range(5):
    liststr = ",".join(list1[i])
    print(liststr)
    res = [j for j in range(len(liststr)) if liststr.startswith('"', j)]
    liststr1 = liststr[res[0]+1:res[1]]
    liststr1 = liststr1.replace(",","")
    print(liststr1)