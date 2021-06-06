import pickle
'''
将列表写入 txt文件

'''
L = [1, 2, 3]
with open("d://1.txt","wb") as f:
    pickle.dump(L, f)
with open("d://1.txt", "rb") as f:
    print(pickle.load(f))

