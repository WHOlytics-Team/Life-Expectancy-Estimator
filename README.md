# Life Expectancy Prediction Using Linear Regression (Ordinary Least Squares)

## 📌 Objective
Predicting **life expectancy** and understanding which factors are of significant influence is crucial for informing policy decisions for public health strategies and improving population wellbeing. In this project, a statistically robust **linear regression** model is developed which quantifies the impacts of key socio-economic, environmental, and health-related factors. From the results of this estimation, an interface is developed which allows users to input data and obtain accurate life expectancy predictions. 

---

## 🌍 Data Source
The [dataset](https://drive.google.com/uc?id=1nXm7P-6nDbqiFYeJdZtwN5ARSNhXI4df&export=download') was sourced from the **World Health Organisation (WHO)** and is yearly in frequency, with a sample period of 2000 to 2015, spanning 179 countries. Included are a range of indicators which are characterised by 3 broad categories:
- **Economic Indicators**: GDP-per-Capita and Geographical Location.
- **Health Infrastructure Measures**: Thinness in Teens, HIV/AIDS prevalence and Immunisation Coverage. 
- **Social Measures**: Average Years of Schooling, Infant Mortality and Adult Mortality.

---

## 🔍 Approach

### 1. **Exploratory Data Analysis (EDA)**
The exploratory analysis includes:
- Assessing distributions, trends and potential outliers.
- Assesing the linearity of the relationship between the features and life expectancy. In particular, GDP-per-Capita and HIV Incidences show to be non-linear. This issue is circumvented by log-transforming these variables. 
- Performing pairwise correlation analysis to explore relationships between predictors and life expectancy, motivating feature selection with regard to avoiding multicolinearity.

### 2. Data Preprocessing and Feature Engineering
- **One Hot Encoding**: Given their importance in determining life-expectancy, regions are one-hot encoded for their inclusion as categorical predictors; Africa was dropped to avoid perfect multicollinearity and is therefore represented by the intercept term. 
- **Normalisation and Standardisation**: Z-score normalisation is applied to ensure a standard scale, improve model convergence, and reduce the condition number for enhanced numerical stability ([source](https://link.springer.com/article/10.1007/s11135-005-6225-5)).
- **Log Transformation**: Log-transformations are applied to GDP-per-Capita and HIV incidences to linearise their relationship with life expectancy.

### 3. **Modelling**
Selected features are based on domain relevance, statistical significance, and correlation strength. The data is train-test split (80%/20%) before a **linear regression model** is estimated using `statsmodel`. The regression equation is specified as:

<p align="center">
  <img src="https://gcdnb.pbrd.co/images/Qz8moR3JRXwU.png?o=1" width="100%">
</p>

---  

## 📊 Post Estimation Analysis  

### 1. **Diagnostics and Performance**  
- **R² (98.2%)**:  
  98.2% of the variation in life expectancy is explained by the variation in the selected predictors.
- **RMSE**:  
  Root Mean Squared Error is **1.2 years**, indicating strong predictive performance.
- **Durbin-Watson Stat**:  
  Indicates **no autocorrelation**; residuals are serially independent.
- **Jarque-Bera Stat**:  
  Confirms **normality of residuals**; no skewness nor kurtosis in the distribution of residuals.
- **Coefficient Signs**:  
  All coefficients **align with theoretical expectations**, lending interpretability to the model.
- **Condition Number**:  
  Below 30, suggesting **no multicollinearity or scaling issues**.
- **Multicollinearity Check**:  
  All **VIF scores are under 10**, below the widely accepted threshold for concern ([source 1](https://link.springer.com/book/10.1007/978-1-0716-1418-1), [source 2](https://www.drnishikantjha.com/papersCollection/Multivariate%20Data%20Analysis.pdf)).


### 2. Results & Insights
All tests for significance are conducted at the 5% level against the null hypothesis drawn under the t-distribution of insignificance. All none-regional coefficients are statistically significant. In fact, all but _Thinness Teens_ are significant at the 1% level. Of the regions, only _Oceania_ and _Middle East_ are estimated to be insignificant. 

The sign of all coefficients is in line with the theoretical relationship between the predictors and life expectancy. The positive coefficient associated with _Year_ indicates that as time moves forward, life-expectancy increases. The constant term captures the life expectancy of someone in Africa when all other predictors are set to zero. 

---

## 📦 Installation
Ensure Python 3.x is installed. Required libraries include:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels

