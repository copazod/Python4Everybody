fname = input("romeo.txt")
fh = open("romeo.txt")
lst = list()


for line in fh:
#print(line.rstrip())
#w is a list when you split it
    w = line.split()
    #print(w)
    #print(len(w))
    for word in w:
        if word not in lst:
            lst.append(word)


print(sorted(lst))
