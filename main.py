#A big program to calculate a variety of equations and formulas
#Written from feb 6th to _____
#Help from Master Higgins

#Imports
import math

#Functions
def Credits():
    print()
    print("   Ultimate Calculator  ")
    print("------------------------")
    print("       Written by:      ")
    print("  Michael Hussey-Fisher ")
    print()
    print("      Assisted by:      ")
    print("     Master Higgins     ")
    print()
    print("     Submitted to:     ")
    print("       Mr. Hynes       ")
    print()

#Functions
    def MathCalculator():
      print("Math Calculator")
      print( "1. Addition")
      print("2. Subtraction")
      print("3. Multiplication")
      print("4. Division")
      print("5. Exponents")
      print("6. Square Root")
      print("7. Logarithm")
      print("8. Trigonometric Functions")
      print("9. Quadratic Equation")
      print("10. Sine")
      print("11. Cosine")
      print("12. Tangent")
      print("13. Circumference")
      print("14. Area")
      print("15. Volume")
      print("16. Surface Area")
      print("17. Perimeter")
      print("18. Midpoint")
      print("19. Distance")
      print("20. Pythagorean Theorem")
      print("21. Circle Circumference")
      print("22. Circle Area")
      print("23. Circle Radius")
      print("24. Circle Diameter")
      keypad = input("Enter a keypad number: ")

def ScienceCalculator():
    print("Science Calculator")
    print("-----------------")
    print("1. Force")
    print("2. Acceleration")
    print("3. Velocity")
    print("4. Density")
    print("5. Energy")
    print("6. Work")
    print("7. Power")
    print("8. Momentum")
    print("9. Kinetic Energy")
    print("10. Gravitational Potential Energy")
    print("11. Work Done")
    print("12. Power")
    print("13. Efficiency")
    print("14. Molarity")
    print("15. Moles")
    print("16. Concentration")

#Startup
print("--Ultimate Calulator--")
print("The calulator for any and")
print("all the Math/Science needs")

while True:
    Calculator = input("Math calculator or Science calulcator [M/S]? >>> ").upper()
    if Calculator == "M":
        print("Math") 
    elif Calculator == "S":
        print("Science")
    elif Calculator == "CREDITS":
        Credits()
    else:
        print("Please enter a correct option")
