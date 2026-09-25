import pandas as pd
import numpy as np
df = pd.DataFrame({
    'A': [10, 20, 30, 40, 50, 60, 70, 80],
    'B': [5, 10, 15, 20, 25, 30, 35, 40],
    'C': [100, 200, 150, 300, 250, 400, 350, 500]
})

print(df.describe())