# for ascending values 

import pandas as pd

data = {'item': ['laptop', 'monitor', 'HDMI', 'speaker'],
        'cost': [500, 300, 700, 600]
       }

df = pd.DataFrame(data)

sorted_data = df.sort_values(by='cost', ascending=True)

print(sorted_data)

# For descending value use False