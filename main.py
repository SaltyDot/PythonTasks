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

try:
    users_day = int(input("Enter the day of the week as a number: "))
    if users_day==1:
        print("Today is Monday")
    elif users_day==2:
        print("Today is Tuesday")
    elif users_day==3:
        print("Today is Wednesday")
    elif users_day==4:
        print("Today is Thursday")
    elif users_day==5:
        print("Today is Friday")
    elif users_day==6:
        print("Today is Saturday")
    elif users_day==7:
        print("Today is Sunday")
    else:
        raise Exception("Please enter a number from 1 to 7!")
except Exception as error:
    print(f"Error: {error}")

