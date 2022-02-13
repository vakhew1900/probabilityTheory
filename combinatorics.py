def P(a):
    num = 1
    try:
        x = int(a)
        for i in range(1, a + 1):
            num*=i
        return num
    except:
        print("error")