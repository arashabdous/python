n = int(input("tedad dict haye voroodi ra vared konid: "))
d = {}
#  یک دیکشنری ورودی بگیرد و مرتب کند
def sorted_dic(n , d):
    # تابع ورودی دیکشنری
    def a_input(n, d):
        for i in range(d):
            text = input("key and value ra ba yek space vared konid: ").split()
            n[text[0]] = text[1]
        return d

    a_input(n , d)
    n = list(n)
    n.sort()
    return n

print(sorted_dic(d , n))