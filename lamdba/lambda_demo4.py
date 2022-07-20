# lambda與 dict 字典數組應用
level_info = {
    10:lambda : print("perfect"),
    9:lambda : print("A"),
    8:lambda : print("B"),
    7:lambda : print("C"),
    6:lambda : print("D"),

}

if __name__ == '__main__':
    print(level_info)
    score = 45
    level = score // 10
    print(score,level, end=" ")
    level_info.get(level, lambda: print("E"))()