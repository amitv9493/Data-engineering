num = 121
divider = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


for i in range(10):
    result = num / divider[i]
    print("This is the formatted value of {:.2f}".format(result))
