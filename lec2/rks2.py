# Compute kernelized Gram matrix using the original kernel ...
from scipy.spatial.distance import cdist
gram_orig = np.exp(-.5 * cdist(X_train, X_train) ** 2)

# ... and plot it.
plt.imshow(gram_orig, interpolation="nearest", vmin=0, vmax=0.1)
plt.colorbar(shrink=0.75)
