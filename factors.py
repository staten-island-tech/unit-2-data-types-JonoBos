""" x= int(input ("What is your number?"))
for i in range (1, x+1):
    if x%i ==0:
        print (i) """

cfl = []

x= int(input ("What is your number?"))
y = int(input ("What is your second number"))
for i in range (1, x+1):
    for i in range (1,y+1):
        if x%i ==0 and y%i==0:
                cfl.insert (i+1, i)
print(max(cfl))



        




