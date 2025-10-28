# 🩺 Medical Insurance Cost Prediction

### 📊 Predicting Health Insurance Charges Using Machine Learning  

This project analyzes a medical insurance dataset and builds a machine learning model to predict the insurance cost billed to individuals based on their age, BMI, smoking status, region, and other factors.  
It includes full **EDA, hypothesis testing, feature engineering, model training, evaluation, and deployment.**

---

## 🧠 Project Overview

| Feature | Description |
|----------|-------------|
| **Domain** | Healthcare / Predictive Analytics |
| **Goal** | Predict medical insurance `charges` for individuals |
| **Algorithm Used** | Random Forest Regressor |
| **Dataset Size** | 1338 rows × 7 columns |
| **Target Variable** | `charges` – Medical insurance cost billed |
| **Libraries Used** | Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, Statsmodels, Flask |

---

## 🧾 Dataset Description

**Dataset columns:**
| Column | Description |
|---------|-------------|
| `age` | Age of primary beneficiary |
| `sex` | Gender (male/female) |
| `bmi` | Body Mass Index |
| `children` | Number of children covered by insurance |
| `smoker` | Smoking status (yes/no) |
| `region` | Residential region (northeast/northwest/southeast/southwest) |
| `charges` | Individual medical costs billed by health insurance |

**Feature Engineering:**
- `Age Group` → Teens, Young Adults, Uncs, Middle-Aged, Seniors  
- `Has Child` → Yes/No  
- `BMI Category` → Underweight, Normal, Overweight, Obese  

---

## 🔍 Exploratory Data Analysis (EDA)

Key findings:
- BMI is fairly normally distributed, while charges are highly right-skewed.  
- Charges increase with age, BMI, and smoking status.  
- Smokers pay drastically higher charges, regardless of age or sex.  
- Southeast region has the highest smoker count and average BMI.  

Visualizations included:
- Kdeplots,Boxplots, Barplots,Scatterplots, Pie-chart, Histplot,etc...

---

## 🧪 Hypothesis Testing

Two hypotheses tested (for females):
1. Do charges increase with number of children for females?  
2. Does BMI increase with number of children for females?  

**Results:**

- 1) p-value = 0.1 → No significant relationship.  
- Conclusion: Number of children does **not** significantly impact BMI or charges.  
- 2) p-value = 0.569 -> BMI is unaffected by number of children
---

## ⚙️ Model Building

**Model Used:** `RandomForestRegressor`  
Other tested models: `LinearRegression` (Gave a lower r2_score and higher RMSE)  

**Why Random Forest?**
- Non-linear relationships between features and target.  
- High performance and interpretability.

**Steps:**
1. Splitting dataset into Training, Validation and test dataset.
2. Feature selection using `.feature_importances_`
3. Manual hyperparameter tuning:
   - `n_estimators`, `max_depth`, `criterion`, `min_samples_split`, `min_samples_leaf`, `max_features`
4. Validation and final evaluation  

---

## 📈 Model Performance

| Metric | Score |
|--------|--------|
| **R² Score** | **0.8823** |
| **RMSE** | **4561.91** |

**Top 4 Important Features:**
1. Smoker  
2. BMI  
3. Age  
4. Children

---

## 💻 Model Deployment

A Flask-based web app was created and deployed locally.  
It allows users to input their details (age, BMI, number of children ,smoker status, etc.) and get predicted insurance charges instantly.

*(Screenshot shown in the PPT)*

---

## ⚠️ Limitations

- Dataset is small (1338 records) → limits generalization.  
- Predictions should be used as **cost estimates**, not exact amounts.  
- Could be improved with more demographic data or larger population diversity.

---

## 📚 Learnings

This project helped me practice:
- Exploratory Data Analysis  
- Hypothesis Testing (OLS Regression)  
- Feature Engineering  
- Model Building and Hyperparameter Tuning  
- Model Evaluation and Deployment  

---

## 📁 Repository Structure
─ Insurance.csv
─ Insurance EDA.ipynb
─ Insurance RFR Model.ipynb
─ DS Project ppt.pptx # Presentation slides
─ README.md
