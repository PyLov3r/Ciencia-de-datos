
import matplotlib.pyplot as plt
import pandas as pd

s = pd.Series([18,42,9,32,81,64,3])
s.plot(kind='bar')
plt.savefig('plot.png')

data = {
    'ages': [14,18,24,42],
    'heights': [165,180,176,184]
}

df = pd.DataFrame(data)