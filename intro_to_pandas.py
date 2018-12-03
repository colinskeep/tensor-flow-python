from __future__ import print_function
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
# frame = pd.DataFrame({'City name': city_names, 'Population': population})
california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")

# print(california_housing_dataframe.describe())
# plt.plot(california_housing_dataframe)
# plt.show()  //matplotlib testing

cities = pd.DataFrame({'City name': city_names, 'Population': population})
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']
cities['Is wide and has saint name'] = (cities['Area square miles'] > 50) & cities['City name'].apply(lambda name: name.startswith('San'))
print(cities.reindex(np.random.permutation(cities.index)))
