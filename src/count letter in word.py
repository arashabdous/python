def count_letter (voroodi):
    voroodi_str = voroodi.replace("" , "")
    voroodi_lower = voroodi_str.lower()
    max_count = 0
    sample_char = None

    for charachter in voroodi_lower:
        count = voroodi_lower.count(charachter)
        if count >= max_count:
            max_count = count
            sample_char = charachter
    return sample_char

x = input("input a string: ")
print(count_letter(x))
