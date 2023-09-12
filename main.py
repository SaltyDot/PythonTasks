# try:
#     users_day = str(input("Enter the day of the week as a number: "))
#     if users_day.strip()=="1" or users_day.lower().strip()=="one" or users_day.lower().strip()=="first":
#         print("Today is Monday")
#     elif users_day.strip()=="2" or users_day.lower().strip()=="two" or users_day.lower().strip()=="second":
#         print("Today is Tuesday")
#     elif users_day.strip()=="3" or users_day.lower().strip()=="three" or users_day.lower().strip()=="third":
#         print("Today is Wednesday")
#     elif users_day.strip()=="4" or users_day.lower().strip()=="four" or users_day.lower().strip()=="fourth":
#         print("Today is Thursday")
#     elif users_day.strip()=="5" or users_day.lower().strip()=="five" or users_day.lower().strip()=="fifth":
#         print("Today is Friday")
#     elif users_day.strip()=="6" or users_day.lower().strip()=="six" or users_day.lower().strip()=="sixth":
#         print("Today is Saturday")
#     elif users_day.strip()=="7" or users_day.lower().strip()=="seven" or users_day.lower().strip()=="seventh":
#         print("Today is Sunday")
#     else:
#         print("Please enter a number from 1 to 7")
# except Exception as error:
#     print(f"Error: {error}")

# try:
#     users_day = int(input("Enter the day of the week as a number: "))
#     if users_day==1:
#         print("Today is Monday")
#     elif users_day==2:
#         print("Today is Tuesday")
#     elif users_day==3:
#         print("Today is Wednesday")
#     elif users_day==4:
#         print("Today is Thursday")
#     elif users_day==5:
#         print("Today is Friday")
#     elif users_day==6:
#         print("Today is Saturday")
#     elif users_day==7:
#         print("Today is Sunday")
#     else:
#         raise Exception("Please enter a number from 1 to 7!")
# except Exception as error:
#     print(f"Error: {error}")

#2nd task
try:
    #1st attempt
    # number1, number2 = input("Enter two numbers:"), input()
    # if number1.strip().isdigit() is False:
    #     raise Exception("First entry was not a number")
    # elif number2.strip().isdigit() is False:
    #     raise Exception("Second entry was not a number")
    #     не працює з від'ємними значеннями, не реалізував :(
    number1, number2 = int(input("Enter two numbers:")), int(input())
    if number1!=number2:
        # метод без мин\макс
        # if (number1)<=0 and (number2)<0:
        #     if (number1/number2)<=0:
        #         print(number2, number1)
        #     else:
        #         print(number1, number2)
        # elif number1<0 and number2==0:
        #     print(number1,number2)
        # elif number1>0 and number2<=0:
        #     print(number2, number1)
        # elif number2>0 and number1<=0:
        #     print(number1, number2)
        # elif number1>=0 and number2>=0:
        #     if number1-number2>0:
        #         print(number2,number1)
        #     else:
        #         print(number1,number2)
        print(min(number1,number2), " ", max(number1,number2))
        # а можно лист.сорт сделать если больше 2-х значений
    else:
        print(number1,number2) # вывод в случае одинаковых значений

except Exception as e:
    print(f"Error:{e}")

    #3rd task
try:
    number1,number2,operation= int(input("Enter the first number:")),int(input("Enter the 2nd-number:")), input("Enter"
    "the math operation you want to perform:")
    if operation=="-":
        print(number1-number2)
    elif operation=="+":
        print(number1+number2)
    elif operation=="*":
        print(number1*number2)
    elif operation=="/":
        if number2!=0:
            print(number1/number2)
        else:
            print("Can't divide by 0")
    else:
        print("Please enter a valid math operation, those being: +,-,* and / ")
except Exception as ee:
    print(f"Error:{ee}")