# We don't really wanna use for loops in Python...
def compute_distances(X):
    n_samples = len(X)
    distances = np.zeros((n_samples, n_samples))
    for i in range(n_samples):
        for j in range(n_samples):
            distances[i, j] = np.sqrt((X[i, 0] - X[j, 0]) ** 2 + (X[i, 1] - X[j, 1]) ** 2)
    return distances
        
print("naive version using for-loops:")
distances = compute_distances(X)
%timeit compute_distances(X)
print(distances[:3,:3])

# We can vectorize it!
print("vectorized version using numpy:")
distances = np.sqrt(np.sum((X[:, np.newaxis] - X) ** 2, 2))
%timeit np.sqrt(np.sum((X[:, np.newaxis] - X) ** 2, 2))
print(distances[:3,:3])

# Or use something that someone already wrote in C
from scipy.spatial.distance import cdist
print("using cdist from scipy:")
distances = cdist(X, X)
%timeit cdist(X, X)
print(distances[:3,:3])

# shape of distance matrix
print("distances.shape = ", distances.shape)