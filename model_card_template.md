# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Model type - RandomForestClassifier

## Intended Use
Analysis on census data

## Training Data
80% random split from census data

## Evaluation Data
The other 20% random split from census data

## Metrics
Precision: 0.7781 | Recall: 0.5924 | F1: 0.6727

## Ethical Considerations
It should be noted that this model is only using the data provided,
and any trends found were not induced through bias.
That is to say, I did not start the analysis off with a goal in mind to prove.

## Caveats and Recommendations
A precision of 0.78 is just ok for a classification model,
so the data collected could overall not be the best metrics to determine salary.