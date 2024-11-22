# 対数らを扱う
from math import *
import cmath

print("e: ", e)

# べき乗を扱う方法3選
# pow() は組み込みのモノとmathのモノがある
print("2**4: ", 2**4)
print("pow(2, 4): ", pow(2, 4))

# 平方根
print("2**0.5: ", 2**0.5)
print("sqrt(2): ", sqrt(2))
print("2**0.5 == sqrt(2): ", 2**0.5 == sqrt(2))
# 0.5乗するのも平方根を取るのも同じ
# 複素数を扱う場合はcmathモジュールを使用することでより正確かつ負の値も処理できる
print("cmath.sqrt(-3 + 4j): ", cmath.sqrt(-3 + 4j))
print("cmath.sqrt(-1): ", cmath.sqrt(-1))

# exp() で指数関数を扱える
print("exp(2): ", exp(2))
print("exp(2) != e**2: ", exp(2) != e**2)
# 実は e**x のほうがより正確のため等価にはならない

# 対数関数それぞれ
print("log(25, 5): ", log(25, 5))
print("log(1024, 2): ", log(1024, 2))
print("log(1024, 2) == log2(1024): ", log(1024, 2) == log2(1024))
print("log10(10000): ", log10(10000))

# 自然対数
# 第2引数を省略することで扱える
print("log(e): ", log(e))
