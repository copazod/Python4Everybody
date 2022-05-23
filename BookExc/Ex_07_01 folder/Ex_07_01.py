fname = input ('words.txt')
fh = open('words.txt')
for lx in fh:
    lx = lx.rstrip()
    lh = lx.upper()
    print (lh)

    
