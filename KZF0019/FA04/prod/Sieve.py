import math

def calc(number):

    if number < 2: 
        return []
    number = num(number)

    g = g2(number)
    return g

def num(number):
    number = number + 1
    
    # CITATION: Sieve of Eratosthenes
    # Create list of all numbers up to max
    # Start with first prime
    # Strike all multiples 
    # repeat for next un-struck number in list
    
    # set up initial matrix
def fn(number):
    f = [False, False]
    for i in range(2, number):
        f.append(True)
    return f

def tem(number):
    f = fn(number)
    for temp1 in range(2, int(math.sqrt(number) + 1)):
        if f[temp1]:
            for temp2 in range(2 * temp1, number, temp1):
                f[temp2] = False
    return f

def nem(number):
    f = tem(number)
    n = 0
    for temp in range(0, number):
        if f[temp]:
            n = n + 1
    return n
def g1(number):
    n = nem(number)
    g = []
    for temp in range(0, n):
        g.append(0)
    return g

def g2(number):
    f = tem(number)
    g = g1(number)
    temp2 = 0
    for temp1 in range (0, number):
        if f[temp1]:
            g[temp2] = temp1
            temp2 = temp2 + 1
    return g
    



                

