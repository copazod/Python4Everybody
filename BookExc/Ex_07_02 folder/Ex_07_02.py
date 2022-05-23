fname = input ('mbox-short.txt')
fh = open('mbox-short.txt')

ln =0
ad = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #print(line)
    else:
        ln = ln + 1
        s = line.find(':')
        x = float(line[19 : ])
        ad = ad + x
        #print(ad)
        #print(x)

#print (ln)
print('Average spam confidence:',ad/ln)
