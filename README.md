# housing-dashboard
This code represents a continuation of the analysis I did on the Washoe County housing market for my PhD disertation. That analysis involved regressing the housing sale price using an OLS hedonic model to predict the value of the home at the time of listing. Based on the value at listing and the original purchase price, I determined the loss in the value of the home and was able to estimate the effect of loss aversion on the asking price of the home at the time it was listed. This loss amount was also used to estimate the effect of loss aversion of the final sale price and the time on market.

## Current status
At this time, the code represents an exploratory analysis of the data. This analysis includes fitting the data to multiple models. To repeat the prior work, a multiple regression model on the final sale price of the home was run. Additionally, based on the findings in the exploratory process, a Gradient Boosting Regressor model was run. This model had a significantly better fit than the Multiple Regression model the was used in the original analysis. 

## Future work
The next steps to consider for this analysis are to:
1. Estimate the value of the home at the time of listing
2. Calculate the loss as the difference between the original purchase price and the estimated value at the time of listing
3. Estimate the loan to value ratio (LTV)
    - The LTV is expected to have similar impacts to the asking price, sale price, and time to sell as loss and thus needs to be accounted for
4. Perform regression on asking price of home using loss and LTV
5. Model survival curves using loss and LTV