h=input("Enter hours:")
r=input("Enter rate:")
H=float(h)
R=float(r)
if H>40:
    S=40*R+((H-40)*R*1.5)
    print('Pay:', S)
else:
    SS=40*R
    print('Pay:',SS)
