from math import *
DAY_RENT=3.00
NIGHT_RENT=2.00
def _night(no_of_rent):
    cost=no_of_rent *DAY_RENT
    return cost
def _day(no_of_rent):
    ncost=no_of_rent*NIGHT_RENT
    return ncost

if __name__ == '__main__':
    print ( "the cost"+"  "+ str(_night(20)))

    
