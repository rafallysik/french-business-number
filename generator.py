import random

def fr_vat():
	siren=random.randrange(100000000, 999999999)
	klucz=(12+3*(siren %97)) %97
	return "FR{}{}".format(klucz, siren)
    
print(fr_vat() )
print("długość łańcucha {}".format(len(fr_vat())))
