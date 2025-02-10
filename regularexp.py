#regex=group of strings if i  want to represent in a particular format or particlaur pattern . hnce search faster

#a+=one or more occurence of a
#a*=zero or more occurence of a
#a?=either there is or there isn't , binary 
#[abc]=either a either b either c
#[^abc]=except 
# [ab]*= eihter a or b , 0 or more times
#[a-z]*=a to z either 0 or more times
#\d=[0-9]=all digits
#\w=a[z] or [A-Z] = all alphabets small and capital both
#\d{3}=exaclty 3 number of digits
#\d{3,7}=minimum 3 number of digits and maximum 7 number of digits

#any string starts with your name and 

# import re 
# str="shreyansh7827 srivastava7843"
# patt="shreyansh"
# l=re.findall("\Ashreyansh\d{4}$",str)
# print(l)

#allowed characters are [A-G] or [a-z] or [0-9]
# first character should be lowercase
# second character should be digit divisble by 3
# length of the identifier  is alteast 2
# 

# import re
# import urllib.request
# str="a3427"
# test=["a3428", "a3429", "a3430", "a34"]
# patt=r"^[a-z][0369][a-z A-Z 0-9]*{4}$" 
# l=re.findall("[a-z][0369][a-zA-Z0-9]*{4}$",str)
# for string in test:
#     if re.match(patt,test):
#         print(f"valid : {string}")

#email validation = stat with small character, seond could be digit, atleast contain 2 digits"
# @,$,# should not be there and ends wirh .com

# # import re
# # patt = r"^[a-z][0-9]?[A-Za-z0-9]*[0-9][A-Za-z0-9]*[0-9][A-Za-z0-9]*\.com$"

# # emails = [
# #     "a3xyz12.com",   #  Valid
# #     "b6test99.com",  #  Valid
# #     "c0a45hello.com", #  Valid
# #     "A3hello12.com", #  Invalid (Starts with uppercase)
# #     "m7test.com",    #  Invalid (Only 1 digit)
# #     "p123@site.com", #  Invalid (@ is not allowed)
# #     "z0$hello99.com", #  Invalid ($ is not allowed)
# #     "testsite.com"   #  Invalid (No digits)
# # ]
# # for email in emails:
# #     if re.match(patt,email):
#         print("Valid")
#     else:
#         print("Invalid")

# import re,urllib
# import urllib
# u=urllib.request.URLopener("https://www.google.com")
# text=u.read()
# pat=r"[A-Z][A-Z]/d{2}[A-Z][A-Z]/d{4}"
# num=["UP32FB2504", "UP2FB250","UP32BB69"]
# for n  in num:
#     if re.match(pat,n):
#         print(f"Valid : ",{n})
#     else:
#         print(f"Invalid : ",{n})

# import re
# import urllib
# import ssl
# ctx=ssl.create_default_context()
# ctx.check_hostname=False
# ctx.verify_mode=ssl.CERT_NONE
# u=urllib.request.URLopener("https://www.redbus.in/info/contactus",co)
# text=u.reaad()
# number=re.findall("[0-9]{12}",text=str(text))
# for n in number:
#     print(n)

import re
l=[]
with open("endpoints.txt","r") as f:
    data=f.read()
    patt=r"^(https)://(fidelity)+//(rest)+//[v][0-9]./d{0}./d{0}$"
    match=re.findall(patt,data)
    for i in f:
        if match:
            list.append(i)
print(l)

