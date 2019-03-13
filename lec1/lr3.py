def power_features(x, max_power):
    """
        Given a vector of data points, x, build a matrix of power
        features from 0 (constant) up to power p for use with
        polynomial fitting.
    """
    # Initialize data matrix
    X = np.zeros((x.shape[0], max_power + 1))

    for p in range(0, max_power+1):
        X[:, p] = x ** p
    
    return X
