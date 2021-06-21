def car_information(color,tow_package,**infor):
    infor['color'] = color
    infor['tow_package'] = tow_package
    return infor

car = car_information(color='黄色',tow_package='hello',location= '北京')
print(car)