import re
#1st/2nd task
phone_number_list= ['2423423523','0442342343','047-123-123-3','048-123-12-12','+380-123-123-1','+380-632-12-12'
               ,"+38-093-233-34-23","380-93-234-23-23","093-234-23-23","0672342323" ]

for i in phone_number_list:
    if re.findall(r'^[+]?[3]{1}[8]{1}-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}$', i) and 10 <= len(i) <= 17:
        print(f"Mobile number: {i}")
    elif re.findall(r'^[0]{1}[4]{1}[0-9]{1}-[0-9]{3}-[0-9]{2}-[0-9]{2}$', i) and 10 <= len(i) <= 17:
        print(f"Landline number: {i}")
    elif re.findall(r'^[0]{1}[4]{1}[0-9]{8}', i):
        print(f"Landline number: {i}")
    elif re.findall(r'^[0]{1}[0-9]{2}[0-9]{7}', i):
        print(f"Mobile number: {i}")
    elif re.findall(r'^[0]{1}[0-9]{2}-[0-9]{3}-[0-9]{2}-[0-9]{2}', i):
        print(f"Mobile number: {i}")
    else:
        print("Invalid number")

#3nd task
data=["pojoki7032@hapincy.com","mavilar@icloud.com","nutsy424@zonnet.nl","asked234mail.com","pogish1!@gmail.com",
      "ewrfwergferf@fadfdsf","asdsfsfd!!@1111.kr","cloudfare.@mail@.com"]
regex=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}$"
for email in data:
    if re.findall(regex,email):
        print(email)
    else:
        print("Invalid email")

#4th task
regex=r"^[A-ZА-ЯЁЇІҐЄ]{1}[a-zа-яёїієґ]{2,10}\s[A-ZА-ЯЁЇІҐЄ]{1}[a-zа-яёїієґ]{2,10}\s[A-ZА-ЯЁЇІҐЄ]{1}[a-zа-яёїієґ]{2,10}$"
name_sample=["Amani Mays Lev", "Autumn May","Autumn May february","Jazmin Vaughan, Hart","Mateo Levy"]
for i in name_sample:
        if re.findall(regex,i):
            print(i)
        else:
            print("Invalid name")
