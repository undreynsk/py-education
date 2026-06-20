# 16. Lambda функции
# Используйте лямбда-выражение для вычисления объема куба со стороной длины а

import sys

volume = lambda side: side ** 3

start = int(sys.argv[1])
print(f"volume({start}) = {volume(start)}")