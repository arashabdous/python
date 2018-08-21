def counter(voroodi ,z):
    count = 0
    voroodi = voroodi.lower()
    for char in voroodi:
        if char==z:
            count = count + 1
    return count


x = 0
voroodi = input("input a word: ")
z = input("input a letter: ")
x = counter(voroodi, z)
print(x)
