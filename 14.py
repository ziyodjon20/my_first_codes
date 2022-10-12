# f = open("text.txt", "w")
# open = f.write()
# print(open)
try:
    f = open("text.html", "r")
    v = f.read()
    print(v)
except:
    g = open("notfound.html", "r")
    p = g.read()
    print(p)