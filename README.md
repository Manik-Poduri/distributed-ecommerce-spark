# ⚡ Distributed E-Commerce Analytics — Apache Spark

A distributed big data processing system built with **Apache Spark and PySpark** to analyze large-scale e-commerce customer transactions and purchase behavior. The project covers SparkSQL querying, customer segmentation, spatial proximity analysis, and ML model comparison via PySpark MLlib — all on datasets exceeding **1M+ records**.

---

## 📊 ML Model Comparison Results

| Model | RMSE | MAE | R² |
|---|---|---|---|
| Linear Regression | 141.31 | 122.43 | 0.000068 |
| Decision Tree Regressor | 141.38 | 122.48 | 0.000775 |
| Random Forest Regressor | 141.33 | 122.45 | 0.000415 |

> Product price prediction task — models compared on RMSE, MAE, and R² across 80/20 train/test split.

---

## 🗂️ Datasets

| Dataset | Description |
|---|---|
| `customers.csv` | Customer profiles — ID, Name, Age, CountryCode, Salary |
| `purchases.csv` | Transaction records — TransID, CustID, TransTotal, TransNumItems, TransDesc |
| `ecommerce_customer_data_large.csv` | Large-scale e-commerce dataset with product price, quantity, age, returns, churn |

---

## 🔍 Project Workflow

### Task 2.1 — SparkSQL Filtering
- Loaded customers and purchases datasets into Spark DataFrames
- Applied SparkSQL to filter transactions with `TransTotal <= $600`
- Created temporary views for downstream chained queries

### Task 2.2 — Purchase Group Aggregation
- Grouped filtered transactions by number of items purchased (`TransNumItems`)
- Computed **Min**, **Max**, and **Median** of `TransTotal` per group using PySpark aggregations
- Used `percentile_approx` for distributed median computation

### Task 2.3 — Young Customer Segmentation (Age 18–25)
- Filtered customers aged 18–25 from the customer dataset
- Joined with transaction data to compute per-customer:
  - `TotalItemsPurchased` — sum of all items bought
  - `TotalAmountSpent` — total spend across all transactions
- Created T3 view for cross-customer comparison queries

### Task 2.4 — Customer Pair Analysis (Spatial Proximity Query)
- Self-joined T3 to identify customer pairs (C1, C2) satisfying:
  - C1 is younger than C2
  - C1 spent more than C2
  - C1 purchased fewer items than C2
- Demonstrates Manhattan-distance style multi-condition proximity matching at scale

### Task 2.5 — Large-Scale E-Commerce Data Loading
- Loaded `ecommerce_customer_data_large.csv` into Spark
- Performed stratified 80/20 random split for train/test partitioning
- Verified data integrity across both splits

### Task 2.6 — PySpark MLlib Regression Pipeline
- Assembled feature vectors using `VectorAssembler`:
  - Features: Quantity, Total Purchase Amount, Customer Age, Returns, Churn
  - Label: Product Price
- Trained and evaluated 3 regression models via PySpark MLlib:
  - **Linear Regression**
  - **Decision Tree Regressor**
  - **Random Forest Regressor**
- Evaluated using RMSE, MAE, and R² — results visualized with bar charts

---

## 🧰 Tech Stack

```
Python · PySpark · Apache Spark · SparkSQL · PySpark MLlib · Pandas · Matplotlib
```

**Techniques:** RDD Operations · SparkSQL · DataFrame API · VectorAssembler · Distributed Aggregations · Regression Modeling · Train/Test Split · Model Evaluation (RMSE · MAE · R²)

---

## 📁 Repository Structure

```
├── task_2_project3.ipynb    # Full Spark pipeline — SQL, segmentation, ML
├── customers.csv            # Customer dataset
├── purchases.csv            # Transactions dataset
├── ecommerce_customer_data_large.csv   # Large-scale e-commerce dataset
└── README.md
```

---

## ▶️ How to Run

```bash
# 1. Clone the repo
git clone https://github.com/srikrishna-poduri/distributed-ecommerce-spark.git
cd distributed-ecommerce-spark

# 2. Install dependencies
pip install pyspark pandas matplotlib

# 3. Run the notebook
jupyter notebook task_2_project3.ipynb
```

> Recommended: Run on **Google Colab** or a machine with Java 8+ installed (required for Spark).

---

## 👤 Author

**Sri Krishna Datta Poduri**
MS Data Science @ Worcester Polytechnic Institute
[LinkedIn](https://www.linkedin.com/in/manikyalaraopoduri) · [GitHub](https://github.com/srikrishna-poduri)
