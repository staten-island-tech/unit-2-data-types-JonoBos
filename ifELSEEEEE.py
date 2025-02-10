""" print ( 12 % 5) """
""" x = int(input("What is your number"))
if (x % 2)== 0:
    print("Your number is even")
else:
    print("Your number is odd") """

x = int(input("How much is your bill?"))
y = int(input("Would you like to tip 0%, 15%, 20%, or 25%?"))
if y == int(0):
    print ("Your bill comes out to:", int(x))
if y== int(15):
    print("Your bill comes out to:", round(float(x * 1.15)))
if y== int (20):
    print ("Your bill comes out to:", round(float(x * 1.2)))
if y == int(25):
    print ("Your bill comes out to:",round(float(x*1.25)))
    
""" a= int(input ("What is your number?"))
if a <= 0:
    print ("Your number must be greater than or equal to 1")
if a>= 1:
    print ("The factors of", a, "are", (a)) """
    
    
""" find_factors """


""" def find_factors(n):
    Returns a list of all factors of a given number n.
input ("What is you number?")    
if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    factors = [i for i in range(1, n + 1) if n % i == 0]
    return factors

# Example usage

print(f"Factors of {num}: {find_factors(num)}") """