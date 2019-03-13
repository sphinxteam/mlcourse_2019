def train_kernel_ridge(X, y, lamb=0.05):
    n_samples, n_features = X.shape
    
    # Obtain kernelized Gram matrix and perform least-squares estimation
    corr = np.exp(-.5 * cdist(X, X) ** 2)
    coef = np.linalg.lstsq(corr + lamb * np.eye(n_samples), y)[0]
    
    # Compute training error
    error = np.mean((y - corr.T.dot(coef)) ** 2)
    print("error on training set: %g" % error)
    
    return coef

def test_kernel_ridge(X_test, y_test, X_train, coef):
    corr = np.exp(-.5 * cdist(X_train, X_test) ** 2)
    
    # Compute test (generalization) error
    error = np.mean((y_test - corr.T.dot(coef)) ** 2)
    print("error on test set: %g" % error)
    
    return error

coef = train_kernel_ridge(X_train, y_train)
kernel_ridge_error = test_kernel_ridge(X_test, y_test, X_train, coef)