# Working with models

## Pitfalls of statistics

- spurious correlation
- p-hacking
- correlation is not causation
  - selection bias, confounders, Simpson's paradox, Berkson's paradox
  - intro to causal calculus, intervention
- the "let data speak for itself" fallacy
  - you *need* assumptions / models
  - frequentist approach
  - bayesian approach

## Pitfalls of ML

- target leak
- model bias / overfitting
  - golden rule (never use test set for training)
  - build a good test and validation sets, time-series
  - difficulty with unsupervised models
- covariate shift
  - adversarial examples
  - robustness
- black box
  - interpretation vs performance tradeoff
  - https://www.kdd.org/kdd2016/papers/files/rfp0573-ribeiroA.pdf
  - http://cs231n.github.io/understanding-cnn/
  - https://blog.datadive.net/interpreting-random-forests/

## References

- ADAfaEPoV https://www.stat.cmu.edu/~cshalizi/ADAfaEPoV/
