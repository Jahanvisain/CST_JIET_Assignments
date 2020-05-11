
def number(ar, n):
    result = ar[0]


    for i in range(1, n):
        result = result ^ ar[i]

    return result



ar = [3,3,4,5,4]

print("Element occuring once is",number(ar, len(ar)))

