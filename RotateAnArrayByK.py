def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    for i in range(0,k):
        arr.append(arr.pop(0))
        
    return arr

    pass