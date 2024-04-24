# Model Card

## Model Details
# This machine learning pipeline was made with FastAPi and Random Forest Classifier. 

## Intended Use
# The intended use for this model is the prediction of a person's salary based on other criteria or aspects of themselves.  

## Training Data
# The data used is from publically available census data, located here. 
# https://archive.ics.uci.edu/dataset/20/census+income
# There were 32,562 rows in the original dataset. I did a train/test split using sklearn's model_selection module, putting 80% of the data into training. 

## Evaluation Data
# The data used is from publically available census data, located here. 
# https://archive.ics.uci.edu/dataset/20/census+income
# There were 32,562 rows in the original dataset. I did a train/test split using sklearn's model_selection module, putting 20% of the data into testing. 

## Metrics
# I used precision, recall, and F1 score. My model got the following results: 
# Precision: 0.7311 | Recall: 0.6299 | F1: 0.6767

## Ethical Considerations
# It is possible that the original dataset could be skewe and there were some missing. 

## Caveats and Recommendations
# Due to the Random Forest Classifier, it is possible that different dispersions of training data could create some variation in results model to model. 
