'''
Created on 8/30/2015

@author: KevinFAN
'''
import os
#import CA01.prod.StarCatalog as SC
import CA01.prod.StarCatalog as StarCat
import unittest
#path = os.path.expanduser("KevinFAN/CA01/test/Sao.txt")  #define a path to find the local file


stars = StarCat.StarCatalog()       #call function of the class
readStar = stars.loadCatalog(os.getcwd() + "/SaoChart.txt")
brightestStar = stars.getMagnitude(11.71239554, 10.5452005, 20)
class StarCatalogTest(unittest.TestCase):

    def test20_930_ShouldRequireFoundFile(self):
        starCatalog = StarCat.StarCatalog()
        expectedString = "StarCatalog.loadCatalog:"
        try:
            self.assertRaises(ValueError, starCatalog.loadCatalog, "missingfile")
        except ValueError as raisedException:
            diagnosticString = raisedException.args[0]
            self.assertEquals(expectedString, diagnosticString[0:len(expectedString)])
        except:
            self.fail("incorrect exception was raised")

#starsBetween2And5 = stars.getStarCount(-0.9,55)
#deleteStar = stars.emptyCatalog() 