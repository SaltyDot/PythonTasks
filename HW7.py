import math
import random
# 1st task
def caret(number, power):
    if power == 0:
        return 1
    else:
        return number * caret(number, power - 1)
num = caret(23, 0)
print(num)
# 2nd task
def stars(number):
    star = "*"
    if number >= 1:
        return star + stars(number - 1)
    else:
        return ""
print(stars(4))
# stars(4) -> star+stars(4-1)
# stars(3) -> star+stars(3-1)
# stars(2) -> star+stars(2-1)
# stars(1) -> star+stars(1-1)
# 0!>=1
# "*"+"*"+"*"+"*"
# 3rd task
def sum_of_num_in_range(number1, number2):
    if number1 > number2:
        if number1 - 1 == number2:
            return 0
        else:
            return number1 - 1 + sum_of_num_in_range(number1 - 1, number2)
    elif number2 > number1:
        if number2 - 1 == number1:
            return 0
        else:
            return number2 - 1 + sum_of_num_in_range(number1, number2 - 1)
    elif number2 == number1:
        return 0
sum = sum_of_num_in_range(19, 26)
print(sum)
# На базі прикладу вище
# sum=sum_of_num_in_range(19,26) -> 25+sum=sum_of_num_in_range(19,25)
# sum=sum_of_num_in_range(19,25) -> 24+sum=sum_of_num_in_range(19,24)
# sum=sum_of_num_in_range(19,24) -> 23+sum=sum_of_num_in_range(19,23)
# sum=sum_of_num_in_range(19,23) -> 22+sum=sum_of_num_in_range(19,22)
# sum=sum_of_num_in_range(19,22) -> 21+sum=sum_of_num_in_range(19,21)
# sum=sum_of_num_in_range(19,21) -> 20+sum=sum_of_num_in_range(19,20)
# sum=sum_of_num_in_range(19,20) -> 0
# 0+20+21+22+23+24+25
# 4th task
def find_position(list, a=0, b=10, minsum=math.inf, position=0):  # ¯\_(ツ)_/¯
    sum = 0
    if b != len(list):
        for i in range(a, b):
            sum += list[i]
    else:
        return position
    if sum < minsum:
        minsum = sum
        position = a
    return find_position(list, a + 1, b + 1, minsum, position)
list = [random.randint(1, 100) for b in range(100)]
print(list)
position = find_position(list)
print(position)