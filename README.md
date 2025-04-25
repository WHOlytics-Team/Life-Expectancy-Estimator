# Life Expectancy Prediction Using Linear Regression (Ordinary Least Squares)

## 📌 Objective
The objective of this project is to develop an interpretable and statistically robust model that predicts the **life expectancy** of countries based on a variety of socio-economic, environmental, and health-related factors. By using **linear regression**, this project aims to:
- Quantify the impact of key predictors (e.g., GDP, immunisation rates, healthcare expenditure) on life expectancy.
- Identify significant trends and relationships across countries.
- Provide a reliable baseline model for forecasting or policymaking decisions.
- Evaluate model assumptions thoroughly to ensure statistical soundness and avoid misleading or spurious results.

---

## 🌍 Data Source
The [dataset](https://drive.google.com/uc?id=1nXm7P-6nDbqiFYeJdZtwN5ARSNhXI4df&export=download') used was sourced from the **World Health Organisation (WHO)** and includes yearly data for multiple countries. It covers a wide range of indicators such as:
- **Economic metrics**: GDP, income composition of resources.
- **Health infrastructure**: healthcare expenditure, immunisation coverage, number of physicians.
- **Social indicators**: schooling years, adult mortality, HIV/AIDS prevalence.

Data was cleaned and preprocessed to prepare it for regression and residual analysis.

---

## 🔍 Approach

### 1. **Exploratory Data Analysis (EDA)**
- Assessed distributions, trends, and outliers.
- Investigated missing values and implemented appropriate imputation strategies.
- Performed pairwise correlation analysis to explore relationships between predictors (features) and life expectancy (target).

### 2. Data Preprocessing and Feature Engineering

- **Data Type Conversion**: Converted relevant columns to appropriate data types to ensure compatibility with statistical analysis and modelling processes.

- **Normalisation and Standardisation**: Applied Z-score normalisation to numerical features to ensure a standard scale, improve model convergence, and reduce the condition number for enhanced numerical stability ([source](https://link.springer.com/article/10.1007/s11135-005-6225-5)).

- **Log Transformation**: Log-transformed skewed features demonstrating exponential relationships with the target variable (life expectancy) to linearise their behaviour and optimise model performance.

- **Feature Engineering**: Constructed new variables and interaction terms to uncover deeper patterns, enhance interpretability, and mitigate multicollinearity among features.

- **Constant Term Inclusion**: Explicitly added a constant (intercept) term to the regression model to ensure proper statistical specification and unbiased coefficient estimation in OLS modelling.

- **Multicollinearity Diagnostics**:
  - Assessed **Variance Inflation Factor (VIF)** to identify features with high redundancy.
  - Analysed **Pearson correlation coefficients** to detect strong linear associations.
  - Evaluated the **condition number** of the feature matrix to gauge overall multicollinearity and numerical sensitivity.


### 3. **Feature Selection**
- Selected features based on domain relevance, statistical significance, and correlation strength.

### 4. **Model Development**
- Built a **linear regression model** using `statsmodel`.
- Split the dataset into training and testing sets (80/20).
- Validated assumptions of linear regression: linearity, independence, homoscedasticity, and normality of residuals.

### 5. **Statistical Diagnostics**
- **R² (98.2%)**:  
  98.2% of the variation in life expectancy is explained by the selected predictors.
- **RMSE**:  
  Root Mean Squared Error is **1.2 years**, indicating strong predictive performance.
- **Durbin-Watson Stat**:  
  Indicates **no autocorrelation**; residuals are statistically independent.
- **Jarque-Bera Stat**:  
  Confirms **normality of residuals**; no major deviation from the assumption.
- **Coefficient Signs**:  
  All coefficients **align with theoretical expectations**, lending interpretability to the model.
- **Condition Number**:  
  Below 30, suggesting **no multicollinearity or scaling issues**.
- **Multicollinearity Check**:  
  All **VIF scores are under 10**, below the widely accepted threshold for concern ([source 1](https://link.springer.com/book/10.1007/978-1-0716-1418-1), [source 2](https://www.drnishikantjha.com/papersCollection/Multivariate%20Data%20Analysis.pdf)).

---

## 📊 Results & Insights
- The model demonstrates **high predictive accuracy** and **strong explanatory power**.
- Variables like **schooling**, **GDP per capita**, **health expenditure**, and **immunisation rates** had the most substantial positive effects on life expectancy.
- The analysis provides an evidence-based understanding of how various factors drive population longevity across different countries.

---

## 📦 Installation
Ensure Python 3.x is installed. Required libraries include:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels
