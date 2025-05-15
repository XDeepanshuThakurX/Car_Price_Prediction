# 🚗 Car Price Prediction using Machine Learning

This project focuses on predicting the price of cars based on various features using machine learning algorithms. It demonstrates an end-to-end ML pipeline including data cleaning, EDA, feature engineering, model training, and evaluation.

---

## 📌 Problem Statement

Accurately predicting car prices helps buyers and sellers make informed decisions. The goal is to build a regression model that can estimate a car's price given its characteristics such as brand, year, mileage, engine, etc.

---

## 🧰 Tools & Technologies Used

- **Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn  
- **IDE:** Jupyter Notebook  

---

## 📂 Project Structure

```
Car-Price-Prediction/
│
├── data/                   # Raw dataset
├── notebooks/              # Jupyter notebooks
│   └── Car_Price_Prediction.ipynb
├── images/                 # Plots and EDA visuals
├── models/                 # Saved model files (if any)
├── README.md               # Project documentation
└── requirements.txt        # List of dependencies
```

---

## 🔍 Exploratory Data Analysis

- Checked for missing values, outliers, and data types
- Visualized price distribution and relationships with features
- Performed correlation analysis

---

## ⚙️ Model Building

- Applied **Linear Regression** and **Lasso Regression**
- Used train-test split for validation
- Evaluated performance using:
  - Root Mean Squared Error (RMSE)
  - R-squared (R²)

---

## 📈 Results

- Both models performed well, with Lasso Regression slightly reducing overfitting.
- Feature importance revealed that car brand, year, mileage, and engine size significantly influenced the price.

---

## 📌 Conclusion
