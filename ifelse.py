""" def login (password):
    if password == "secret":
        print ("logged in")
    else:
        print ("incorrect")
x = input ("what da password")
login ("secrets") """

def grade(score):
    if score >=92:
        print("A")
    elif score >= 82:
        print ("B")
    elif score >= 72:
        print("C")
    else:
        print ("F")
score = input ("what da score")