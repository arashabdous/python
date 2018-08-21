voroodi = input("yek list vared konid: ")
voroodi = voroodi.split()

def tekrari(voroodi):
    output = []
    for item in voroodi:
        if item not in output:
            output.append(item)
    return output

print(tekrari(voroodi))