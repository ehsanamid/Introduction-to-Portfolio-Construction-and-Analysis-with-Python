
def to_celsius(fahrenheit):
    """Return the given fahrenheit temperature in degrees celsius"""
    return (fahrenheit - 32) * (5 / 9)


def days_in_years(number_of_years):
    """ Return the number of days in the given number of years, assuming
        exactly 365 days in all years.
    """
    # Your code goes here
    return number_of_years * 365

def calculate_cartons(eggs):
    """ Calculate the number of cartons needed to hold 
        the specified number of eggs.
    """
    return eggs // 12

def dinner_calculator(meal_cost, drinks_cost):
    """ Calculate the cost of dinner during happy hour.
        Takes into consideration:
         - Pre-GST meal and drink costs
         - Happy Hour discounts
         - GST
    """
    total_cost = (meal_cost + drinks_cost * 0.7) * 1.15
    return total_cost

def trip_cost(price,distance,economy):
    return price * distance *  economy / 100

def odd_finder(a,b,c,d,e,f,g,h,i,j):
    count = 0
    if(a > 0) and (a % 2 != 0):
        count += 1
    if(b > 0) and (b % 2 != 0):
        count += 1
    if(c > 0) and (c % 2 != 0):
        count += 1
    if(d > 0) and (d % 2 != 0):
        count += 1
    if(e > 0) and (e % 2 != 0):
        count += 1
    if(f > 0) and (f % 2 != 0):
        count += 1
    if(g > 0) and (g % 2 != 0):
        count += 1
    if(h > 0) and (h % 2 != 0):
        count += 1
    if(i > 0) and (i % 2 != 0):
        count += 1
    if(j > 0) and (j % 2 != 0):
        count += 1
    return count

def virus_growth(num,rate,hour,time):
    return num * rate ** (time/hour)

def dseries(n_terms):
    sum  = 0
    for i in range(1,n_terms+1):
        sum += i**2
    return sum

print(dseries(1))
print(dseries(2))
print(dseries(3))
print(dseries(4))

# print(virus_growth(100,2,4,16))

# print(odd_finder(1,2,3,4,5,-1,-2,-3,-4,0))




# print(to_celsius(32.0))
# print(to_celsius(212.0))

# print(days_in_years(2))
# print(days_in_years(10))

# print(calculate_cartons(12))
# print(calculate_cartons(65))

# print(dinner_calculator(10, 0))
# print(dinner_calculator(12, 4))

# print(round(trip_cost(1.3, 10,5),2))    
# print(round(trip_cost(1.68, 27,7.7),2))