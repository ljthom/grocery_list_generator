"""
This file is the module source for the overall 
application's functionality, including conversions, 
interaction with the database and frontend, and 
calling the recipe scrapers. 

Pantry!    
"""
# Imperial to metric unit conversions
class ImpToMetConversions:
    # Convert fluid ounce (or ounce) to milliliter
    def floz_to_ml(self, oz):
        return oz * 28.41

    # Convert pound to grams
    def lbs_to_g(self, lbs):
        return lbs * 454
    
    
# Metric to imperial unit conversions
class MetToImpConversions:
    # Convert milliliter to fluid ounce (or ounce)
    def ml_to_floz(self, ml):
        return ml / 28.41
    
    # Convert grams to pounds
    def g_to_lbs(self, g):
        return g / 454  

# Big imperial to little imperial conversions
# Mainly used to support imperial to metric conversions
class ImpToImpConversions:
    # Gallon to fluid ounce (or ounce)
    def gal_to_floz(self, gal):
        return gal * 128
    
    # Quart to fluid ounce (or ounce)
    def qt_to_floz(self, qt):
        return qt * 32
    
    # Pint to fluid ounce (or ounce)
    def pt_to_floz(self, pt):
        return pt * 16
    
    # Cup to fluid ounce (or ounce)
    def cp_to_floz(self, cp):
        return cp * 8
    
    # Tablespoon to fluid ounce (or ounce)
    def tbsp_to_floz(self, tbsp):
        return tbsp * 0.5
    
    # Teaspoon to fluid ounce (or ounce)
    def tsp_to_floz(self, tsp):
        return tsp * 0.166667