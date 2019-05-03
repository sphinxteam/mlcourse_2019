"""We clearly see that the regression coefficient for allergy is now zero. 
By removing coughing, fatigue and car_accident from the set of covariates 
we have effectively blocked all paths that created statistical associations
between allergy and lung cancer. For the remaining features we see that 
only the direct causes of lung cancer (smoking and genetics) have a non-zero 
regression coefficient. By carefully choosing the set of covariate you can 
accurately estimate the causal impact of each factor on the target, but you 
need to know (or infer) the causal structure to do this.
"""

features = [
    column for column in lucas.columns 
    if column not in ["lung_cancer","coughing","fatigue","car_accident"]
]
X, y = lucas[features].astype(float), lucas["lung_cancer"].astype(float)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler().fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

clf = LogisticRegression(C=0.03, penalty="l1", solver="saga")
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(f"Test accuracy: {accuracy}")

coefficients = pd.Series(clf.coef_[0], index=features).sort_values()
coefficients.plot.barh(title="Logistic Regression Coefficients").axvline(0, color='grey');