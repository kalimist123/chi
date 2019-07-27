import pandas as pd
import numpy as np

df_ages = pd.DataFrame({'age': np.random.randint(21, 81, 20)})

print(df_ages)

df_ages['age_bins'] = pd.cut(x=df_ages['age'], bins=[20, 29, 39, 49, 59, 69, 79,89])
print(df_ages)

df_ages['age_by_decade'] = pd.cut(x=df_ages['age'], bins=[20, 29, 39, 49, 59, 69, 79,89],
                                  labels=['20s', '30s', '40s', '50s', '60s','70s','80s'])
print(df_ages)