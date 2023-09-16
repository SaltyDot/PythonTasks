# 1st task
user_text=input("Enter whatever you want: ")
letters=0
numbers=0
for i in user_text:
    if i.isalpha():
        letters+=1
    elif i.isdigit():
        numbers+=1
print(f"Number of letters in the text:{letters}, Number count:{numbers} ")
# 2nd-task
user_text2=input("Please enter text: ")
ctrlF=input("Enter the character whose number you want to find in the text: ")
result=0
for i in user_text2:
    if i==ctrlF:
        result+=1
if result==0:
    print("None found")
else:
    print(f"This character is used {result} times in the text")
# 3rd-task

user_text3=input("Enter text: ")
OGword=input("Enter a word you want to replace: ")
NewWord=input("Enter the replacement: ")
user_text3=user_text3.replace(OGword, NewWord)
print(user_text3)

# 4th-task
user_test4 = input("Enter text: ")
print(user_test4[2])
print(user_test4[-2])
print(user_test4[:5])
print(user_test4[:len(user_test4)-2])
print(user_test4[::2])
print(user_test4[1::2])
print(user_test4[::-1])
print(user_test4[::-2])
print(len(user_test4))

