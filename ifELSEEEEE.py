""" print ( 12 % 5) """
""" x = int(input("What is your number"))
if (x % 2)== 0:
    print("Your number is even")
else:
    print("Your number is odd") """

""" x = int(input("How much is your bill?"))
y = int(input("Would you like to tip 0%, 15%, 20%, or 25%?"))
if y == int(0):
    print ("Your bill comes out to:", int(x))
if y== int(15):
    print("Your bill comes out to:", round(float(x * 1.15)))
if y== int (20):
    print ("Your bill comes out to:", round(float(x * 1.2)))
if y == int(25):
    print ("Your bill comes out to:",round(float(x*1.25))) """
    
a= int(input ("What is your number?"))
if a <= 0:
    print ("Your number must be greater than or equal to 1")
if a>= 1:
    print ("The factors of", a, "are", find_factors(a))
    
    
    """ find_factors """