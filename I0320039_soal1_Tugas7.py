nama = 'Samsuddin Apacemita Magnumasari '

#Penggunaan metode Count()
x = nama.count('a')
y = nama.count('m')
print('Penggunaan metode Count()')
print('jumlah huruf a dalam string nama adalah ',x)
print('jumlah huruf m dalam string nama adalah ',y)
print("")

#Penggunaan metode Find()
a = nama.find('s')
b = nama.find('m')
print('Penggunaan metode Find()')
print('huruf s distring nama ada di index :',a)
print('huruf m distring nama ada di index :',b)

#Penggunaan metode Replace()
nama1 = nama.replace('Samsuddin', 'Fahruddin')
nama2 = nama1.replace('Apacemita', 'Ari')
nama3 = nama2.replace('Magnumasari', 'Wicaksono')
print('Penggunaan metode Replace()')
print('Perubahan nama ke-1 :', nama1)
print('Perubahan nama ke-2 :', nama2)
print('Perubahan nama ke-3 :', nama3)


