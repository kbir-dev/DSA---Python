def makeBeautiful(str):
    t1 = 0
    t2 = 0
    s1 = '0'
    s2 = '1'
    for i in range(len(str)):
        if str[i] == "1":
            if s1 == "0":
                t1 += 1
            else:
                t2 += 1
        else:
            if s1 == "1":
                t1 += 1
            else:
                t2 += 1
        
        if s1 == "0":
            s1 = "1"
            s2 = "0"
        else:
            s1 = "0"
            s2 = "1"
    return min(t1,t2)
