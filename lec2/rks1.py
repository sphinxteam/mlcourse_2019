from scipy.spatial.distance import pdist

# Generate Z for a given value of D
def generate_random_features(X_train, n_projections):
    n_features = X_train.shape[1]
    A = np.random.randn(n_features, n_projections) / np.sqrt(n_projections)
    return X_train.dot(A)

# Compute distance matrix for both original and transformed sets of features
dists_orig = pdist(X_train)
dists_proj_10 = pdist(generate_random_features(X_train, 10))
dists_proj_40 = pdist(generate_random_features(X_train, 40))

# Scatter plot of distances between samples in original/transformed spaces
plt.plot(dists_orig, dists_proj_10, "o", label=r"$D = 10$")
plt.plot(dists_orig, dists_proj_40, "o", label=r"$D = 40$")
plt.plot([0, 60], [0, 60], "k")
plt.legend()