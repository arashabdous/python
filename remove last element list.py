voroodi = input("yek list vared konid: ")
voroodi = voroodi.split()

def rem(voroodi):
    voroodi.pop()
    voroodi.pop(0)
    return voroodi
print(rem(voroodi))