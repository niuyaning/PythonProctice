def sandwich(size,**infor):
    infor['size'] = size
    return infor

sand = sandwich(
    12,
    color='yellow',
)
sand1 = sandwich(
    12,
    color='yellow',
    delicious = '美味的'
)
sand2 = sandwich(
    12,
    color='yellow',
    price = 100
)
print(sand,sand1,sand2)