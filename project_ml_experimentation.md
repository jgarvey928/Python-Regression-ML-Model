#### SERX94: Experimentation
### Do People in Wealthier Countries Live Longer? (Working Title)
#### John Garvey
###### 11/20/2023


## Explainable Records
### Record 1
**Raw Data:** Malaysi Life Expectancy vs GDP

Country: Malaysia 
Actual Life Expectancy: 74.2331875 
Feature GDP: 7317.355520461901
Model01 Prediction:  68.10133249635184 = 0.00027894 * 7317.355520461901 + 66.06025658
Model01 Difference: 6.131855003648155

Prediction Explanation:** The nation being tested is the nation of Malaysia. The input feature data is the GDP for the 
nation being $7,317.36 per capita. And based on this input our base line model predicts the mean life expectancy to be
68 years. Which is about 6 years off from the actual life expectancy of the nation being 74 years.

### Record 2
**Raw Data:** Honduras Life Expectancy vs Percentage of Underweight Children
Country: Honduras 
Actual Life Expectancy: 70.5875 
Feature Underweight Children: 9.533333333333333
Model02 Prediction:  67.92262981426656 = -0.5675496 * 9.533333333333333 + 73.33326929
Model02 Difference: 2.6648701857334487

Prediction Explanation:** The nation being tested is the nation of Honduras. The input feature data is the percentage of
underweight children for the nation being 9.5%. And based on this input, our best model predicts the mean life expectancy 
to be 68 years. Which is about 3 years off from the actual life expectancy of the nation being 71 years

## Interesting Features
### Feature A
**Feature:** Changing Parameters

**Justification:** In order to improve the accurate of the mutlivariable model, we can choose better national povery indicators
instead of only use the GDP and percentage of underweight children, we can change the indicators that have a stronger correlation.
We also still need to add the records going back to the 60's.

### Feature B
**Feature:** Removing Outliers

**Justification:** The data set right are being effects be the most significant outliers in the data. There are several
outliers in the data that take just be removed. With them gone our models hopefully well become more than 5 years accurate.

## Experiments 
### Varying A
**Prediction Trend Seen:** GDP there is the strongest correlation between the life expectancy of a nation and its GDP.
The predicitive power of this model is our baseline and average a mean accuracy off by about 5 years.

### Varying B
**Prediction Trend Seen:** Percentage of underweight children has a strong with life expectancy not as strong as the GDP.
However the accuracy of this model tends to be a sligthy higher on average.

### Varying A and B together
**Prediction Trend Seen:** Together the GDP and Percentage of underweight children create the third model. This models 
accuracy is not improved greatly by the extra parameters so by occams razor its would seem that only model 2 with less 
parameters but same accuracy would be the better model.

