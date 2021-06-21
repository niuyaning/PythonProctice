

def make_album(songer,Album,songnum = None):
    #描述音乐专辑
    infor = {'song':songer,'album':Album}

    if songnum:
        infor['songno'] =songnum

    return infor


while True:
    s_songer = input("请输入歌手名称：")
    s_album = input("请输入销量：")

    s_info = make_album(s_songer,s_album)
    print(f"\nHello,{ s_info }")














