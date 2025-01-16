### SERX94: Project Proposal
### Do People in Wealthier Countries Live Longer?
#### John Garvey
###### 11/20/2023

## Evaluation Metrics
### Metric 1
**Name:** MSE

**Choice Justification:** The first evaluation metric I chose I of course MSE (minimum squared error)
for my linear regression model. The MSE finds the smallest possible residual distances from the modeled
function and the actual data points. So the MSE for each is the least possible.

Interpretation:** TODO

### Metric 2
**Name:** Accuracy

**Choice Justification:** The second evaluation metric I chose is the accuracy of my predictions. The
accuracy is taken from the mean of the life expectancy of a nation. The prediction finds the mean 
life expectancy. The accuracy measures the mean distance from the prediction to the actual.

## Alternative Models
### Alternative 0
**Construction:** This is the baseline linear regression prediction model for estimating the life expectancy
of a nation based on its GDP. This model was chosen because the GDP has the stongest correlation with
the life expectancy of a nation.

**Evaluation:** 

### Alternative 1
**Construction:** The initial baseline model is for a single feature being the GDP this feature 
was chosen because the GDP and Life Expectancy have the strongest correlation. For this secondary 
alternative model we chose the second strongest correlation for life expectancy being the percentage
of underweight children in the population of a nation. 

**Evaluation:** This model actually tends to perform better for predicting the life expectancy of a nation.
Both the MSE and Accuracy tend to be slightly less than our baseline GDP model.

### Alternative 2
**Construction:** This last model is a multiple variable / feature linear regression model for predicting the
the life expectancy of a nation. This model incorporates both the above features into one predictive model.
The model estimates the life expectancy of a nation from its GDP and its percent of underweight childre.

**Evaluation:** This model tends to perform about as well as model 2 this is not significant increase
in the accuracy. As of now our models are about 5 years off on average from predicting the actual life 
expectancy of a nation.

## Best Model

**Model:** Model 02 Life Expectancy based on Percentage of Underweight Children. As of now our model 
is about 5 years off from the actual average mean life expectancy. I am hoping after more tweaking I 
can get this prediction accuracy to less than 5 years.