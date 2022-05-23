s=None
l=None
while True:
    n=input('enter number:')
    if n == 'done':
       break
    try:
        nn = int (n)
    except:
        print("no invalid")
        continue

    if s is None and l is None :
        s = nn
        l = nn
    if nn < s:
        s=nn
    elif nn > l:
        l=nn
print ('max:',l)
print ('min:',s)
