def distance(str1,str2):
    difference = 0
    length = len(str1)
    for index in range(length):
        if str1[index] != str2[index]:
            difference += 1
    return difference