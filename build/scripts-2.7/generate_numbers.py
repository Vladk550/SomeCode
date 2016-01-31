__author__ = 'yanabanana'

import random

with open('numbers.txt', 'w') as f:
    f.writelines('{}\n'.format(random.randint(-100000, 100000)) for _ in range(100000))
