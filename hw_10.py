import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
lsth = [1 if data.loc[i, 'whoAmI'] == 'human' else 0 for i in range(20)]
lstr = [1 if data.loc[i, 'whoAmI'] == 'robot' else 0 for i in range(20)]
data_hot = pd.DataFrame({'human' : lsth, 'robot' : lstr})
print(data_hot)