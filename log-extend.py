#I wanted to extend the definition of the logarithm log base a of b
#Instead of an extended piecewise definition, I decided to make an all in one equation that uses complex numbers

# log          (c + di) = ln(c+di)/ln(a + bi) = (ln|r1|*ln|r2|+theta1*theta2)/(ln^2|r1|+theta1^2) + i*(theta2*ln|r1| - theta1*ln|r2|)/(ln^2|r1|+theta1^2)
#     (a + bi)      
#      
from math import * #imports math library to use the mathematical functions

def arctangent(a,b):
    # if statements for the base's angle
    if a == 0: # if its purely imaginary, the angle arctangent would be b/0, and python cannot compute that
        if b > 0:
            theta = pi/2 # where arctan(+b/0) = pi/2; and any pure imaginary number either has pi/2 for positive or (-pi/2 or 3pi/2) for negative
        elif b < 0:
            theta = -pi/2 # where arctan(-b/0) = -pi/2
    elif a < 0:# for negative real exponentiation cases
        theta = pi # where arctan(0/a) will not yield a result, but all negative real numbers will have an angle of pi
    else: # otherwise, the normal arctangent will work for these cases
        theta = atan(b/a)
    return theta

def checkComplex(real,imaginary):
    ## if statements for checking if the result is Real, Imaginary, or Complex
    if round(imaginary,4) == 0: #Real results only
        print("\nThe result is Real:\n\t", round(real,4))
    elif round(real,4) == 0: #Imaginary results only
        print("\nThe result is Imaginary:\n\t", round(imaginary,4), " * i")
    else: # Complex results only
        print("\nThe result is Complex::\n\t", round(real,4), " + ", round(imaginary,4), " * i")

n = "y"
while (n != "n" and n != "N"):
    n = input("\nDo you want to Calculate Logarithms?\n>>")
    if n == "y" or n == "Y":
        print("For the base:")
        a = float(input("input a (Real): ")) #input real number a (base)
        b = float(input("input b (Imaginary): ")) #input real number b for imaginary part (base)
        print("For the input:")
        c = float(input("input c (Real): ")) #input real number c (input)
        d = float(input("input d (Imaginary): ")) #input real number d for imaginary part (input)

        radiusBase = sqrt(a*a + b*b)
        radiusInput = sqrt(c*c + d*d)
        
        alpha = arctangent(a,b)
        beta = arctangent(c,d)

        if radiusBase == 0:
            if radiusInput == 0:
                print("This is undefined")
            else:
                print("The result is 0")
        elif a == 1 and b == 0:
            if c == 1 and d == 0:
                print("This is undefined")
            else:
                print("The result is complex infinity")
        elif a == c and b == d:
            print("The result is 1")
        else:
            real = (log(radiusBase)*log(radiusInput)+alpha*beta)/(log(radiusBase)**2+alpha**2)
            imaginary = (beta*log(radiusBase) - alpha*log(radiusInput))/(log(radiusBase)**2+alpha**2)
            # (theta2*ln|r1| - theta1*ln|r2|)/(ln^2|r1|+theta1^2)

    elif n == "n" or n == "N":
        print("\nBye-bye!")
    else:
        print("\nPlease input y or n only")