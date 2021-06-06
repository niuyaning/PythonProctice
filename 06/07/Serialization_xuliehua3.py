import pickle

class Record:
    def __init__(self,name,phone_number):
        self.name = name
        self.phone_number = phone_number

record = Record("牛亚宁",'15010561875')

with open("d:/2.txt","wb") as f:
    print(pickle.dump(Record,f))
with open("d:/2.txt","rb") as f:
    print(pickle.load(f))
