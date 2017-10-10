import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.cluster import KMeans

# Loading in the csv file
customers = pd.read_csv('Customers.csv')
X = np.array([customers['CustomerID'],customers['Age'],customers['Annual Income'],customers['Spending Score']])  # Manipulating the data
X = X.T  # To make sure the columns represent features

# Creating the clustering model
model = KMeans(n_clusters=5,random_state=0)

# Fitting the clustering model
mod_fit = model.fit_predict(X)
centers = model.cluster_centers_  # Obtaining the centroids

# Plotting the clusters and centroids
scat = plt.scatter(X[:,2],X[:,3],c=mod_fit)
cent = plt.scatter(centers[:,2],centers[:,3],c='k',marker='o', linewidth = 7)
plt.title('Clusters of Customers')
plt.xlabel('Annual Income k$')
plt.ylabel('Spending Score(1-100)')
plt.show()