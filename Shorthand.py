# shorthand: += -= /= *= %= &= |= ^=

# alpha=alpha*cosmo>> alpha*=cosmo

myLapTopPrice=43400
myMobilePrice=21000

print(myLapTopPrice,myMobilePrice)

'''# swap + -
myLapTopPrice+=myMobilePrice
myMobilePrice=myLapTopPrice-myMobilePrice
myLapTopPrice-=myMobilePrice'''


# swap by ^
myLapTopPrice^=myMobilePrice
myMobilePrice^=myLapTopPrice
myLapTopPrice^=myMobilePrice

print(myLapTopPrice,myMobilePrice)