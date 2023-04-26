

from sklearn.cluster import KMeans

from sklearn.datasets import make_moons
X, y = make_moons(n_samples=300, noise=0.1, random_state=0)
data = pd.concat([pd.DataFrame(X), pd.DataFrame(y)], axis=1)
# X = csv.iloc[:, :2].values
# y = csv.iloc[:, 2].values

kmeans = KMeans(n_clusters=3)

kmeans.fit(X)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Create a scatter plot with the data colored by cluster
colors = ['b', 'g', 'r']
for i in range(len(X)):
    plt.scatter(X[i, 0], X[i, 1], color=colors[labels[i]])

plt.title('KMeans with k=3')

# Add centroids to the plot
plt.scatter(centroids[:, 0], centroids[:, 1], color='k', marker='x')

plt.show()