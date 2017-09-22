import numpy as np

sel = np.random.choice(range(20), 15, replace=False)  # Creation of random vector with elements from 0 to 20, size 15
                                                      # and without repetition
print(sel)

# Finding the index of the maximum value
print(np.max(sel))
print(np.argmax(sel))

# Replacing the maximum value by 100
sel[np.argmax(sel)] = 100
print(sel)
