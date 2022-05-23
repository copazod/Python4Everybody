
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open('mbox-short.txt')

counts = dict()

for line in handle:

    if line.startswith('From '):

        hora = line.split()
        h = hora[5]
        hfin = h.split(':')
        hrf = hfin[0]

        counts[hrf] = counts.get(hrf,0)+1

lst = list()
for k,v in sorted(counts.items()):
    print (k,v)
