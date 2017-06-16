import sys
import pickle

#import new_api

#sys.modules['old_api'] = new_api

with open('object.bin', 'rb') as f:
    o = pickle.load(f)

print(o)

