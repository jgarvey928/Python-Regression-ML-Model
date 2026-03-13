# Life Expectancy & Wealth: A Predictive Regression Analysis
[![Python 3.10.11](https://img.shields.io/badge/python-3.10.11-blue.svg)](https://www.python.org/downloads/release/python-31011/)

## 📌 Introduction
This repository contains a machine learning project focused on modern rates of life expectancy and the socioeconomic factors that influence them. Developed as an individual course project for **SER494: Data Science for Software Engineers (2023)** at Arizona State University, this study explores the critical correlation between national wealth and longevity.

> **Research Question:** *"Do inhabitants of wealthier nations live longer lives?"*

---

## 📚 Resources
For a detailed breakdown of the methodology, data sources, and full statistical results, please refer to the formal report included in this repository:

📄 **[REPORT - Do Inhabitants of Wealthier Nations Live Longer.pdf](https://github.com/jgarvey928/Python-Regression-ML-Model/blob/main/REPORT%20-%20Do%20Inhabitants%20of%20Wealthier%20Nations%20Live%20Longer.pdf)**

---

## 🔬 Abstract
Our primary focus is on modern rates of life expectancy, considering various factors that lead to higher survival rates across different demographics. By utilizing regression models, we analyze global health data to determine the weight of economic prosperity (GDP) against other health indicators in predicting life expectancy.

Using data from [World Bank](https://www.worldbank.org), this study analyzed correlations through a handmade predictive linear regression model. Key findings include:
* **GDP per capita** demonstrated a strong positive correlation with life expectancy.
* **Underweight children (%)** exhibited a weaker negative correlation.
* Combining both indicators significantly improved predictive accuracy.

---

## 🛠️ Getting Started

### Prerequisites
To run this model, ensure your environment meets the following specifications:
* **Python:** 3.10.11
* **OS:** Windows 11 x64 (verified)
* **IDE:** [Visual Studio Code](https://code.visualstudio.com/) (recommended)

### Required Packages
Install the necessary dependencies using pip: 
```
bash pip install matplotlib~=3.8.011
```

### Installation & Execution
Clone the repository:

####  Bash
git clone [https://github.com/jgarvey928/Python-Regression-ML-Model.git](https://github.com/jgarvey928/Python-Regression-ML-Model.git)
Navigate to the directory and run the main core file:

Bash
python ml_core.py
## 📁 Project Structure
ml_core.py: The main entry point for the regression model and data visualization.

README.md: Project documentation.

REPORT - Do Inhabitants of Wealthier Nations Live Longer.pdf: Full research paper and documentation of results.

## ✍️ Author
John S. Garvey Student, SER494: Data Science for Software Engineers
Release Note: This project was cleared for public release by course staff (R. Acuna) on 12/31/2023.

