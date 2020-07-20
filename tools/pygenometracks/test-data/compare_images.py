from matplotlib.testing.compare import compare_images
from os import listdir
import os

pngs = [f for f in listdir('test-data') if f.endswith('.png')]

for png in pngs:
    res = compare_images(os.path.join('test-data', png),
                         os.path.join('outputs', png),
                         10)
    print(res)
