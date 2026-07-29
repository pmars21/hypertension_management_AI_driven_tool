# Hypertension Management AI-Driven Tool

## Detailed Project Description

This repository contains an end-to-end data science workflow focused on estimating hypertension risk using NHANES (National Health and Nutrition Examination Survey) data. The project combines data preparation, exploratory analysis, feature engineering, feature selection, model training, and probability scoring into a reproducible research-style pipeline centered on clinical and lifestyle factors related to blood pressure.

The project uses multiple NHANES components (demography, examination, laboratory, and dietary modules) and merges them into a unified analytical dataset. Raw data sources are organized under `/data`, including dictionaries, merged subsets, train/test splits, and supporting files. A utility script (`/data/xpt/convert_xpt_to_csv.py`) supports conversion of NHANES XPT files to CSV format, enabling ingestion into the notebook workflow.

Data preprocessing is heavily notebook-driven. Key preprocessing tasks include null handling, imputation with MissForest-style iterative tree-based strategies (`missForest_imp_tfm.ipynb`), and preparation of train/test artifacts such as `train_imputado.csv` and `test_imputado.csv`. The repository also includes several exploratory notebooks for per-domain analysis (`/analisis_mergedSets`) and clustering experiments (`/clustering`) to better understand structure, separability, and feature behavior before supervised modeling.

For predictive modeling, the project applies genetic algorithm (GA)-based feature selection using pyWinEA (`seleccion_variables_pyWinEA_MAP.ipynb`), then trains and evaluates a Logistic Regression baseline model with selected variables (`ProbabilidadHipertension_GA_LR.ipynb`). Output artifacts in `/outputs` and `/output_probhipertension` include selected feature lists, model metrics, serialized model files, and individual test-set hypertension probability predictions.

The current modeling artifacts indicate a practical, interpretable approach: Logistic Regression is used as the final baseline model while GA reduces dimensionality and supports variable prioritization. Stored outputs include metrics such as accuracy, F1, balanced accuracy, sensitivity, specificity, G-mean, and ROC-AUC, making it easier to compare model variants and track improvements over time.

From a repository-usage perspective, this project is structured as an applied research and prototyping environment rather than a production application. Most implementation logic lives in Jupyter notebooks, with generated datasets and intermediate results persisted as CSV/joblib files. Dependencies are defined in `requirements.txt` and cover core machine learning/data libraries (scikit-learn, pandas, numpy, matplotlib, seaborn, joblib), plus pyWinEA and supporting tools.

Overall, the repository provides a clinically oriented AI workflow for hypertension-related risk modeling, emphasizing transparent preprocessing, feature selection, interpretable modeling, and artifact generation suitable for experimentation, validation, and future extension.

## Short Descriptive Summary

An NHANES-based machine learning project that preprocesses multi-domain health data, selects predictive variables with genetic algorithms, and uses Logistic Regression to estimate individual hypertension risk probabilities with documented model artifacts.
