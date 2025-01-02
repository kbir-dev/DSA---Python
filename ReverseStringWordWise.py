def reverseStringWordWise(string):
    # write your code logic !!!
    l1 = list(string.split())
    n = int(len(l1)/2)
    start = 0
    end = -1
    for i in range(n):
        temp = l1[start]
        l1[start] = l1[end]
        l1[end] = temp
        start += 1
        end -= 1
    string = " ".join(l1)
    return string
