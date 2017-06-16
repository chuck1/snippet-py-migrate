
import pickle

import old_api

o = old_api.Foo()

with open('object.bin', 'wb') as f:
    pickle.dump(o, f)



