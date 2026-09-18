\# 🍔 Food Delivery Analytics \& Delivery Time Prediction



\## 📌 Project Overview



This project analyzes food delivery operations to understand the factors associated with delivery time.



The project combines Exploratory Data Analysis (EDA) with Machine Learning to identify patterns in delivery performance and predict delivery time.



\## 🎯 Objectives



\- Analyze food delivery operations

\- Understand delivery-time patterns

\- Study the relationship between distance and delivery time

\- Analyze the impact of road traffic and weather

\- Compare delivery performance across vehicle types and cities

\- Examine driver ratings and delivery time

\- Build a Machine Learning model to predict delivery time



\## 📊 Dataset



The dataset contains 38,964 food delivery records and 22 variables.



Important variables include:



\- Delivery person age

\- Delivery person rating

\- Vehicle condition

\- Multiple deliveries

\- Weather conditions

\- Road traffic density

\- Type of order

\- Type of vehicle

\- Festival

\- City

\- Distance

\- Delivery time



\## 🛠️ Technologies Used



\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Scikit-learn

\- Jupyter Notebook

\- Git

\- GitHub



\## 🔍 Exploratory Data Analysis



The analysis examines:



\### Delivery Time



Distribution and statistical summary of delivery times.



\### Traffic



Relationship between road traffic density and delivery time.



\### Distance



Relationship between delivery distance and delivery time.



\### Weather



Comparison of delivery times across different weather conditions.



\### Vehicle Type



Comparison of delivery performance across vehicle types.



\### City



Comparison of average delivery time across cities.



\### Driver Rating



Analysis of the relationship between driver ratings and delivery time.



\## 🤖 Machine Learning



A Random Forest Regression model was developed to predict delivery time.



\### Features Used



\#### Numerical Features



\- Delivery person age

\- Delivery person rating

\- Vehicle condition

\- Multiple deliveries

\- Distance



\#### Categorical Features



\- Weather conditions

\- Road traffic density

\- Type of order

\- Type of vehicle

\- Festival

\- City



Categorical variables were transformed using One-Hot Encoding.



A train-test split was used to evaluate the model on unseen data.



\## 📈 Model Evaluation



The model was evaluated using:



\- Mean Absolute Error (MAE)

\- Root Mean Squared Error (RMSE)

\- R² Score



The actual model results are available in the project notebook.



\## 📁 Project Structure



```text

Food-Delivery-Analytics/

│

├── data/

│   └── food\_orders.csv

│

├── images/

│   ├── delivery\_time\_distribution.png

│   ├── traffic\_vs\_delivery\_time.png

│   ├── distance\_vs\_delivery\_time.png

│   ├── weather\_vs\_delivery\_time.png

│   ├── vehicle\_vs\_delivery\_time.png

│   ├── city\_vs\_delivery\_time.png

│   ├── rating\_vs\_delivery\_time.png

│   ├── correlation\_heatmap.png

│   ├── actual\_vs\_predicted.png

│   └── feature\_importance.png

│

├── notebooks/

│   └── food\_delivery\_analysis.ipynb

│

├── src/

│

├── README.md

├── requirements.txt

└── .gitignore

