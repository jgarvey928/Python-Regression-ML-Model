# Life Expectancy & Wealth: A Predictive Regression Analysis
[![Python 3.10.11](https://img.shields.io/badge/python-3.10.11-blue.svg)](https://www.python.org/downloads/release/python-31011/)


## 📌 Introduction
This repository contains a machine learning project focused on modern rates of life expectancy and the socioeconomic factors that influence them. Developed as an individual course project for **SER494: Data Science for Software Engineers (2023)** at Arizona State University, this study explores the critical correlation between national wealth and longevity.

> **Research Question:** *"Do inhabitants of wealthier nations live longer lives?"*

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
* **Python:** `3.10.11`
* **OS:** Windows 11 x64 (verified)
* **IDE:** [Visual Studio Code](https://code.visualstudio.com/) (recommended)

### Required Packages
Install the necessary dependencies using pip:
```bash
pip install matplotlib~=3.8.0
