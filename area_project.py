# asks user to enter the radius of the circle
# calculate and print the area and circumference of the circle

import math

radius = float(input("Enter the radius of the circle in cm: "))
area = math.pi * radius * radius
print("The area of the circle is: ", area, "cm^2")  
circumference = 2 * math.pi * radius
print("The circumference of the circle is: ", circumference, "cm")