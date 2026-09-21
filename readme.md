# 🍔 Food Delivery Analytics & Delivery Time Prediction

## 📌 Project Overview

This project analyzes food delivery operations to understand the factors associated with delivery time and develops a Machine Learning model to predict delivery time.

The project combines **Exploratory Data Analysis (EDA)**, statistical analysis, data visualization, and **Random Forest Regression** to investigate delivery-time patterns and build a predictive model.

---

## 🎯 Objectives

* Analyze food delivery operations
* Understand delivery-time patterns
* Study the relationship between distance and delivery time
* Analyze road traffic and weather conditions
* Compare delivery performance across vehicle types and cities
* Examine the relationship between driver ratings and delivery time
* Identify important features used by the prediction model
* Build a Machine Learning model to predict delivery time

---

## 📊 Dataset

The dataset contains **38,964 food delivery records and 22 variables**.

### Key Variables

* Delivery person age
* Delivery person rating
* Vehicle condition
* Multiple deliveries
* Weather conditions
* Road traffic density
* Type of order
* Type of vehicle
* Festival
* City
* Distance
* Delivery time

The target variable for Machine Learning is:

`Time_taken (min)`

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook
* Git
* GitHub

---

## 🔍 Exploratory Data Analysis

The project investigates several factors associated with delivery time.

### Delivery Time

The dataset has an average delivery time of **26.58 minutes**, with a median of **26 minutes**.

The observed delivery times range from **10 to 54 minutes**.

### Distance

Distance was analyzed against delivery time using scatter plots and correlation analysis.

The correlation between distance and delivery time was approximately **0.322**, indicating a positive relationship in this dataset.

### Road Traffic

Delivery time was compared across different road-traffic-density categories to examine how traffic conditions are associated with delivery performance.

### Weather

Delivery times were compared across different weather conditions.

### Vehicle Type

Average and median delivery times were analyzed across vehicle types.

### City

Delivery performance was compared across cities using average and median delivery times.

### Driver Rating

Driver ratings were analyzed in relation to delivery time.

The correlation between driver rating and delivery time was approximately **-0.362** in the dataset.

### Correlation Analysis

A correlation matrix was created for the numerical variables to examine relationships between delivery time and other numerical features.

---

## 🤖 Machine Learning

A **Random Forest Regression** model was developed to predict delivery time.

### Numerical Features

* Delivery person age
* Delivery person rating
* Vehicle condition
* Multiple deliveries
* Distance

### Categorical Features

* Weather conditions
* Road traffic density
* Type of order
* Type of vehicle
* Festival
* City

Categorical variables were processed using **One-Hot Encoding**.

Missing values in numerical model features were handled using median imputation.

The data was divided into training and testing sets using an **80/20 train-test split**.

A preprocessing and model pipeline was used to keep the data transformation and prediction workflow together.

---

## 📈 Model Performance

The Random Forest Regression model achieved the following results on the test dataset:

| Metric |           Result |
| ------ | ---------------: |
| MAE    | **3.12 minutes** |
| RMSE   | **3.93 minutes** |
| R²     |        **0.818** |

The model's **MAE of 3.12 minutes** means that its predictions differed from the actual delivery times by about 3.12 minutes on average in absolute terms.

The **R² score of 0.818** indicates that the model captured a substantial portion of the variation in delivery time within this test dataset.

---

## ⭐ Feature Importance

The Random Forest model's feature-importance analysis identified the following features among the most important model inputs:

| Feature                  | Importance |
| ------------------------ | ---------: |
| Delivery person rating   |      0.215 |
| Distance                 |      0.147 |
| Low road traffic density |      0.113 |
| Multiple deliveries      |      0.109 |
| Delivery person age      |      0.101 |
| Sunny weather            |      0.070 |
| Vehicle condition        |      0.070 |

These values represent the features the Random Forest model relied on most heavily for its predictions. They should not be interpreted as proof that a feature independently causes changes in delivery time.

---

## 📊 Visualizations

The project includes visualizations covering:

* Delivery time distribution
* Traffic vs delivery time
* Distance vs delivery time
* Weather vs delivery time
* Vehicle type vs delivery time
* City vs delivery time
* Driver rating vs delivery time
* Correlation heatmap
* Actual vs predicted delivery time
* Feature importance

---

## 📁 Project Structure

```text
Food-Delivery-Analytics/
│
├── data/
│   └── food_orders.csv
│
├── images/
│   ├── actual_vs_predicted.png
│   ├── city_vs_delivery_time.png
│   ├── correlation_heatmap.png
│   ├── delivery_time_distribution.png
│   ├── distance_vs_delivery_time.png
│   ├── feature_importance.png
│   ├── rating_vs_delivery_time.png
│   ├── traffic_vs_delivery_time.png
│   ├── vehicle_vs_delivery_time.png
│   └── weather_vs_delivery_time.png
│
├── notebooks/
│   └── food_delivery_analysis_final.ipynb
│
├── src/
│   └── analysis.py
│
├── readme.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/dharani-15-star/Food-Delivery-Analytics.git
```

### 2. Navigate to the project

```bash
cd Food-Delivery-Analytics
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the analysis script

```bash
python src/analysis.py
```

### 5. Open the Jupyter Notebook

```bash
python -m jupyter notebook
```

Then open:

```text
notebooks/food_delivery_analysis_final.ipynb
```

---

## 💡 Key Project Takeaways

This project demonstrates an end-to-end data science workflow:

**Data → Cleaning → EDA → Visualization → Feature Analysis → Preprocessing → Machine Learning → Evaluation → Interpretation**

It demonstrates practical skills in:

* Data analysis
* Data cleaning
* Exploratory Data Analysis
* Data visualization
* Feature engineering and preprocessing
* Machine Learning
* Model evaluation
* Git/GitHub project management
