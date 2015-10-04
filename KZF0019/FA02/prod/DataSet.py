'''
Created on Sep 19, 2015

@author: KevinFAN
'''
import math
class DataSet(object):

    def __init__(self):
        pass
        
    def gamma(self, x):
        if(x == 1):
            return 1
        if(x == 0.5):
            return math.sqrt(math.pi)
        return (x - 1) * self.gamma(x - 1)
    
    def LHP(self, n):
        n = float(n)
        numerator = self.gamma((n + 1.0) / 2.0)
        denominator = self.gamma(n / 2.0) * math.sqrt(n * math.pi)
        result = numerator / denominator
        return result
    
    def RHP(self, t, n, f):
        epsilon = 0.001
        simpsonOld = 0
        simpsonNew = epsilon
        s = 4
        while (abs((simpsonNew - simpsonOld) / simpsonNew) > epsilon):
            simpsonOld = simpsonNew
            w = t/s
            simpsonNew = f(0,n) + f(t,n)
            flagTag = True
            for i in range(1,s):
                if flagTag:
                    simpsonNew = simpsonNew + 4*f(i*w, n)
                    flagTag = False
                else:
                    simpsonNew =simpsonNew + 2*f(i*w, n)
                    flagTag = True
            simpsonNew = (w/3) * simpsonNew
            s = s * 2
        return simpsonNew

    
    def f(self, u, n):
        n = float(n)
        base = (1 + (u ** 2) / n)
        exponent = -(n + 1.0) / 2.0
        result = base ** exponent
        return result
    
    def p(self, t=None, n=None, tails=None):
        if(t == None):
            raise ValueError
        if(not(isinstance(t, float))):
            raise ValueError
        if(t < 0.0):
            raise ValueError
        
        if(tails == None):
            raise ValueError
        if(not(isinstance(tails, int))):
            raise ValueError
        if((tails != 1) & (tails != 2)):
            raise ValueError
        
        if(n == None):
            raise ValueError
        if(not(isinstance(n, int))):
            raise ValueError
        if(n < 3):
            raise ValueError
        
        self.n = n
        
        constant = self.LHP(n)
        integration = self.RHP(t, n, self.f)
        
        if(tails == 1):
            result = constant * integration + 0.5
        else:
            result = constant * integration * 2
            
        if(result > 1.0):
            raise ValueError
        
        return result
        
        
    
        
            
        
