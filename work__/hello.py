import math
import time
print time.clock

name = "seth amponsah"
print name

#request inputs
TAX_RATE = 20
STANDAND_DEDUCTION= 45
DEPENDENT_DEDUCTION = 90
grossIncome = input("Enter the gross income")
numDependents=input("Enter the number of dependents: ")

taxableIncome = grossIncome - STANDAND_DEDUCTION - DEPENDENT_DEDUCTION * numDependents
incomeTax= taxableIncome * TAX_RATE

print "The income tax is $" +str(round(incomeTax,2))

print "Trying Daniels Program"
fname = raw_input("please enter your firstname")
lname = raw_input("please enter your lastname")

print " " * 1+fname+"  "+lname

print """seth"""

#area of a circle

radius =input("Enter the radius of the circle")
area = math.pi*(radius ** 2)
print("the area of the circle is:" +" "+str(area))

