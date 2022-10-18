print(" $$$$$$\  $$$$$$$\  $$$$$$$\  $$$$$$\  $$$$$$\  $$\   $$\  ")
print("$$  __$$\ $$  __$$\ $$  __$$\ \_$$  _|$$  __$$\ $$$\  $$ | ")
print("$$ /  $$ |$$ |  $$ |$$ |  $$ |  $$ |  $$ /  $$ |$$$$\ $$ | ")
print("$$$$$$$$ |$$ |  $$ |$$$$$$$  |  $$ |  $$$$$$$$ |$$ $$\$$ | ")
print("$$  __$$ |$$ |  $$ |$$  __$$<   $$ |  $$  __$$ |$$ \$$$$ | ")
print("$$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ |  $$ |  $$ |$$ |\$$$ | ")
print("$$ |  $$ |$$$$$$$  |$$ |  $$ |$$$$$$\ $$ |  $$ |$$ | \$$ | ")
print("\__|  \__|\_______/ \__|  \__|\______|\__|  \__|\__|  \__| ")



import time
import math

print('Nama : "Adrian Halim"')
print('Nim : "064002200043"')

x1 = eval(input('Masukan titik kordinat x1: '))
x2 = eval(input('Masukan titik kordinat x2: '))
y1 = eval(input('Masukan titik kordinat y1: '))
y2 = eval(input('Masukan titik kordinat y2: '))

print('Hasil dari jarak antara titik A[{0} , {1}] dan B[{2} , {3}] adalah'.format(x1,x2,y2,y1), math.sqrt((x2-x1)**2+(y2-y1)**2))
time.sleep(50)