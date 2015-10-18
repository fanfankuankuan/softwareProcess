
import unittest
from FA04.prod.Sieve import calc

class SieveTest(unittest.TestCase):


    def test001(self):
        x = int(raw_input("input a value "))    
        print "The primes are "
        print calc(x)
