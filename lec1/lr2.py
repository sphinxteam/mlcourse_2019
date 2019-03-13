def likelihood(x, y, alpha, var):
    """
        Define the likelihood for a given set of data and explanatory variable $alpha$,
            y = alpha * x + noise (iid Gausian with variance var)
    """
    res = y - alpha * x
    likelihood = 1 / np.power(2 * np.pi * var, y.size/2) * np.exp(-.5 * np.dot(res, res) / var)
    return likelihood
