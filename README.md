# Startup-Profit-Predictor

### Overview
This project aims to predict startup profits using a dataset containing 50 startups . The dataset includes the following features :

- R&D Spend: Research and Development expenses (float)
- Administration: Administration costs (float)
- Marketing Spend: Marketing expenses (float)
- State: The state where the start-up is located (categorical: New York, California, Florida).
- The target variable is Profit. The project involves data exploration, preprocessing, model training with hyperparameter tuning, cross-validation, and final evaluation. In addition, a Streamlit web application is provided for interactive predictions

### Model Training and Evaluation
The Jupyter Notebook (Predict Start-up Business Profits.ipynb) contains all the steps for :

- Exploratory Data Analysis (EDA): Data overview, summary statistics , visualization of numerical and categorical features, and outlier detection
-Preprocessing: Handling categorical variables using OneHotEncoder 
- Modeling: Building multiple regression pipelines (Linear Regression, Ridge Regression, Decision Tree Regression, Random Forest Regression, and XGBoost Regression)
- Hyperparameter Tuning: Using GridSearchCV for selected models
- Cross-Validation: Performing repeated 5-fold cross validation to assess model performance
- Evaluation: Generating evaluation metrics (MSE, RMSE, MAE, R², Adjusted R²) on the test set and visualizing Actual vs. Predicted profit values
  
### Streamlit App for Predictions
A user-friendly Streamlit app is provided for real-time profit predictions. Users can :

- Input values for R&D Spend, Administration,  Marketing Spend and state ( New York, California, Florida)
- Click Predict Profit to see the forecasted profit
- To run the app, simply execute: streamlit run app.py

 ### Model Evaluation Metrics
   During cross-validation and test set evaluation, the following metrics are used to measure model performance:

- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² (Coefficient of Determination)
- Adjusted R²: Adjusted for the number of predictors in the model
- The evaluation results indicate that the Random Forest Regression model, for example, achieved high R² and low error metrics, making it a strong candidate for predicting startup profits




