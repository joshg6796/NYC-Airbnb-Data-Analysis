#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
    Read in csv dataset from local file path. The csv dataset can be downloaded from this link:
    https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data#AB_NYC_2019.csv
'''
file_path = "/Users/JoshGoldstein/git/NYC-Airbnb-Data-Analysis/app/dataset/AB_NYC_2019.csv"
dataset = pd.read_csv(file_path)

#%%
'''
    This function will generate a bar graph with lowest priced Airbnb listings of 2019 given a specified neighbourhood 
    and neighbourhood group. 
'''
def getLowestPriceByNeighbourhood(nhood, nhood_group):
    # Filter dataset by neighbourhood and neighbourhood group.
    neighbourhood_group_dataset = dataset[dataset['neighbourhood_group'] == nhood_group]
    neighbourhood_group_dataset = neighbourhood_group_dataset[neighbourhood_group_dataset['neighbourhood'] == nhood]

    # To simplifiy the dataset, only listings that have 200+ reviews will be considered in the data analysis. 
    # This will yield a result of more reputable listings too.
    neighbourhood_group_dataset = neighbourhood_group_dataset[neighbourhood_group_dataset['number_of_reviews'] >= 200]

    # Ignore listings that have a price of $0. Such listings will not be considered in the data analysis.
    neighbourhood_group_dataset = neighbourhood_group_dataset[neighbourhood_group_dataset['price'] > 0]

    # Prepare data for graph and plot the graph.
    x_axis = neighbourhood_group_dataset['id'].astype(str)
    y_axis = neighbourhood_group_dataset['price'].astype(float)

    plt.bar(x_axis, y_axis, alpha=0.8)
    plt.title('2019 Lowest Priced Listings in ' + nhood + ', '+nhood_group)
    plt.xticks(x_axis, rotation=90, fontsize=10)
    plt.xlabel('Listing ID')
    plt.ylabel('Price ($)')

    # Annotates the exact price on top of each bar in the bar graph.
    for i,j in zip(x_axis, y_axis):
        plt.annotate(str(int(j)),xy=(i,j+0.5), xytext=(-10,1.75), textcoords='offset points', weight='bold')

    plt.show()

#%%
getLowestPriceByNeighbourhood('Long Island City', 'Queens')
getLowestPriceByNeighbourhood('Astoria', 'Queens')
getLowestPriceByNeighbourhood('Greenpoint', 'Brooklyn')
getLowestPriceByNeighbourhood('Park Slope', 'Brooklyn')
getLowestPriceByNeighbourhood('West Village', 'Manhattan')
getLowestPriceByNeighbourhood('Chelsea', 'Manhattan')

#%%
