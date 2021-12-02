# OPerator: BUDMAS/BODMAS

delta=87
cosmo=43

'''
1024 512 256 128 64 32 16 8 4 2 1
   0   0   0   0  1  0  1 0 1 1 1 >> 87
   1   0   1   0  1  1  1 0 0 0 0 >> 1392
   0   0   0   0  0  1  0 1 0 1 1 >> 43
   
   0   0   0   0  1  1  1 1 1 1 1 >> 127
   
'''

beta=(delta|cosmo)+(cosmo*2)/(delta<<4)
#      127+86/1392

print(beta)


