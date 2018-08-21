def vowels(voroodi):
    count = 0
    voroodi = voroodi.lower()
    vowels = ['a' , 'e' , 'i' , 'o' , 'u']
    for char in voroodi:
        if char in vowels:
            count = count + 1
    return count

voroodi = input("input a word: ")
print(vowels(voroodi))