import time
import os

for i in range(10):
    print("\n" * 130)
    print('-' * (30-i))
    print(' ' * (i + 1) + '~')
    print('-' * (30-i))
    time.sleep(0.5)

os.system('cls')
print('Você chegou ao seu destino')