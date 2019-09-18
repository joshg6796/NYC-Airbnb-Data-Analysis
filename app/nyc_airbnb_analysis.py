#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file_path = "/Users/JoshGoldstein/git/NYC-Airbnb-Data-Analysis/app/dataset/AB_NYC_2019.csv"
dataset = pd.read_csv(file_path)
#%%
neigborhood_group_dataset = dataset[dataset['neighbourhood_group'] == 'Manhattan']

min_prices = neigborhood_group_dataset.loc[neigborhood_group_dataset.groupby('neighbourhood')['price'].idxmin()]
min_prices = min_prices[min_prices['price'] > 0]
min_prices
#%%
x_axis = min_prices['neighbourhood']
y_axis = min_prices['price'].astype(float)

plt.bar(x_axis, y_axis, alpha=0.8)
plt.title('2019 Lowest Priced Listings in Manhattan')
plt.xticks(x_axis, rotation=90, fontsize=10)
plt.xlabel('Neighborhood')
plt.ylabel('Price ($)')
plt.show()
#%%
