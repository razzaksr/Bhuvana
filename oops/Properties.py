# class attributes/properties check

class MyCheck:
    alpha=0
    beta=""


my=MyCheck()
mine=MyCheck()
mine.alpha=900
mine.beta="Razak Mohamed"

print(hasattr(my,"cosmo"))

setattr(my,"delta",0.0)

print(hasattr(mine,"delta"))
print(hasattr(my,"delta"))

print(getattr(mine,"beta"))
print(getattr(mine,"alpha"))
delattr(mine,"alpha")

print(getattr(mine,"alpha"))