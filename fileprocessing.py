
# import pickle
# d=[] #empty dictionary
# with open("mydata.txt","r") as f:
#     for line in f:
#         if line[0]=="{" and line[-2]=="}" :    #checks for first and last character as opening and closing backets
#             obj=eval(line)  #this fails for sets
#             if isinstance(obj,dict):
#                 d.append(obj)
 
# with open("d1.pkl","wb") as f:
#     pickle.dump(d,f) #loads the data into pickle

# with open("d1.pkl", "rb") as f:
#     data = pickle.load(f)
#     print(data)  #prints the extracted dictionaries

