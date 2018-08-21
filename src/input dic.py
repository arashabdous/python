def _input(n , d):
    # i = 0
    for i in range(n):
        text = input("key and value ra ba yek space vared konid: ").split()
        d[text[0]] = text[1]
    return d

n = int(input("tedad dict haye voroodi ra vared konid: "))
d = {}
print(_input(n , d))