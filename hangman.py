def hangman(word):
    stages = ["-----------",
              "|    |     ",
              "|    O     ",
              "|   /|\    ",
              "|   / \    ",
              "|          ",
              "|          "
              ]
    print("ハングマンの世界へようこそ！")
    a = list(word)
    broad = ["_"]*len(word)
    print("今回の長さは{}".format(broad))
    win = False
    wrong = 0

    while wrong < len(stages):
        m = input("小文字を一つ入力してください：　")
        if m in a:
            index = word.index(m)
            broad[index] = m
            a[index] = "$"
        else:
            wrong += 1
        print("".join(broad))
        e = wrong + 1
        print("\n".join(stages[:e]))

        if "_" not in broad:
            print("君の勝ちだ！")
            win = True
            break

    if not win:
        print("君の負けだ！")
        print("正解は",word)

hangman("cat")

            

