# # file=open("text1.txt", "w")
# # file.close()

# file=open("C:\Users\shrey\OneDrive\Desktop\Fidelity_2025_Interns\5_February_2025\text1.txt", "r")
# file.seek(0)
# c=file.readlines()
# print(c)
# #file.close()

# walk()
# create a folder f1 with file.txt
# create a another folder in f1 as f2 and create file.txt

# enter the path: example c://f1
# it should display all the folders in f1 
# can be done by using walk

# import os
# path=input("Enter path to the file : ")
# if os.path.exists(path):
#     print("\Folders inside :  ",path)
#     for root,dir,files in os.walk(path):
#         for dir_name in dir:
#             print(os.path.join(root,dir_name))
# else:
#     print("Invalid path! please use correct path")

#any file having endwith (eg .py, .txt, .java)
#it will only show those specific files ending with thoee exact etension
#  

# import os
# print(os.listdir("."))
# for dirpath,dir,file in os.walk("."):
#     for i in file:
#         if i.endswith(".py"):
#             print(i)
#         else:
#             print ("No such file.")

            

# import csv
# with open("data.csv","w",newline="") as f:
#     w=csv.writer(f)
#     w.writerow(["Eno","Ename","Salary"])
#     w.writerow(["111","Shreyansh","6969696"])
# print("CSV file created successdully.")

# with open("data.csv","w",newline="") as f:
#     w=csv.reader(f)
#     print(w)

# Serialization=coneverting into binary format

# d={}

#.dat is used for binary files
#dump helps to dump object in a file 
# pickle is a process where we convert the file types

# import pickle
# d=[10,30,56]
# file=open("lsit.dat","wb")
# '''wb is binary'''
# pickle.dump(d,file)
# file.close()
# l=pickle.load()
