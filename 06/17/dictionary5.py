alients = []
#创建 6个外星人
for alien_number in range(6):
    alient = {'name':'张三','age':15,'sex':'男'}
    alients.append(alient)
    print(alients)
#显示 前5个外星人
for alient in alients[:5]:
    print(alient)
#显示 创建了多少个外星人
print(f"一共创建了:{len(alients)}外星人")


for alient in alients[:3]:
    if alient['sex']== '男':
        alient['name'] ='李四'
        alient['age'] = 18,
        print(alients)
    elif alient['address']== '天津':
        alient['name'] = '王五'
        print(alients)


