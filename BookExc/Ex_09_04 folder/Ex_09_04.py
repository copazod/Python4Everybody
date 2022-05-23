fname = input("Enter file:")
if len(fname) < 1 : fname = 'mbox-short.txt'

handle = open('mbox-short.txt')

counts = dict()


for line in handle:
    if line.startswith('From '):
        sender = line.split()

        name = sender[1]
        print(name)
        counts[name] = counts.get(name,0)+1

#print(counts)

mxcount = None
mxword = None

for name, counts in counts.items():
    if mxcount is None or counts>mxcount:
        mxword = name
        mxcount = counts
print(mxword,mxcount)
