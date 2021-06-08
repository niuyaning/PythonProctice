import os
#列出目录下包括子目录的所有文件

for dirpath,dirames,filenames in os.walk("d:"):
    print('['+ dirpath+']')
    for filename in filenames:
        print(os.path.join(dirpath,filename))
