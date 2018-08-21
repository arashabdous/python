def counter(voroodi ,z):
    count = 0
    voroodi_split = voroodi.lower().split()
    z = z.lower()
    for string in voroodi_split:
        if string[0] == z:
            count= count + 1
    return count

x = 0
voroodi = input("input a word: ")
z = input("input a letter: ")
x = counter(voroodi, z)
print(x)
