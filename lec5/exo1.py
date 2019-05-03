"""Allergy and lung cancer are actually independent. This is shown by the statisical 
test and barplot below. In the causal graph we see that both allergy and lung cancer 
are possible causes of coughing. If we condition on coughing (their common effect), 
they will become dependent (as shown by the barplot for coughing patients). It is an 
illustration of selection bias or Berkson's paradox.
"""

# contingency table
contingency = pd.crosstab(index=lucas["allergy"], columns=lucas["lung_cancer"])
# independence G-test
chi2, p_value, _, _ = chi2_contingency(contingency, lambda_="log-likelihood")
print(f"chi2 = {chi2:.2f} with p_value={p_value:.2e} independent: {p_value > alpha}")

# barplot P(lung_cancer|allergy)
pd.crosstab(
    index=lucas["allergy"], columns=lucas["lung_cancer"],
    normalize="index"
).plot.bar(stacked=True);