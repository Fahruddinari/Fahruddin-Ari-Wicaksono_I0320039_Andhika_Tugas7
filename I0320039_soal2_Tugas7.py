#input nilai
a = float(input('Masukan nilai bilangan yang anda inginkan :'))
print("")

#menggunakan fungsi abs()
print('%0.2f adalah harga mutlak untuk bilangan'%(abs(a)) ,a)
print("")

import math

#menggunakan fungsi ceil()
print('%d adalah nilai pembulatan ke atas untuk bilangan'%(math.ceil(a)), a)
print("")

#menggunakan fungsi floar()
print('%d adalah nilai pembulatan ke bawah untuk bilangan'%(math.floor(a)), a)
print("")