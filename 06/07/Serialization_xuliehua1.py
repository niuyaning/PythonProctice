import pickle

class Record:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone

r = pickle.dumps(Record)
print(r)
print(pickle.loads(r))

record = Record("张三","15010561875")
r = pickle.dumps(record)
print(r)
print(pickle.loads(r))