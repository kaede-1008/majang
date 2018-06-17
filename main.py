def main():
    man=[1, 2, 3, 4, 5, 6, 7, 8, 9]      #マンズ
    sou=[1, 2, 3, 4, 5, 6, 7, 8, 9]      #ソウズ
    pin=[1, 2, 3, 4, 5, 6, 7, 8, 9]      #ピンズ
    figure=[1, 2, 3, 4, 5, 6, 7]   #字牌, 東,南,西,北,白,発,中

    ##手牌の入力

    print("手牌(上がり牌以外の13牌)を入力してください.")
    while(True):
        print("マンズ(例: 123456789)")
        rise_man = input()
        print("これでいいですか？", rise_man)
        print("Yes:1 No:2")
        confirm=input()
        if (confirm == '1'):
            break
    
    while(True):
        print("ソウズ(例: 123456789)")
        rise_sou = input()
        print("これでいいですか？", rise_sou)
        print("Yes:1 No:2")
        confirm=input()
        if (confirm == '1'):
            break

    while(True):
        print("ピンズ(例: 123456789)")
        rise_pin = input()
        print("これでいいですか？", rise_pin)
        print("Yes:1 No:2")
        confirm=input()
        if (confirm == '1'):
            break
    
    while(True):
        print("字牌(例: 1234567)")
        rise_figure = input()
        print("これでいいですか？", rise_figure)
        print("Yes:1 No:2")
        confirm=input()
        if (confirm == '1'):
            break

    ## 上がり牌の入力

    while (True):
        print("1:ツモ 2:ロン")
        rise_way=input()
        if (rise_way == '1' or rise_way == '2'):
            break
    

if __name__ == '__main__':
    main()