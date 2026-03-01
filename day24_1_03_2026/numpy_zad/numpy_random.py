from numpy import random

x = random.randint(100, size=5)
print(x)  # [ 8 75 98 54 16]

x = random.randint(100, size=(3, 5))
print(x)
# [[28 14 83 34 33]
#  [13 95 98 59 68]
#  [95 70 90 72 35]]

x = random.rand(5)
print(x)  # [0.62910091 0.00721311 0.58687773 0.6260181  0.81099889]
print(x.dtype)  # float64

x = random.rand(3, 4)
print(x)
# [[0.78332144 0.24573234 0.99837399 0.45656728]
#  [0.35256526 0.07705059 0.35921788 0.06221404]
#  [0.70931709 0.75973276 0.36406465 0.63892951]]

x = random.choice([3, 5, 7, 9])
print(x)  # 5

x = random.choice([3, 5, 7, 9], size=(3, 5))  # z powtórzeniami
print(x)
# [[9 5 9 9 9]
#  [9 9 9 5 3]
#  [3 5 5 7 3]]

# bez powtórzen -> False
x = random.choice([3, 5, 7, 9], 2, replace=False)
print(x) # [7 9]
