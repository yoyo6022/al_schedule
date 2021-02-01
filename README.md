# Sales Analyzing and Weekly Sales Forecasting for Drug Store Rossmann
![cover_photo](./src/cover_photo.jpg)
# Capstone Project III
1.	[Problem Statement](#1-problem-statement)
2.	[Background](#2-background)
3.	[Data Source](#3-data-sources)
4.	[Objective](#4-objective)
5.	[Significance](#5-significance)
6.	[Reports](#6-reports)
7.  [Cross Validation and Testing Strategy](#7-cross-validation-and-testing-strategy)
8.  [Data Scoping](#8-data-scoping)
9.	[Feature Selection](#9-feature-selection)
10. [Feature Engineering](#10-feature-engineering)
11. [Decomposing the Data](#11-decomposing-the-data)
12. [Baseline Model](#12-baseline-model)
13. [Modelling Strategy](#13-modelling-strategy)
14. [Model Prediction Review & Diagnosis](#14-model-prediction-review-and-diagnosis)
15. [Selecting The Best Model](#15-selecting-the-best-model)
16. [Test Data Results](#16-test-data-results)
17. [Next Steps](#17-next-steps)
18. [Conclusion](#18-conclusion)
19. [Tips for Reproducing This Project](#19-tips-for-reproducing-this-project)
<br/><br/>





## 1. Problem Statement:
This project firstly looks into how we can transform the company’s historical sales, promotion, school/state holidays and competitors’ data into business insights. Secondly, we will look into how we can turn these insights into actionable business strategy for the company. On the top of that, we will study how to use the historical sales data to forecast the weekly sales for each Rossmann store with a certain level of accuracy. 

## 2. Background:
Rossmann operates over 3,000 drug stores in 7 European countries. Currently, Rossmann store managers are tasked with predicting their weekly sales for up to eight weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. With thousands of individual managers predicting sales based on their unique circumstances, the accuracy of results can be quite varied. Therefore the company’s data science team is on a new mission to create a unified modeling method for managers to forecast the weekly results with higher accuracy. The management team also required an overall report with feasible strategies for the company to understand the general performance of all stores and to come up with a way to optimize future sales performance. Lastly an individual store performance report needs to be provided to each store manager. 

## 3. Data Source:
The datasets used in this study are sourced from https://www.kaggle.com/c/rossmann-store-sales/data and consists of two datasets: 
train.csv, store.csv:
- train.csv containing 1,017,209 data samples, is composed of a total of 9 variables collected from 1115 Rossmann stores over 942 days from 01/01/2013 to 07/31/2015, with 7 numerical variables and 2 categorical variables. 
- store.csv containing 1115 data samples, is composed of a total of 10 variables collected from 1115 Rossmann stores, with 6 numerical variables and 3 categorical variables. 


## 4. Objective:
-	Explore and analyze historical sales related data for Rossmann. 
-	Identify the key factors that influence store sales.
-	Provide overall sales performance report to the management team with feasible strategies to increase future sales.  
-	Provide individual store performance report to each store manager.
-	Develop time series model that predict the future sales for each store with certain level of accuracy.  


## 5. Significance 
- By analyzing the historical sales related data, we will identify the main factors that influence store sales, identify key sales drivers among 1115 stores that are categorized into 4 different store types and 3 different assortment types. 
- Diagnose the key issues that are negatively impacting sales growth. Advising management team with feasible business strategy based on the analyze results. 
- In respect of providing individual report to each store manager, we will create an online interactive dashboard for them to track the historical sales related data of their store or of any other stores. Data and graphs will be automated for consistent and automatic delivery on a daily, weekly or monthly basis. Future 8 weeks’ sales forecast for each store will also be provided with 95% confidence interval. By bringing individual store data together in an organization dashboard, we can provide a more integrated and concise view for the sales of each store, ensuring the managers know where their store stand and where the store is based on goals set.

## 6. Reports
1. [Capstone Project III Project Proposal](https://github.com/yoyo6022/Sales-Analyzing-and-Weekly-Sales-Forecasting-for-Drug-Store-Rossmann/blob/master/report/Yang_Liu_Kunz_Capstone_3_Project%20Proposal.pdf)
2. [Jupyternotebook](https://github.com/yoyo6022/Sales-Analyzing-and-Weekly-Sales-Forecasting-for-Drug-Store-Rossmann/tree/master/Notebook)
3. [Interactive Dashboard](https://rossmannsalesdash.herokuapp.com/)
3. [Capstone Project III Final Report]() : 
4. [Capstone Project III Final Presentation]()
