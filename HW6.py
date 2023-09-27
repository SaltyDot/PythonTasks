import random
#1st task
def multi(list):
    base=1
    for i in range (len(list)):
        base*=list[i]
    return list
#2nd task
def minimum():
    return min(list)
#3rd task
def simple_number_count(list):
    count=0
    for i in range(len(list)):
        if list[i]>1:
            if list[i]==2 or list[i]==3:
                count+=1
            elif list[i]%2==0 or list[i]%3==0:
                continue
            else:
                count+=1
        else:
            continue
    return count
def simple_number_count_v2(list):
    count=0
    for i in range(len(list)):
        if list[i]>1:
            if list[i] == 2 or list[i] == 3:
                count += 1
            else:
                for x in range(2, list[i]):
                    if list[i]%x==0:
                        break
                    else:
                        count+=1
    return count
#4th task
def removed_number_count(list, number):
    count=0
    for i in range(len(list)):
        i-=count
        if list[i]==number:
            count+=1
            list.remove(list[i])
    # print (list)
    return count
# list=[random.randint(1,10) for b in range(10)]
# print(list)
# wut=removed_number_count(list, 8)
# print(wut)
#5th task Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.
def idk_how_to_name_this(list1,list2):
    combo=[]
    count=0
    copy1 = list1.copy()
    copy2 = list2.copy()
    for i in range(len(copy1)):
        i-=count
        for ii in range(len(copy2)):
            if copy1[i]==copy2[ii]:
                combo.append(copy1[i])
                count+=1
                copy1.remove(copy1[i])
                copy2.remove(copy2[ii])
                break
    # print(copy1,copy2)
    return combo
# list1=[random.randint(1,10) for b in range(4)]
# list2=[random.randint(1,10) for b in range(9)]
# print(list1)
# print(list2)
# wut=idk_how_to_name_this(list1,list2)
# print( wut)
#6th task
def list_to_the_power_of(list, carat):
    newlist=[]
    for i in range(len(list)):
        newnum=list[i]**carat
        newlist.append(newnum)
    return newlist
####






