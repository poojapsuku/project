import numpy as np
import pandas as pd

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('darkgrid')

df = pd.read_csv('example1.csv')
df.head()

df.shape

df.describe()

#df["mean score"] = ((df["math score"] + df["reading score"] + df["writing score"]) / 3).round()
df.head()
#df['gender'].value_counts()

from sklearn.preprocessing import LabelEncoder
lc = LabelEncoder()
df['Gender'] = lc.fit_transform(df['Gender'])
df['Department'] = lc.fit_transform(df['Department'])
df['Year'] = lc.fit_transform(df['Year'])
df['Label'] = lc.fit_transform(df['Label'])
#df['Teachers Feedback'] = lc.fit_transform(df['Teachers Feedback'])
df.head()

sns.countplot(df['Gender'], hue = df['Year'])

labels = ['None', 'Completed']
colors = ['red', 'green']
plt.pie(df['Have you won or participated in any Non - Technical event?'].value_counts() , labels = labels, colors = colors)
plt.show()
import pandas as pd

