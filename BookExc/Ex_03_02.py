while True:
    h=input("Enter hours:")
    try:
        H=float(h)
    except:
        print('Error, enter a number')
        continue
    r=input("Enter rate:")
    try:
        R=float(r)
    except:
        print('Error, enter a number')
        continue
    if H>40:
        S=40*R+((H-40)*R*1.5)
        print('Pay:', S)
    else:
        SS=40*R
        print('Pay:',SS)
