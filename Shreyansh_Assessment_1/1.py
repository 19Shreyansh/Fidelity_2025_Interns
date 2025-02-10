'''Name = Shreyansh Srivastava'''
'''Questions = 1,4,7,8,10'''
'''Email Address = shreyanshsri19@gmail.com'''



employee=[
    {'id':1,'name':'AAA','role': 'CEO','hra': 5000,'da': 2000},
    {'id':2,'name':'BBB','role': 'CTO','hra': 4000,'da': 1800},
    {'id':3,'name':'CCC','role': 'CFO','hra': 3000,'da': 1600},
    {'id':4,'name':'DDD','role': 'CDO','hra': 2000,'da': 1400},
    {'id':5,'name':'EEE','role': 'Intern','hra': 1000,'da': 1200}
    ]

for emp in employee:
    emp['total salary']=emp['hra']+emp['da']

with open("employee.txt","w") as f: #creating a file for writing
    f.write("Employee Details :-\n\n")
    for emp in employee:
        f.write(f"ID : {emp['id']}\n")
        f.write(f"Name : {emp['name']}\n")
        f.write(f"Role : {emp['role']}\n")
        f.write(f"HRA : {emp['hra']}\n")
        f.write(f"DA : {emp['da']}\n")
        f.write(f"Total Salary : {emp['total salary']}\n\n")
