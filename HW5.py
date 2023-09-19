import random
#1st-task
print(random.randint(-100,100,))
num_size=20
numbers=[]
negativesum=0
sum=0
oddsum=0
multi3=1
sum2=0
for i in range(num_size):
    numbers.append(random.randint(0,50)-25)
print(numbers)
for i in range(num_size):
    if numbers[i]<=0:
        negativesum+=numbers[i]
print(f"Sum of negative numbers in the list: {negativesum}")
for i in range(num_size):
    if numbers[i]%2==0:
        sum+=numbers[i]
    else:
        oddsum+=numbers[i]
print(f"Sum of odd numbers in the list: {oddsum}\nSum of even numbers in the list: {sum}")
for i in range(num_size):
    if numbers[i]!=0:
        if numbers[i]%3==0:
            multi3=multi3*numbers[i]
print(f'Product of numbers that can be divided by 3 without a remainder: {multi3}')
print(f"Product of the largest and the smallest number in the list: {min(numbers)*max(numbers)}")
for i in range(1,len(numbers)-1):
    sum2+=numbers[i]
print(f"Sum of numbers in the list with the exception of the first and the last number: {sum2}")
#2nd-task
even=[]
odd=[]
negative=[]
positive=[]
for i in range(num_size):
    if numbers[i]%2==0:
        even.append(numbers[i])
    else:
        odd.append(numbers[i])
for i in range(num_size):
    if numbers[i]>=0:
        positive.append(numbers[i])
    else:
        negative.append(numbers[i])
print(f"List of: \nPositive numbers: {positive}\nNegative numbers: {negative}\nEven numbers: {even}\nOdd numbers: {odd}")

