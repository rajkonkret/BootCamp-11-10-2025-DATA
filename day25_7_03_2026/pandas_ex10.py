# macierz korelacji
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())
#    Duration  Pulse  Maxpulse  Calories
# 0        60    110       130     409.1
# 1        60    117       145     479.0
# 2        60    103       135     340.0
# 3        45    109       175     282.4
# 4        45    117       148     406.0

# macierz korealacji
print(df.corr())
#           Duration     Pulse  Maxpulse  Calories
# Duration  1.000000 -0.155408  0.009403  0.922721
# Pulse    -0.155408  1.000000  0.786535  0.025120
# Maxpulse  0.009403  0.786535  1.000000  0.203814
# Calories  0.922721  0.025120  0.203814  1.000000
# (0.6) (-0.6)
