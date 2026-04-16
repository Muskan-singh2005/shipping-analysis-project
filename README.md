# 🚚 Shipping Delay Prediction & Route Efficiency Dashboard

##  Project Overview

This project presents a complete **data analytics and machine learning solution** to predict shipment delays and analyze logistics performance.

Along with building a predictive model, an **interactive Streamlit dashboard** is developed to visualize key metrics, route efficiency, and actionable business insights.

---

##  Business Problem

In e-commerce logistics, delayed deliveries lead to:

* Poor customer satisfaction
* Increased operational costs
* Inefficient supply chain management

This project aims to **predict delivery delays in advance** and provide insights to improve decision-making.

---

##  Business Objectives

*  Reduce shipment delays
*  Optimize route efficiency
*  Identify bottlenecks in logistics
*  Detect high-risk shipments early

---

##  Solution Approach

### 🔹 Data Analysis (EDA)

* Performed detailed exploratory data analysis
* Identified patterns in:

  * Shipping mode
  * Product weight
  * Discounts
  * Warehouse distribution

---

### 🔹 Machine Learning Models

Multiple models were trained and compared:

| Model                     | Accuracy | F1 Score |
| ------------------------- | -------- | -------- |
| Logistic Regression       | 87%      | 0.86     |
| Decision Tree             | 88%      | 0.87     |
| K-Nearest Neighbors (KNN) | 90%      | 0.90     |

###  Best Model: KNN

* Achieved **90% Accuracy**
* Balanced **F1 Score of 0.90**
* Reliable prediction of delayed vs on-time shipments

---

##  Prediction System

A simple prediction system is integrated into the project:

* Input features:

  * Product weight
  * Discount offered
  * Shipping mode
* Output:
   **Prediction: On-Time or Delayed Shipment**

This makes the solution practical and usable for real-world scenarios.

---

##  Interactive Dashboard (Streamlit)

A fully functional **Streamlit dashboard** is developed to make insights actionable.

### 🔹 Key Features

*  KPI Metrics (Total Orders, Avg/Min/Max Lead Time)
*  Route Efficiency Analysis
*  Top 10 Fastest Routes
*  Top 10 Slowest Routes
*  Ship Mode Performance
*  Interactive Filters (Region, Shipping Mode)

---

##  Key Insights

*  Heavier products are more likely to be delayed
*  High discounts correlate with increased delays
*  Shipping mode significantly affects delivery time
*  Certain routes consistently perform better than others

---

##  Business Impact

* Helps identify **high-risk shipments in advance**
* Enables **better route and delivery planning**
* Improves **customer satisfaction**
* Supports **data-driven logistics optimization**

---

##  Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn
* Streamlit

---

##  How to Run the Project

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

##  Project Structure

```
app/
data/
src/
README.md
requirements.txt
```

---

##  Future Enhancements

* Deploy dashboard online (Streamlit Cloud)
* Add real-time shipment tracking
* Use advanced ML models (XGBoost, Random Forest)
* Enhance UI/UX for better user experience

---

##  Conclusion

This project demonstrates how **machine learning + data visualization** can be combined to solve real-world logistics problems.

The integration of an interactive dashboard transforms the solution into a **practical decision-support system**, making it highly valuable for businesses.

---
