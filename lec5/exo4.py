"""Model 1 implies that SEX is independent of PE and model the opposite. 
Clearly only model 2 is compatible with the data: SEX and PE are not 
statistically independent.
"""

# contingency table
contingency = pd.crosstab(index=students["SEX"], columns=students["PE"])
# independence G-test
chi2, p_value, _, _ = chi2_contingency(contingency, lambda_="log-likelihood")
print(f"chi2 = {chi2:.2f} with p_value={p_value:.2e} independent: {p_value > alpha}")

# barplot P(PE|SEX)
pd.crosstab(
    index=students["SEX"], columns=students["PE"], 
    normalize="index"
).plot.bar(stacked=True);