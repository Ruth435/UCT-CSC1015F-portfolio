# path testing for the function called ‘aswords’ which accepts an integer (0-999) as a parameter and returns the English language equivalent
# Ruth-ann Rudolph RDLRUT001
# 17/04/2023

# testnumberutil.py
"""
>>> import numberutil
>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(880)
'eight hundred and eighty'
>>> numberutil.aswords(999)
'nine hundred and ninety nine'
>>> numberutil.aswords(60)
'sixty'
>>> numberutil.aswords(120)
'one hundred and twenty'
>>> numberutil.aswords(20)
'twenty'
>>> numberutil.aswords(200)
'two hundred'
>>> numberutil.aswords(99)
'ninety nine'

"""
import doctest
doctest.testmod(verbose=True)