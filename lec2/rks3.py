def generate_nonlinear_features(X, n_projections):
    n_features = X.shape[1]
    
    # Sample \omega
    w = np.random.randn(n_features, n_projections)
    
    # Compute z
    z = np.hstack((np.cos(X.dot(w)), np.sin(X.dot(w)))) / np.sqrt(n_projections)
    return z