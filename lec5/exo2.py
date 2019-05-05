"""Yellow fingers does not cause lung cancer, and lung cancer does not cause 
yellow fingers. However smoking causes both lung cancer and yellow fingers. 
The statisical association between yellow fingers and cancer is entirely due 
to the counfouding effect of smoking. As shown with the barplots below, lung 
cancer becomes independent of yellow fingers when we condition on smoking. 
This an example of confounding or Simpson's paradox.
"""

# barplot P(lung_cancer|yellow_fingers, smoking)
fig, axs = plt.subplots(1,2, figsize=(8,4))

# barplot P(lung_cancer|yellow_fingers, smoking = 1)
smokers = lucas.query("smoking==1")
pd.crosstab(
    index=smokers["yellow_fingers"], columns=smokers["lung_cancer"],
    normalize="index"
).plot.bar(stacked=True, title="smokers", ax=axs[0])

# barplot P(lung_cancer|yellow_fingers, smoking = 0)
non_smokers = lucas.query("smoking==0")
pd.crosstab(
    index=non_smokers["yellow_fingers"], columns=non_smokers["lung_cancer"],
    normalize="index"
).plot.bar(stacked=True, title="non smokers", ax=axs[1])

fig.tight_layout()