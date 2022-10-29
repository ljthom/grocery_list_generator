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